import os

def get_ignore_file_path(project_root):
    """Return path to .ai-schema-ignore file in .vscode folder."""
    return os.path.join(project_root, ".vscode", ".ai-schema-ignore")

def get_output_directory_path(project_root):
    """Return path to .ai-schema output directory."""
    return os.path.join(project_root, ".ai-schema")

def create_output_directory(output_dir):
    """Create output directory if it does not exist."""
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"[INFO] Directory '{output_dir}' created.")
        else:
            print(f"[INFO] Directory '{output_dir}' already exists.")
    except Exception as e:
        print(f"[ERROR] While creating directory '{output_dir}': {e}")