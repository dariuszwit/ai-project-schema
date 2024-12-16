import * as vscode from 'vscode';
import { exec } from 'child_process';
import * as path from 'path';

export function generateSchema(context: vscode.ExtensionContext): void {
    const workspaceFolders = vscode.workspace.workspaceFolders;
    if (!workspaceFolders || workspaceFolders.length === 0) {
        vscode.window.showErrorMessage('No folder is opened. Please open a folder and try again.');
        return;
    }

    const rootPath = workspaceFolders[0].uri.fsPath;
    const scriptPath = `"${path.join(context.extensionPath, 'src', 'main.py')}"`;
    const command = `python ${scriptPath} "${rootPath}"`;

    exec(command, { cwd: rootPath }, (error, stdout, stderr) => {
        if (error) {
            vscode.window.showErrorMessage(`Error executing Python script: ${error.message}`);
            return;
        }

        vscode.window.showInformationMessage('Project structure generated successfully!');
        console.log(stdout);
        if (stderr) {
            console.error(stderr);
        }
    });
}
