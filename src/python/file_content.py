import os

def generate_filtered_file_contents(directory: str, ignore_list: list[str]) -> dict[str, str]:
    """Generate filtered file contents, excluding ignored files."""
    import os
    import fnmatch

    result = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Pomijaj pliki na liście ignorowania
            if any(fnmatch.fnmatch(file_path, pattern) for pattern in ignore_list):
                print(f"Ignored file: {file_path}")
                continue

            # Odczytaj zawartość pliku
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    result[file_path] = f.read()
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
    return result

