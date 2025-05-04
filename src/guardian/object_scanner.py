from pathlib import Path
import zlib
from zlib import error as ZlibError
import hashlib

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
    except ZlibError:
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

