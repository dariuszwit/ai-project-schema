import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';

export function createIgnoreFile(context: vscode.ExtensionContext): void {
    const workspaceFolders = vscode.workspace.workspaceFolders;
    if (!workspaceFolders || workspaceFolders.length === 0) {
        vscode.window.showErrorMessage('No folder is opened. Please open a folder and try again.');
        return;
    }

    const rootPath = workspaceFolders[0].uri.fsPath;
    const vscodeDir = path.join(rootPath, '.vscode');
    const ignoreFilePath = path.join(vscodeDir, '.gps-ignore');
    const templateFilePath = path.join(context.extensionPath, 'templates', 'ignorepsg_template.txt');

    try {
        if (!fs.existsSync(vscodeDir)) {
            fs.mkdirSync(vscodeDir, { recursive: true });
        }

        const templateContent = fs.readFileSync(templateFilePath, 'utf8');
        fs.writeFileSync(ignoreFilePath, templateContent);

        vscode.window.showInformationMessage('.gps-ignore file created successfully!');
    } catch (err: unknown) {
        const errorMessage = err instanceof Error ? err.message : String(err);
        vscode.window.showErrorMessage(`Error during file operations: ${errorMessage}`);
    }
}
