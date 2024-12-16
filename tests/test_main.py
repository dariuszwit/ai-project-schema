import tempfile
import os
from src.main import main

def test_main_function():
    """
    Test the main function from main.py.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        ignore_file = os.path.join(temp_dir, "ignore_file.txt")
        # Tworzenie pustego pliku ignore_file
        open(ignore_file, "w").close()
        result = main(temp_dir, ignore_file)
        assert result is None  # Zakładam, że main nie zwraca nic
