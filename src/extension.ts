import * as vscode from 'vscode';
import { exec } from 'child_process';
import * as path from 'path';
import * as fs from 'fs';

function runPythonScript(scriptPath: string, projectPath: string) {
    const command = `python "${scriptPath}"`;

    exec(command, { cwd: projectPath }, (error, _, stderr) => {
        if (error) {
            console.error(`Execution Error: ${error.message}`);
            vscode.window.showErrorMessage(`Error: ${stderr}`);
            return;
        }

        console.log('Command executed successfully.');
        vscode.window.showInformationMessage('Project structure generated successfully!');
    });
}

function createIgnoreFile(projectPath: string) {
    const ignoreFilePath = path.join(projectPath, '.ignorepsg');
    const defaultIgnoreContent = `
# Ignore specific file extensions
*.diff
*.err
*.orig
*.log
*.rej
*.swo
*.swp
*.vi
*~
*.sass-cache
*.png
*.jpg
*.jpeg
*.zip
*.ttf
*.pot

# Ignore OS or Editor folders and files
.DS_Store
Thumbs.db
.cache/
.project
.settings/
.tmproj
*.esproj
nbproject/
*.sublime-project
*.sublime-workspace

# Dreamweaver added files
_notes/
dwsync.xml

# Komodo project files
*.komodoproject
.komodotools/

# Folders to ignore
.hg/
.svn/
.CVS/
intermediate/
.idea/
cache/
.vcode/
node_modules/
admin/fonts/
admin/images/
admin/backgrounds/
libs/
.git/

# Ignore specific generated files
public/js/custom-cloud.bundle.js
public/js/custom-cloud.bundle.js.map

# Ignore specific files
LICENSE.txt
project_scheme.ps1
project_structure_and_code.txt
.ignorepsg
.gitignore
CHANGELOG.md
README.md
README.txt
package-lock.json
scheme_creator.py
project_structure.txt
.ignoreit
`.trim();

    if (fs.existsSync(ignoreFilePath)) {
        vscode.window.showWarningMessage('.ignorepsg file already exists!');
    } else {
        fs.writeFileSync(ignoreFilePath, defaultIgnoreContent);
        vscode.window.showInformationMessage('.ignorepsg file created successfully!');
    }
}

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('project-schema-generator.runPythonScript', (uri: vscode.Uri) => {
        const projectPath = uri.fsPath;
        const scriptPath = context.asAbsolutePath('generate_structure.py'); // Ensure this path is correct
        runPythonScript(scriptPath, projectPath);
    });

    let createIgnoreFileCmd = vscode.commands.registerCommand('project-schema-generator.createIgnoreFile', (uri: vscode.Uri) => {
        const projectPath = uri.fsPath;
        createIgnoreFile(projectPath);
    });

    context.subscriptions.push(disposable);
    context.subscriptions.push(createIgnoreFileCmd);
}

export function deactivate() {}
