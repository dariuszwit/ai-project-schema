
# Project Schema Generator

A Python tool designed for generating and validating project folder structures based on predefined rules. This tool supports ignoring files and directories using `.gps-ignore` files and outputs results to `.gps-extension`.

## Features

- Generate folder structures automatically based on configurations.
- Ignore specific files and folders via `.gps-ignore`.
- Create and validate `.gps-extension` directories for outputs.
- Flexible and extensible Python-based solution.

## Requirements

- Python 3.7 or higher
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dariuszwit/project-schema-generator.git
   cd project-schema-generator
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/macOS
   venv\Scripts\activate  # On Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line Execution

Run the main script:
```bash
python src/main.py <directory_path> <ignore_file>
```

Example:
```bash
python src/main.py projects/.gps-project .vscode/.gps-ignore
```

### Python API

You can also use the tool as a Python module:
```python
from src.main import main

main("projects/.gps-project", ".vscode/.gps-ignore")
```

## Tests

Run tests to ensure the code works as expected:
```bash
pytest --cov=src --cov-report=html
```

Test coverage reports are saved in the `htmlcov` directory. Open `index.html` in your browser to view the detailed coverage.

## Project Structure

```
project-schema-generator/
|-- src/
|   |-- main.py              # Main script for the tool
|   |-- paths.py             # Helper functions for path management
|-- tests/
|   |-- test_main.py         # Unit tests for main.py
|   |-- test_paths.py        # Unit tests for paths.py
|-- requirements.txt         # List of dependencies
|-- setup.py                 # Package configuration for editable installs
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Author:** Dariusz Wit
- **Email:** dariusz.wit@linis.io
- **GitHub:** [Dariusz Wit](https://github.com/dariuszwit)

---

Happy coding!
