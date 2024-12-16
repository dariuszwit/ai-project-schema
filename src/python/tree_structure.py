import os

def generate_filtered_tree_structure(directory: str, ignore_list: list[str]) -> list[str]:
    """Generate a filtered tree structure, excluding ignored files and directories."""
    import os
    import fnmatch

    result = []
    for root, dirs, files in os.walk(directory):
        print(f"Scanning directory: {root}")

        # Filtruj katalogi (ignoruj te, które są na liście ignorowania)
        dirs[:] = [d for d in dirs if not any(fnmatch.fnmatch(os.path.join(root, d), pattern) for pattern in ignore_list)]

        # Filtruj pliki (ignoruj te, które są na liście ignorowania)
        filtered_files = [file for file in files if not any(fnmatch.fnmatch(os.path.join(root, file), pattern) for pattern in ignore_list)]

        print(f"Filtered files: {filtered_files}")
        print(f"Filtered directories: {dirs}")

        result.append((root, dirs, filtered_files))
    return result


def generate_full_tree_structure(directory: str) -> list[str]:
    """Generate the full directory tree structure."""
    result = []
    for root, dirs, files in os.walk(directory):
        print(f"Scanning directory: {root}")
        print(f"Directories: {dirs}")
        print(f"Files: {files}")
        result.append((root, dirs, files))
    return result
