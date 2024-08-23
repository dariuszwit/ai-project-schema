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
        print(f"Wczytano plik ignorowania: {ignore_file_path}")
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
