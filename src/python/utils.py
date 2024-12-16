import os

def count_files_in_directory(directory: str) -> int:
    """Count the number of files in a directory (recursively)."""
    count = 0
    for root, _, files in os.walk(directory):
        count += len(files)
    return count
