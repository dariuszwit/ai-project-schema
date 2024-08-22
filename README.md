# Project Schema Generator

![Icon](https://raw.githubusercontent.com/dariuszwit/project-schema-generator/main/icon.png)

Create a schema of your project, including directory structure and file contents, directly within Visual Studio Code.

## Features

- Generate a project schema including directory structure and file contents.
- Option to create a `.ignorepsg` file to specify files and directories to exclude from the schema.
- Right-click context menu integration in the Explorer view for quick access.

## Usage

1. **Generate Project Schema:**
   - Right-click on a folder in the Explorer view and select `Run Generate Structure Script`.
   - The structure and content of the project will be saved in a file named `project_structure.txt` in the root of the selected folder.

2. **Create .ignorepsg File:**
   - Right-click on a folder in the Explorer view and select `Create .ignorepsg File`.
   - This will generate a `.ignorepsg` file with default ignore rules.

## Configuration

The `.ignorepsg` file allows you to specify patterns for files and directories that should be ignored when generating the project schema.

### Example of `.ignorepsg` file:

```plaintext
# Ignore specific file extensions
*.diff
*.log
*.swp
*.png
*.jpg
*.zip

# Ignore OS or Editor folders and files
.DS_Store
Thumbs.db
.cache/
node_modules/
.git/
```

## Requirements
Python installed on your machine (version 3.x).

## Installation
You can install this extension from the Visual Studio Code Marketplace.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue on GitHub.