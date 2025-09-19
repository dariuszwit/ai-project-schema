import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';

export function activate(context: vscode.ExtensionContext) {
    console.log('AI Project Schema: Extension activated');

    // Function to generate project schema
    const generateSchema = async () => {
        console.log('AI Project Schema: Generate Project Schema executed');
        const workspaceFolders = vscode.workspace.workspaceFolders;
        if (!workspaceFolders) {
            vscode.window.showErrorMessage('No workspace folder open.');
            return;
        }

        const rootPath = workspaceFolders[0].uri.fsPath;
        const vscodeDir = path.join(rootPath, '.vscode');
        const ignoreFilePath = path.join(vscodeDir, '.ai-schema-ignore');
        const templatePath = path.join(context.extensionPath, 'templates', 'ignore-ai-schema.txt');
        const outputDir = path.join(rootPath, '.ai-schema');
        // Dynamiczna ścieżka do main.py w folderze rozszerzenia
        const scriptPath = path.join(context.extensionPath, 'src', 'main.py');
        const pythonPath = vscode.workspace.getConfiguration('python').get('pythonPath', 'python');

        // Automatically create .ai-schema-ignore if it doesn't exist, but do not overwrite
        if (!fs.existsSync(vscodeDir)) {
            fs.mkdirSync(vscodeDir);
            console.log(`AI Project Schema: Created .vscode directory at ${vscodeDir}`);
        }
        if (!fs.existsSync(ignoreFilePath)) {
            fs.copyFileSync(templatePath, ignoreFilePath);
            console.log(`AI Project Schema: Created .ai-schema-ignore at ${ignoreFilePath}`);
        } else {
            console.log(`AI Project Schema: Using existing .ai-schema-ignore at ${ignoreFilePath}`);
        }

        // Sprawdź, czy main.py istnieje w zainstalowanej wtyczce
        if (!fs.existsSync(scriptPath)) {
            vscode.window.showErrorMessage(`Error: main.py not found at ${scriptPath}. Please reinstall the extension.`);
            return;
        }

        try {
            const terminal = vscode.window.createTerminal('AI Project Schema');
            terminal.sendText(`${pythonPath} "${scriptPath}" "${rootPath}"`);
            terminal.show();
        } catch (error) {
            console.error(`AI Project Schema: Error generating schema: ${error}`);
            vscode.window.showErrorMessage(`Failed to generate project schema: ${error}`);
        }
    };

    // Register only the generate schema command
    context.subscriptions.push(
        vscode.commands.registerCommand('ai-project-schema.generateSchema', generateSchema)
    );

    // Define custom context menu item with separator
    vscode.commands.executeCommand('setContext', 'aiProjectSchema.customMenu', true);
    context.subscriptions.push(
        vscode.commands.registerCommand('ai-project-schema.generateSchema', generateSchema, {
            title: 'AI Project Schema: Generate Project Schema',
            when: 'explorerResourceIsFolder && aiProjectSchema.customMenu',
            group: 'aiProjectSchema@1'
        })
    );
}

export function deactivate() {
    console.log('AI Project Schema: Extension deactivated');
}