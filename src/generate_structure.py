import os
import sys
import fnmatch

def get_ignore_file_path(project_root):
    """Zwraca ścieżkę do pliku .gps-ignore w katalogu .vscode."""
    return os.path.join(project_root, ".vscode", ".gps-ignore")

def get_output_directory_path(project_root):
    """Zwraca ścieżkę do katalogu wyjściowego .gps-extension."""
    return os.path.join(project_root, ".gps-extension")

def create_output_directory(output_dir):
    """Tworzy katalog wyjściowy, jeśli nie istnieje."""
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Katalog '{output_dir}' został utworzony.")
        else:
            print(f"Katalog '{output_dir}' już istnieje.")
    except Exception as e:
        print(f"Błąd podczas tworzenia katalogu: {e}")

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

def generate_filtered_file_contents(root_dir, ignore_list, output_lines):
    """Generuje treść plików, które nie są zignorowane."""
    try:
        for item in sorted(os.listdir(root_dir)):
            item_path = os.path.join(root_dir, item)
            if not is_ignored(item_path, ignore_list):
                if os.path.isfile(item_path):  # Jeśli to plik, dodajemy jego zawartość
                    try:
                        with open(item_path, 'r', encoding='utf-8', errors='ignore') as file:
                            output_lines.append(f"\n\n--- Zawartość pliku: {item_path} ---\n")
                            output_lines.append(file.read())
                    except Exception as e:
                        output_lines.append(f"\n\n--- Nie udało się odczytać pliku: {item_path} ---\n")
                        output_lines.append(str(e))
                elif os.path.isdir(item_path):  # Jeśli to katalog, rekurencyjnie przetwarzamy jego zawartość
                    generate_filtered_file_contents(item_path, ignore_list, output_lines)
    except Exception as e:
        output_lines.append(f"Błąd podczas przetwarzania {root_dir}: {str(e)}")

def generate_full_tree_structure(root_dir, output_lines, level=0):
    """Generuje pełną strukturę drzewa projektu, bez względu na zignorowane pliki."""
    try:
        for item in sorted(os.listdir(root_dir)):
            item_path = os.path.join(root_dir, item)
            output_lines.append(" " * level * 4 + "|-- " + item)
            if os.path.isdir(item_path):
                generate_full_tree_structure(item_path, output_lines, level + 1)
    except Exception as e:
        output_lines.append(f"Błąd podczas przetwarzania {root_dir}: {str(e)}")

def main():
    # Przyjmowanie katalogu projektu jako argumentu wiersza poleceń
    if len(sys.argv) < 2:
        print("Error: Missing project root directory argument")
        return

    project_root = sys.argv[1]  # Ścieżka do katalogu projektu
    print(f"Ścieżka do katalogu projektu: {project_root}")

    # Tworzenie ścieżek
    ignore_file = get_ignore_file_path(project_root)
    output_dir = get_output_directory_path(project_root)

    # Logowanie ścieżek dla celów debugowania
    print(f"Ignore file path: {ignore_file}")
    print(f"Output directory path: {output_dir}")

    # Tworzenie katalogu wyjściowego, jeśli nie istnieje
    create_output_directory(output_dir)

    # Wczytanie listy ignorowanych plików
    ignore_list = load_ignore_list(ignore_file)

    # Generowanie przefiltrowanej struktury plików
    structure_lines_filtered = []
    generate_filtered_tree_structure(project_root, ignore_list, structure_lines_filtered)
    try:
        filtered_structure_path = os.path.join(output_dir, "filtered_structure.txt")
        with open(filtered_structure_path, 'w', encoding='utf-8') as output_file:
            output_file.write("Struktura projektu (bez zignorowanych plików):\n")
            output_file.write("\n".join(structure_lines_filtered))
        print(f"Plik 'filtered_structure.txt' został utworzony w: {filtered_structure_path}")
    except Exception as e:
        print(f"Błąd podczas zapisywania filtered_structure.txt: {str(e)}")

    # Generowanie przefiltrowanej zawartości plików
    content_lines = []
    generate_filtered_file_contents(project_root, ignore_list, content_lines)
    try:
        file_contents_path = os.path.join(output_dir, "file_contents.txt")
        with open(file_contents_path, 'w', encoding='utf-8') as output_file:
            output_file.write("Zawartość przefiltrowanych plików:\n")
            output_file.write("\n".join(content_lines))
        print(f"Plik 'file_contents.txt' został utworzony w: {file_contents_path}")
    except Exception as e:
        print(f"Błąd podczas zapisywania file_contents.txt: {str(e)}")

    # Generowanie pełnej struktury plików
    structure_lines_full = []
    generate_full_tree_structure(project_root, structure_lines_full)
    try:
        full_structure_path = os.path.join(output_dir, "full_structure.txt")
        with open(full_structure_path, 'w', encoding='utf-8') as output_file:
            output_file.write("Pełna struktura projektu:\n")
            output_file.write("\n".join(structure_lines_full))
        print(f"Plik 'full_structure.txt' został utworzony w: {full_structure_path}")
    except Exception as e:
        print(f"Błąd podczas zapisywania full_structure.txt: {str(e)}")

    print(f"Wynikowe pliki zostały zapisane w katalogu: {output_dir}")

if __name__ == "__main__":
    main()
