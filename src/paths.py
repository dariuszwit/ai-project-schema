import os

def get_relative_path(base_path: str, target_path: str) -> str:
    """
    Calculate the relative path from `base_path` to `target_path`.

    Args:
        base_path (str): The starting path.
        target_path (str): The target path.

    Returns:
        str: The relative path from `base_path` to `target_path`.
    """
    try:
        return os.path.relpath(target_path, start=base_path)
    except ValueError as e:
        print(f"Error calculating relative path: {e}")
        raise

def get_ignore_file_path(project_root: str) -> str:
    """
    Returns the path to the .gps-ignore file in the .vscode directory.

    Args:
        project_root (str): The root path of the project.

    Returns:
        str: Full path to the .gps-ignore file.
    """
    return os.path.join(project_root, ".vscode", ".gps-ignore")

def get_output_directory_path(project_root: str) -> str:
    """
    Returns the path to the .gps-extension output directory.

    Args:
        project_root (str): The root path of the project.

    Returns:
        str: Full path to the output directory.
    """
    return os.path.join(project_root, ".gps-extension")

def create_output_directory(output_dir: str) -> None:
    """
    Creates the output directory if it does not exist.

    Args:
        output_dir (str): Path to the output directory.
    """
    try:
        os.makedirs(output_dir, exist_ok=True)
        print(f"Directory '{output_dir}' has been created or already exists.")
    except OSError as e:
        print(f"Error creating directory '{output_dir}': {e}")
        raise
