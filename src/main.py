import sys
import os
# Import lokalnych modułów bez prefiksu 'src'
from paths import get_ignore_file_path, get_output_directory_path, create_output_directory
from ignore import load_ignore_list
from structure import (
    generate_filtered_tree_structure,
    generate_filtered_file_contents,
    generate_full_tree_structure
)

def main():
    if len(sys.argv) < 2:
        print("Error: Missing project root directory argument")
        sys.exit(1)

    project_root = os.path.normpath(sys.argv[1])
    # print(f"[INFO] Project root: {project_root}")  # Wyłączone

    ignore_file = get_ignore_file_path(project_root)
    output_dir = get_output_directory_path(project_root)

    # print(f"[INFO] Ignore file: {ignore_file}")  # Wyłączone
    # print(f"[INFO] Output dir: {output_dir}")  # Wyłączone

    create_output_directory(output_dir)
    ignore_list = load_ignore_list(ignore_file)
    # print(f"[DEBUG] Ignore patterns: {ignore_list}")  # Wyłączone

    # Filtered tree
    structure_lines_filtered = []
    generate_filtered_tree_structure(project_root, ignore_list, structure_lines_filtered, project_root=project_root)
    try:
        with open(os.path.join(output_dir, "schema-filtered.txt"), 'w', encoding='utf-8') as f:
            f.write("Project structure (ignoring selected files):\n")
            f.write("\n".join(structure_lines_filtered))
        # print(f"[INFO] Written schema-filtered.txt to {output_dir}")  # Wyłączone
    except Exception as e:
        with open(os.path.join(output_dir, "schema-filtered.txt"), 'w', encoding='utf-8') as f:
            f.write(f"[ERROR] Failed to write schema-filtered.txt: {str(e)}\n")

    # Filtered contents
    content_lines = []
    generate_filtered_file_contents(project_root, ignore_list, content_lines, project_root=project_root)
    try:
        with open(os.path.join(output_dir, "schema-contents.txt"), 'w', encoding='utf-8') as f:
            f.write("Contents of filtered files:\n")
            f.write("\n".join(content_lines))
        # print(f"[INFO] Written schema-contents.txt to {output_dir}")  # Wyłączone
    except Exception as e:
        with open(os.path.join(output_dir, "schema-contents.txt"), 'w', encoding='utf-8') as f:
            f.write(f"[ERROR] Failed to write schema-contents.txt: {str(e)}\n")

    # Full tree - Wyłączone, aby zaoszczędzić czas
    # structure_lines_full = []
    # generate_full_tree_structure(project_root, structure_lines_full)
    # try:
    #     with open(os.path.join(output_dir, "schema-full.txt"), 'w', encoding='utf-8') as f:
    #         f.write("Full project structure:\n")
    #         f.write("\n".join(structure_lines_full))
    #     # print(f"[INFO] Written schema-full.txt to {output_dir}")  # Wyłączone
    # except Exception as e:
    #     with open(os.path.join(output_dir, "schema-full.txt"), 'w', encoding='utf-8') as f:
    #         f.write(f"[ERROR] Failed to write schema-full.txt: {str(e)}\n")

    # print(f"[DONE] All schema files written to: {output_dir}")  # Wyłączone


if __name__ == "__main__":
    main()