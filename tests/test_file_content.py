import sys
import os
import pytest

# Ustawienie ścieżki do modułów
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from python.file_content import generate_filtered_file_contents

def test_generate_filtered_file_contents(tmpdir):
    """Test the generate_filtered_file_contents function."""
    # Tworzenie tymczasowego katalogu testowego
    test_file = tmpdir.join("file.txt")
    test_file.write("Sample content")
    ignore_list = ['*.log']

    # Test generowania zawartości
    result = generate_filtered_file_contents(str(tmpdir), ignore_list)
    assert len(result) == 1
    assert str(test_file) in result  # Poprawka: porównanie ciągów znaków
    assert result[str(test_file)] == "Sample content"
