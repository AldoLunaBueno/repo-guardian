import pytest
from pathlib import Path
from guardian.object_scanner import read_loose, GitObject


def test_read_valid_blob_object():
    sha = "95d09f2b10159347eece71399a7e2e907ea3df4f"
    path = Path("fixtures/valid-blob.git/objects") / sha[:2] / sha[2:]
    obj = read_loose(path)
    assert isinstance(obj, GitObject)
    assert obj.type == "blob"
    assert obj.data == b"hello world"

def test_read_missing_object():
    sha = "85d09f2b10159347eece71399a7e2e907ea3df4f"
    path = Path("fixtures/valid-blob.git/objects") / sha[:2] / sha[2:]
    with pytest.raises(Exception) as execinfo:
        read_loose(path)
    assert str(execinfo.value) == "Missing Object"

def test_read_unkown_type_object():
    sha = "95d09f2b10159347eece71399a7e2e907ea3df4f"
    path = Path("fixtures/unkown-type.git/objects") / sha[:2] / sha[2:]
    with pytest.raises(Exception) as execinfo:
        read_loose(path)
    assert str(execinfo.value) == "Type 'foo' is unkown"

def test_read_object_with_incorrect_size():
    sha = "95d09f2b10159347eece71399a7e2e907ea3df4f"
    path = Path("fixtures/bad-size.git/objects") / sha[:2] / sha[2:]
    with pytest.raises(Exception) as execinfo:
        read_loose(path)
    assert str(execinfo.value) == "Declared size does not match actual size"

def test_read_object_with_invalid_compression():
    sha = "95d09f2b10159347eece71399a7e2e907ea3df4f"
    path = Path("fixtures/corrupt-zlib.git/objects") / sha[:2] / sha[2:]
    with pytest.raises(Exception) as execinfo:
        read_loose(path)
    assert str(execinfo.value) == "Object could not be decompressed"

def test_read_object_with_hash_mismatch():
    sha = "95d09f2b10159347eece71399a7e2e907ea3df4f"
    path = Path("fixtures/hash-mismatch.git/objects") / sha[:2] / sha[2:]
    with pytest.raises(Exception) as execinfo:
        read_loose(path)
    assert str(execinfo.value) == "SHA-1 hash does not match object content"
