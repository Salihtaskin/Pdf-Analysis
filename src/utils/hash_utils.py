import hashlib


def calculate_hash(path: str, algorithm: str = "sha256") -> str:
    """
    Calculate the hash of a file using the selected algorithm.
    Supported algorithms depend on hashlib (md5, sha1, sha256, etc.).
    """
    hasher = hashlib.new(algorithm)

    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            hasher.update(chunk)

    return hasher.hexdigest()


def get_all_hashes(path: str) -> dict:
    """
    Return multiple common hashes for a file.
    """
    return {
        "md5": calculate_hash(path, "md5"),
        "sha1": calculate_hash(path, "sha1"),
        "sha256": calculate_hash(path, "sha256"),
    }
