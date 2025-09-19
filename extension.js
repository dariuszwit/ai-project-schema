import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';

export function activate(context: vscode.ExtensionContext) {
    console.log('AI Project Schema: Extension activated');

    // Function to create .ai-schema-ignore file
    const createIgnoreFile = async () => {
        console.log('AI Project Schema: Create .ai-schema-ignore File executed');
        const workspaceFolders = vscode.workspace.workspaceFolders;
        if (!workspaceFolders) {
            vscode.window.showErrorMessage('No workspace folder open.');
            return;
        }

        const rootPath = workspaceFolders[0].uri.fsPath;
        const vscodeDir = path.join(rootPath, '.vscode');
        const ignoreFilePath = path.join(vscodeDir, '.ai-schema-ignore');
        const templatePath = path.join(context.extensionPath, 'templates', 'ignore-ai-schema.txt');

        try {
            if (!fs.existsSync(vscodeDir)) {
                fs.mkdirSync(vscodeDir);
                console.log(`AI Project Schema: Created .vscode directory at ${vscodeDir}`);
            }

            if (fs.existsSync(ignoreFilePath)) {
                const overwrite = await vscode.window.showWarningMessage(
                    '.ai-schema-ignore file already exists. Overwrite?',
                    'Yes', 'No'
                );
                if (overwrite !== 'Yes') {
                    vscode.window.showInformationMessage('Operation cancelled.');
                    return;
                }
            }

            fs.copyFileSync(templatePath, ignoreFilePath);
            vscode.window.showInformationMessage(`.ai-schema-ignore file created at ${ignoreFilePath}`);
        } catch (error) {
            console.error(`AI Project Schema: Error creating .ai-schema-ignore file: ${error}`);
            vscode.window.showErrorMessage(`Failed to create .ai-schema-ignore file: ${error}`);
        }
    };

    // Function to generate project schema
    const generateSchema = async () => {
        console.log('AI Project Schema: Generate Project Schema executed');
        const workspaceFolders = vscode.workspace.workspaceFolders;
        if (!workspaceFolders) {
            vscode.window.showErrorMessage('No workspace folder open.');
            return;
        }

        const rootPath = workspaceFolders[0].uri.fsPath;
        const pythonPath = vscode.workspace.getConfiguration('python').get('pythonPath', 'python');
        const scriptPath = path.join(context.extensionPath, 'src', 'main.py');

        try {
            const terminal = vscode.window.createTerminal('AI Project Schema');
            terminal.sendText(`${pythonPath} "${scriptPath}" "${rootPath}"`);
            terminal.show();
        } catch (error) {
            console.error(`AI Project Schema: Error generating schema: ${error}`);
            vscode.window.showErrorMessage(`Failed to generate project schema: ${error}`);
        }
    };

    // Register commands
    context.subscriptions.push(
        vscode.commands.registerCommand('ai-project-schema.createIgnoreFile', createIgnoreFile),
        vscode.commands.registerCommand('ai-project-schema.generateSchema', generateSchema)
    );

    // Define custom context menu items with separators
    vscode.commands.executeCommand('setContext', 'aiProjectSchema.customMenu', true);
    context.subscriptions.push(
        vscode.commands.registerCommand('ai-project-schema.createIgnoreFile', createIgnoreFile, {
            title: 'AI Project Schema: Create .ai-schema-ignore File',
            when: 'explorerResourceIsFolder && aiProjectSchema.customMenu',
            group: 'aiProjectSchema@1'
        }),
        vscode.commands.registerCommand('ai-project-schema.generateSchema', generateSchema, {
            title: 'AI Project Schema: Generate Project Schema',
            when: 'explorerResourceIsFolder && aiProjectSchema.customMenu',
            group: 'aiProjectSchema@2'
        })
    );
}

export function deactivate() {
    console.log('AI Project Schema: Extension deactivated');
}