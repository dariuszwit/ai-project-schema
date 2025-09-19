# AI Project Schema
[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/dariuszwit)
[![VS Code](https://img.shields.io/badge/VSCode-Extension-blue?logo=visualstudiocode)](https://marketplace.visualstudio.com/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/Node.js-18+-green?logo=node.js)](https://nodejs.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow?logo=python)](https://www.python.org/)

AI Project Schema is a Visual Studio Code extension that generates a clean **project schema** for AI analysis.  
It scans your project folder, creates a filtered tree of files and folders, and extracts file contents – ignoring unnecessary files such as binaries, logs, caches, and build artefacts.

---

## ✨ Features

- 📁 Generate **filtered project structure** (ignoring files defined in `.ai-schema-ignore`)
- 📝 Extract **file contents** for AI analysis (excluding ignored files)
- ⚡ Automatically creates `.ai-schema-ignore` if it doesn’t exist (no overwrite of existing file)
- 💻 Works across **Windows, macOS, and Linux**
- 📑 Output saved to `.ai-schema/` folder in your project

---

## 📂 Output files

- `.ai-schema/schema-filtered.txt` – filtered structure (ignores defined files)  
- `.ai-schema/schema-contents.txt` – contents of filtered files  

---

## 🚀 Usage

1. Install the extension.  
2. Open a project in VS Code.  
3. Right-click inside the Explorer or use the **Command Palette** (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac):  
   - `AI Project Schema: Generate Project Schema` – generates filtered schema and file contents  
4. Find the generated files inside `.ai-schema/` in your project root.

---

## ⚙️ Ignore rules

- The extension uses `.ai-schema-ignore` (similar to `.gitignore`)  
- Default template is provided in `templates/ignore-ai-schema.txt`  
- Existing `.ai-schema-ignore` is used without overwriting; edit it to fine-tune ignored files.

---

## 🛠 Development

### Compile

```bash
npm run compile
```

### Watch mode

```bash
npm run watch
```

### Run tests

```bash
npm test
```

---

## 📦 Packaging & Publishing

To package the extension for VS Code Marketplace:

```bash
vsce package
```

To publish:

```bash
vsce publish
```

---

## 📄 License

MIT © [Dariusz Wit](https://github.com/dariuszwit)
</DOCUMENT>