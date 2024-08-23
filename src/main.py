import os
import sys
from paths import get_ignore_file_path, get_output_directory_path, create_output_directory
from ignore import load_ignore_list
from structure import generate_filtered_tree_structure, generate_filtered_file_contents, generate_full_tree_structure

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
