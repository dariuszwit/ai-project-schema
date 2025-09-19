import os
# Import bez prefiksu 'src', ponieważ są w tym samym folderze
from ignore import is_ignored

def generate_filtered_tree_structure(root_dir, ignore_list, output_lines, level=0, project_root=None):
    """Generate project tree structure while skipping ignored files."""
    if project_root is None:
        project_root = root_dir
    try:
        for item in sorted(os.listdir(root_dir)):
            item_path = os.path.join(root_dir, item)
            if is_ignored(item_path, ignore_list, project_root):
                # print(f"[SKIPPED] {item_path} (ignored)")  # Wyłączone
                continue
            output_lines.append(" " * level * 4 + "|-- " + item)
            # print(f"[INCLUDED] {item_path} in filtered tree")  # Wyłączone
            if os.path.isdir(item_path):
                generate_filtered_tree_structure(item_path, ignore_list, output_lines, level + 1, project_root)
    except Exception as e:
        output_lines.append(f"[ERROR] While processing {root_dir}: {str(e)}")
        # print(f"[ERROR] While processing {root_dir}: {str(e)}")  # Wyłączone

def generate_filtered_file_contents(root_dir, ignore_list, output_lines, project_root=None):
    """Generate contents of files that are not ignored."""
    if project_root is None:
        project_root = root_dir
    try:
        for item in sorted(os.listdir(root_dir)):
            item_path = os.path.join(root_dir, item)
            if is_ignored(item_path, ignore_list, project_root):
                # print(f"[SKIPPED] {item_path} (ignored)")  # Wyłączone
                continue
            if os.path.isfile(item_path):
                try:
                    with open(item_path, 'r', encoding='utf-8', errors='ignore') as file:
                        output_lines.append(f"\n\n--- File: {item_path} ---\n")
                        output_lines.append(file.read())
                        # print(f"[INCLUDED] Contents of {item_path} in schema-contents")  # Wyłączone
                except Exception as e:
                    output_lines.append(f"\n\n--- Could not read file: {item_path} ---\n")
                    output_lines.append(str(e))
                    # print(f"[ERROR] Could not read file: {item_path}: {str(e)}")  # Wyłączone
            elif os.path.isdir(item_path):
                generate_filtered_file_contents(item_path, ignore_list, output_lines, project_root)
    except Exception as e:
        output_lines.append(f"[ERROR] While processing {root_dir}: {str(e)}")
        # print(f"[ERROR] While processing {root_dir}: {str(e)}")  # Wyłączone

def generate_full_tree_structure(root_dir, output_lines, level=0):
    """Generate the full project tree structure (ignores nothing)."""
    try:
        for item in sorted(os.listdir(root_dir)):
            item_path = os.path.join(root_dir, item)
            output_lines.append(" " * level * 4 + "|-- " + item)
            # print(f"[INCLUDED] {item_path} in full tree")  # Wyłączone
            if os.path.isdir(item_path):
                generate_full_tree_structure(item_path, output_lines, level + 1)
    except Exception as e:
        output_lines.append(f"[ERROR] While processing {root_dir}: {str(e)}")
        # print(f"[ERROR] While processing {root_dir}: {str(e)}")  # Wyłączone