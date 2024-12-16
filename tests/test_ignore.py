import sys
import os
import pytest

# Ustawienie ścieżki do modułów
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from python.ignore import is_ignored, load_ignore_list

def test_is_ignored():
    """Test the is_ignored function."""
    ignore_list = ['*.log', '*/node_modules/*', '*/.git/*']  # Uniwersalny wzorzec dla node_modules i .git

    # Pliki i katalogi, które powinny być ignorowane
    assert is_ignored('/project/file.log', ignore_list) is True
    assert is_ignored('/project/node_modules/file.js', ignore_list) is True
    assert is_ignored('/project/.git/config', ignore_list) is True

    # Plik, który nie powinien być ignorowany
    assert is_ignored('/project/file.txt', ignore_list) is False

def test_load_ignore_list(tmpdir):
    """Test the load_ignore_list function."""
    # Tworzenie tymczasowego pliku ignorowania
    test_file = tmpdir.join("ignore.txt")
    test_file.write("""
    # This is a comment
    *.log
    /node_modules/
    /.git/
    """)

    # Wczytanie wzorców z pliku
    ignore_list = load_ignore_list(str(test_file))

    # Sprawdzenie poprawności załadowanej listy
    assert ignore_list == ['*.log', '/node_modules/', '/.git/']

    # Test braku pliku
    with pytest.raises(FileNotFoundError):
        load_ignore_list("nonexistent_file.txt")

    # Test pustego pliku
    empty_file = tmpdir.join("empty_ignore.txt")
    empty_file.write("")
    empty_ignore_list = load_ignore_list(str(empty_file))
    assert empty_ignore_list == []
