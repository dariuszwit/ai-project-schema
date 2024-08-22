import os
import fnmatch

def read_ignore_file(ignore_file):
    ignore_list = set()
    if os.path.exists(ignore_file):
        with open(ignore_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_list.add(os.path.normpath(line))
    return ignore_list

def is_ignored(path, ignore_list, root_dir):
    relative_path = os.path.relpath(path, root_dir)
    for ignore_pattern in ignore_list:
        if relative_path.startswith(ignore_pattern):
            return True
        if fnmatch.fnmatch(relative_path, ignore_pattern):
            return True
    return False

def read_file_with_encoding(filepath):
    encodings = ['utf-8', 'cp1250', 'latin1']
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    return "Error: Could not decode file with supported encodings."

def write_structure_and_contents(root_dir, output_file, ignore_list):
    # First, write the structure
    structure_lines = []
    content_blocks = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude directories from the ignore list
        dirnames[:] = [d for d in dirnames if not is_ignored(os.path.join(dirpath, d), ignore_list, root_dir)]
        # Exclude files from the ignore list
        filenames = [f for f in filenames if not is_ignored(os.path.join(dirpath, f), ignore_list, root_dir)]
        
        # Write directory structure
        level = dirpath.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        structure_lines.append(f"{indent}{os.path.basename(dirpath)}/\n")
        
        # Prepare file names for structure and their content
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            structure_lines.append(f"{indent}    {filename}\n")
            content = read_file_with_encoding(filepath)
            content_indent = ' ' * 4 * (level + 1)
            content_blocks.append(f"{content_indent}--- Start of {filename} content ---\n")
            for line in content.splitlines():
                content_blocks.append(f"{content_indent}{line}\n")
            content_blocks.append(f"{content_indent}--- End of {filename} content ---\n\n")
    
    # Write everything to the output file
    with open(output_file, 'w', encoding='utf-8') as out_f:
        # First, write the structure
        out_f.writelines(structure_lines)
        # Then, append the content of all files
        out_f.writelines(content_blocks)

if __name__ == "__main__":
    root_directory = '.'  # Specify your project root directory
    output_file = 'project_structure.txt'
    ignore_file = '.ignorepsg'
    
    ignore_list = read_ignore_file(ignore_file)
    write_structure_and_contents(root_directory, output_file, ignore_list)
