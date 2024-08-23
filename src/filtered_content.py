import os
from filtered_structure import is_ignored

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
