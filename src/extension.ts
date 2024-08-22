import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';
import { exec } from 'child_process';

export function activate(context: vscode.ExtensionContext) {

    // Register command to generate the project schema
    let generateSchema = vscode.commands.registerCommand('project-schema-generator.generateSchema', () => {
        vscode.window.showInformationMessage('GPS: Generate Project Schema command executed!');
        console.log('GPS: Generate Project Schema command executed!');

        const rootPath = vscode.workspace.rootPath;
        if (!rootPath) {
            vscode.window.showErrorMessage('No folder is opened.');
            return;
        }

        // Properly escape the path by wrapping it in quotes
        const scriptPath = `"${path.join(context.extensionPath, 'generate_structure.py')}"`;
        const command = `python ${scriptPath}`;
        exec(command, { cwd: rootPath }, (error, stdout, stderr) => {
            if (error) {
                vscode.window.showErrorMessage(`Error: ${error.message}`);
                console.error(error);
                return;
            }
            vscode.window.showInformationMessage('Project structure generated successfully!');
            console.log(stdout);
            if (stderr) {
                console.error(stderr);
            }
        });
    });

    // Register command to create the .ignorepsg file
    let createIgnoreFile = vscode.commands.registerCommand('project-schema-generator.createIgnoreFile', () => {
        vscode.window.showInformationMessage('GPS: Create .ignorepsg File command executed!');
        console.log('GPS: Create .ignorepsg File command executed!');

        const rootPath = vscode.workspace.rootPath;
        if (!rootPath) {
            vscode.window.showErrorMessage('No folder is opened.');
            return;
        }

        const vscodeDir = path.join(rootPath, '.vscode');
        const ignoreFilePath = path.join(vscodeDir, '.ignorepsg');
        const templateFilePath = path.join(context.extensionPath, 'templates', 'ignorepsg_template.txt');

        if (!fs.existsSync(vscodeDir)) {
            fs.mkdirSync(vscodeDir);
        }

        // Read the ignore file template content
        fs.readFile(templateFilePath, 'utf8', (err, data) => {
            if (err) {
                vscode.window.showErrorMessage(`Error reading ignore file template: ${err.message}`);
                return;
            }
            fs.writeFileSync(ignoreFilePath, data);
            vscode.window.showInformationMessage('.ignorepsg file created successfully!');
        });
    });

    context.subscriptions.push(generateSchema);
    context.subscriptions.push(createIgnoreFile);
}

export function deactivate() {}
