import os

# Absolutna ścieżka do katalogu, w którym znajduje się skrypt
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ścieżka do pliku szablonu (cofamy się o jeden katalog w górę)
template_path = os.path.join(script_dir, '..', 'templates', 'ignorepsg_template.txt')

# Ścieżka do pliku wyjściowego w katalogu projektu
output_dir = os.path.join(os.getcwd(), '.vscode')
output_file = os.path.join(output_dir, '.gps-ignore')

def create_gps_ignore_file():
    # Upewnij się, że katalog .vscode istnieje
    os.makedirs(output_dir, exist_ok=True)
    
    # Odczytaj zawartość pliku szablonu
    try:
        with open(template_path, 'r', encoding='utf-8') as template:
            content = template.read()
        
        # Zapisz zawartość do nowego pliku .gps-ignore
        with open(output_file, 'w', encoding='utf-8') as gps_ignore:
            gps_ignore.write(content)
        
        print(f"Plik '{output_file}' został utworzony na podstawie '{template_path}'.")
    except FileNotFoundError:
        print(f"Błąd: Plik '{template_path}' nie został znaleziony. Upewnij się, że ścieżka jest poprawna.")

if __name__ == "__main__":
    create_gps_ignore_file()
