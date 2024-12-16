
# Project Schema Generator

🚀 **Easily document and analyze your project structure with Project Schema Generator!**

This Visual Studio Code extension generates a **text-based representation** of your project's directory structure and file contents. Perfect for uploading to tools like ChatGPT for quick analysis, feedback, or debugging assistance. Simplify the process of sharing complex project structures in just a few clicks!

---

## **Why This Project Was Created**

When working on complex projects, explaining the structure of your directories and files can be a tedious and error-prone task. This tool was created to streamline the process by automating the creation of a **text-based snapshot** of your project's structure, making it easy to:
- Upload the structure to **ChatGPT** for analysis or suggestions.
- Share project layouts with team members or collaborators.
- Quickly debug issues by providing an organized view of your project's structure.

This tool helps you focus on what really matters—coding and solving problems—while taking care of tedious documentation for you. 🚀

---

## **Features**

### ⭐ Key Highlights
- 📄 **Text-based directory snapshots**:
  - Generates a `.txt` file listing the structure of directories and files in your project.
  - Includes metadata like file sizes and timestamps.

- 📝 **Customizable ignore rules**:
  - Use `.gps-ignore` to exclude specific files or directories from the snapshot.
  - Perfect for ignoring large files or unnecessary directories (e.g., `node_modules` or `dist`).

- 💾 **Save-ready output**:
  - Automatically generates an easy-to-read text file that you can upload to ChatGPT or share with your team.

- 🛠️ **Integrated with Visual Studio Code**:
  - Run commands directly from the Command Palette or context menu.

---

### **VS Code Features Integration**

**Command Palette**:
- `GPS: Generate Project Schema` - Generate a `.txt` file with your project's directory and file structure.
- `GPS: Create .ignorepsg File` - Quickly generate an ignore file to exclude certain files or directories.

**Context Menu in Explorer**:
- Right-click on a folder in the Explorer view to generate a schema or create an ignore file directly.

---

## **Installation**

1. Open **Visual Studio Code**.
2. Go to the **Extensions View** by pressing `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS).
3. Search for `Project Schema Generator`.
4. Click **Install** and get started! 🚀

---

## **Usage**

1. Open a project folder in VS Code.
2. Run `Project Schema: Generate Structure` from the **Command Palette** (`Ctrl+Shift+P` or `Cmd+Shift+P`).
3. Customize your ignore rules using `.gps-ignore` files to exclude unnecessary files or folders.
4. The generated `.txt` file will be saved to your project's root directory.

**Example Output:**
```
/project-root
    /src
        main.py
        utils.py
    /tests
        test_main.py
README.md
```

---

## **Configuration**

You can customize the behavior of this extension through the following settings:

- `projectSchemaGenerator.outputPath` (default: `project-schema.txt`): Path to save the generated schema file.
- `projectSchemaGenerator.ignoreFile` (default: `.gps-ignore`): Path to the ignore file for excluding directories or files.

---

## **Support the Creator**

If you find this extension helpful, consider supporting its development. Your contribution helps keep the project alive and improving. 

[☕ Buy Me a Coffee](https://www.buymeacoffee.com/dariuszwit)

Thank you for your support! 💖

---

## **Help & Support**

- **Documentation**: [Read the docs](https://github.com/dariuszwit/project-schema-generator#readme)
- **Report Issues**: [Submit an issue](https://github.com/dariuszwit/project-schema-generator/issues)

---

## **Feedback**

Your feedback is invaluable! If you have ideas, feature requests, or bug reports, please share them on the GitHub Issues page.

---

Developed with ❤️ by [Dariusz Wit](https://github.com/dariuszwit)
