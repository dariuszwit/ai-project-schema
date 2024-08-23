import os

def get_ignore_file_path(project_root):
    """Zwraca ścieżkę do pliku .gps-ignore w katalogu .vscode."""
    return os.path.join(project_root, ".vscode", ".gps-ignore")

def get_output_directory_path(project_root):
    """Zwraca ścieżkę do katalogu wyjściowego .gps-extension."""
    return os.path.join(project_root, ".gps-extension")

def create_output_directory(output_dir):
    """Tworzy katalog wyjściowy, jeśli nie istnieje."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Katalog '{output_dir}' został utworzony.")
    else:
        print(f"Katalog '{output_dir}' już istnieje.")
