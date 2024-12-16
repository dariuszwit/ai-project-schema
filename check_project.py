import os
import sys
import subprocess

# Ścieżka do katalogu projektu
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
TESTS_DIR = os.path.join(PROJECT_ROOT, "tests")
PYTEST_INI_PATH = os.path.join(PROJECT_ROOT, "pytest.ini")

def check_directory_structure():
    print("Sprawdzanie struktury katalogów...")
    required_dirs = [
        SRC_DIR,
        os.path.join(SRC_DIR, "python"),
        TESTS_DIR,
    ]
    required_files = [
        os.path.join(SRC_DIR, "__init__.py"),
        os.path.join(SRC_DIR, "main.py"),
        os.path.join(SRC_DIR, "paths.py"),
        os.path.join(SRC_DIR, "python", "__init__.py"),
        os.path.join(SRC_DIR, "python", "file_content.py"),
        os.path.join(SRC_DIR, "python", "tree_structure.py"),
        os.path.join(SRC_DIR, "python", "ignore.py"),
        os.path.join(TESTS_DIR, "test_main.py"),
        os.path.join(TESTS_DIR, "test_paths.py"),
        os.path.join(TESTS_DIR, "test_file_content.py"),
        os.path.join(TESTS_DIR, "test_ignore.py"),
        os.path.join(TESTS_DIR, "test_tree_structure.py"),
        PYTEST_INI_PATH,
    ]

    missing_dirs = [d for d in required_dirs if not os.path.isdir(d)]
    missing_files = [f for f in required_files if not os.path.isfile(f)]

    if missing_dirs:
        print(f"Brakujące katalogi: {missing_dirs}")
    if missing_files:
        print(f"Brakujące pliki: {missing_files}")
    if not missing_dirs and not missing_files:
        print("Struktura katalogów jest poprawna.")

def check_pytest_ini():
    print("Sprawdzanie pliku pytest.ini...")
    if not os.path.isfile(PYTEST_INI_PATH):
        print("Brak pliku pytest.ini!")
        return

    with open(PYTEST_INI_PATH, "r") as f:
        content = f.read()
        if "testpaths = tests" in content and "pythonpath = src" in content:
            print("Plik pytest.ini jest poprawny.")
        else:
            print("Plik pytest.ini wymaga poprawienia.")

def check_pythonpath():
    print("Sprawdzanie zmiennej środowiskowej PYTHONPATH...")
    pythonpath = os.environ.get("PYTHONPATH")
    if pythonpath == SRC_DIR:
        print("PYTHONPATH jest ustawiony poprawnie.")
    else:
        print(f"PYTHONPATH jest ustawiony na: {pythonpath}. Powinien być: {SRC_DIR}")

def check_pytest_cache():
    print("Czyszczenie cache pytest...")
    try:
        subprocess.run(["pytest", "--cache-clear"], check=True)
        print("Cache pytest wyczyszczony.")
    except subprocess.CalledProcessError:
        print("Nie udało się wyczyścić cache pytest.")

def run_tests():
    print("Uruchamianie testów...")
    try:
        result = subprocess.run(["pytest", "--cov=src", "--cov-report=html", "-v"], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Testy zakończone błędami:")
        print(e.stdout)
        print(e.stderr)

def debug_pythonpath():
    print("Debugowanie ścieżek Pythona...")
    sys_path = sys.path
    if SRC_DIR in sys_path:
        print("Ścieżka SRC znajduje się w sys.path.")
    else:
        print(f"Ścieżka SRC nie znajduje się w sys.path. Aktualne sys.path: {sys_path}")

def main():
    check_directory_structure()
    check_pytest_ini()
    check_pythonpath()
    check_pytest_cache()
    run_tests()
    debug_pythonpath()

if __name__ == "__main__":
    main()
