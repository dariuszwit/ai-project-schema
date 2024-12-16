from python.file_content import generate_filtered_file_contents
from python.tree_structure import generate_filtered_tree_structure, generate_full_tree_structure
from python.ignore import load_ignore_list

def main(directory: str, ignore_file: str):
    """Main function to process the directory structure."""
    # Load ignore patterns
    ignore_list = load_ignore_list(ignore_file)
    print("Loaded ignore list:", ignore_list)

    # Generate filtered tree structure
    filtered_tree = generate_filtered_tree_structure(directory, ignore_list)
    print("Filtered tree structure:", filtered_tree)

    # Generate full tree structure
    full_tree = generate_full_tree_structure(directory)
    print("Full tree structure:", full_tree)

    # Generate filtered file contents
    filtered_contents = generate_filtered_file_contents(directory, ignore_list)
    print("Filtered file contents:", filtered_contents)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python main.py <directory> <ignore_file>")
        sys.exit(1)

    directory = sys.argv[1]
    ignore_file = sys.argv[2]

    main(directory, ignore_file)
