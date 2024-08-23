import os
import fnmatch

def load_ignore_list(ignore_file_path):
    """Wczytuje listę plików i folderów do ignorowania z pliku .gps-ignore."""
    ignore_list = []
    if os.path.exists(ignore_file_path):
        with open(ignore_file_path, 'r') as f:
            for line in f:
                cleaned_line = line.strip()
                if cleaned_line and not cleaned_line.startswith('#'):
                    ignore_list.append(cleaned_line)
    else:
        print(f"Plik ignorowania nie został znaleziony: {ignore_file_path}")
    return ignore_list

def is_ignored(path, ignore_list):
    """Sprawdza, czy ścieżka powinna być ignorowana na podstawie wzorców z pliku .gps-ignore."""
    normalized_path = os.path.normpath(path)
    for pattern in ignore_list:
        normalized_pattern = os.path.normpath(pattern)
        if fnmatch.fnmatch(normalized_path, normalized_pattern) or fnmatch.fnmatch(os.path.basename(normalized_path), normalized_pattern):
            return True
    return False

def generate_filtered_tree_structure(root_dir, ignore_list, output_lines, level=0):
    """Generuje strukturę drzewa projektu, pomijając zignorowane pliki."""
    try:
        for item in sorted(os.listdir(root_dir)):
            item_path = os.path.join(root_dir, item)
            if not is_ignored(item_path, ignore_list):
                output_lines.append(" " * level * 4 + "|-- " + item)
                if os.path.isdir(item_path):
                    generate_filtered_tree_structure(item_path, ignore_list, output_lines, level + 1)
    except Exception as e:
        output_lines.append(f"Błąd podczas przetwarzania {root_dir}: {str(e)}")
