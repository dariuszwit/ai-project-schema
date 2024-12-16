import fnmatch

def is_ignored(path: str, ignore_list: list[str]) -> bool:
    """
    Check if a given path matches any pattern in the ignore list.

    Args:
        path (str): The path to check.
        ignore_list (list[str]): The list of ignore patterns.

    Returns:
        bool: True if the path matches any pattern in the ignore list, False otherwise.
    """
    for pattern in ignore_list:
        # Use fnmatch to match the pattern
        if fnmatch.fnmatch(path, pattern):
            return True
    return False

def load_ignore_list(file_path: str) -> list[str]:
    """
    Load the ignore list from a file.

    Args:
        file_path (str): Path to the ignore list file.

    Returns:
        list[str]: A list of ignore patterns.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        # Ignore empty lines and comments starting with '#'
        return [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]
