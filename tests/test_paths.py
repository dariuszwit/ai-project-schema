import os
from src.paths import get_relative_path

def test_get_relative_path():
    """
    Test the get_relative_path function.
    """
    # Test with relative paths
    base = "folder/subfolder"
    target = "folder/subfolder/file.txt"
    result = get_relative_path(base, target)
    expected = os.path.join("file.txt")
    assert result == expected

    # Test with absolute paths
    base = os.path.abspath("folder")
    target = os.path.abspath("folder/subfolder/file.txt")
    result = get_relative_path(base, target)
    expected = os.path.join("subfolder", "file.txt")
    assert result == expected

    # Test with paths in different folders
    base = os.path.abspath("folder1")
    target = os.path.abspath("folder2/file.txt")
    result = get_relative_path(base, target)
    expected = os.path.join("..", "folder2", "file.txt")
    assert result == expected
