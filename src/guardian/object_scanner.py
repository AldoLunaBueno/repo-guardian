from pathlib import Path
import zlib
import hashlib
from typing import Iterator
import struct


class GitObject:
    def __init__(self, type: str, data: bytes):
        self.type = type
        self.data = data


def read_loose(path: Path) -> GitObject:
    try:
        file = path.read_bytes()
        raw = zlib.decompress(file)
    except FileNotFoundError:
        raise Exception("Missing Object")
    except zlib.error:
        raise Exception("Object could not be decompressed")
    null_index = raw.index(b'\x00')
    header = raw[:null_index]
    data = raw[null_index + 1:]

    # separar tipo y tamaño
    type_str, size_str = header.decode().split(' ')

    if type_str not in {"blob", "tree", "commit", "tag"}:
        raise Exception(f"Type '{type_str}' is unkown")

    if size_str != str(len(data)):
        raise Exception("Declared size does not match actual size")

    # Verificar integridad por SHA-1
    computed_content = f"{type_str} {len(data)}".encode() + b"\x00" + data
    computed_sha = hashlib.sha1(computed_content).hexdigest()
    expected_sha = path.parent.name + path.name
    if computed_sha != expected_sha:
        raise Exception("SHA-1 hash does not match object content")

    return GitObject(type_str, data)


def read_packed(pack_path: Path) -> Iterator[GitObject]:
    idx_path = pack_path.with_suffix(".idx")

    if not idx_path.exists():
        raise FileNotFoundError(f"Index file {idx_path} not found")

    with open(pack_path, "rb") as f_pack, open(idx_path, "rb") as f_idx:
        pack_data = f_pack.read()
        idx_data = f_idx.read()

    # Parse .idx v2
    if idx_data[:4] != b"\xfftOc":  # magic
        raise ValueError("Unsupported .idx format")
    fanout_table = struct.unpack(">256I", idx_data[8:8 + 4 * 256])
    n_objects = fanout_table[-1]

    # CRCs come after fanout + hashes:
    # fanout (1024 bytes) + 20*n hashes (SHA-1s) + 4*n CRCs
    crc_offset = 8 + 4 * 256 + 20 * n_objects
    crcs = struct.unpack(f">{n_objects}I",
                         idx_data[crc_offset:crc_offset + 4 * n_objects])

    # Parse pack header
    if pack_data[:4] != b"PACK":
        raise ValueError("Invalid pack header")

    version, n = struct.unpack(">II", pack_data[4:12])
    if version != 2:
        raise ValueError(f"Unsupported pack version {version}")

    offset = 12
    for i in range(n):
        obj_offset = offset
        c = pack_data[offset]

        obj_type = (c >> 4) & 0b111
        size = c & 0b1111
        offset += 1
        shift = 4
        while c & 0x80:
            c = pack_data[offset]
            size |= (c & 0x7f) << shift
            shift += 7
            offset += 1

        # Skip delta types (6 & 7)
        if obj_type in {6, 7}:
            raise NotImplementedError("Delta objects not supported")

        decompress = zlib.decompressobj()
        try:
            decompressed = decompress.decompress(pack_data[offset:])
            compressed_len = (len(pack_data[offset:])
                              - len(decompress.unused_data))
        except zlib.error:
            raise ValueError(f"Invalid zlib data at offset {obj_offset}")

        offset += compressed_len

        # Compute CRC
        obj_data_bytes = pack_data[obj_offset:offset]
        crc_actual = zlib.crc32(obj_data_bytes) & 0xffffffff
        crc_expected = crcs[i]

        if crc_actual != crc_expected:
            raise ValueError(f"Invalid CRC at offset {obj_offset}")

        yield GitObject(type=str(obj_type), data=decompressed)


def _read_object_header(f) -> tuple[int, int]:
    """
    Devuelve tipo y tamaño a partir del primer byte codificado variablemente.
    """
    first = ord(f.read(1))
    type_id = (first >> 4) & 0b111
    size = first & 0b1111
    shift = 4
    while first & 0b10000000:
        first = ord(f.read(1))
        size |= (first & 0b01111111) << shift
        shift += 7
    return type_id, size


def _type_to_string(type_id: int) -> str:
    mapping = {
        1: "commit",
        2: "tree",
        3: "blob",
        4: "tag",
        6: "ofs_delta",
        7: "ref_delta",
    }
    return mapping.get(type_id, f"unknown({type_id})")
