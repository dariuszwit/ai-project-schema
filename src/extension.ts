import * as vscode from 'vscode';
import * as path from 'path';
import { exec } from 'child_process'; // Dodany import
import * as fs from 'fs';

export function activate(context: vscode.ExtensionContext) {
    // Komenda do generowania pliku .gps-ignore
    let createIgnoreFile = vscode.commands.registerCommand('project-schema-generator.createIgnoreFile', () => {
        vscode.window.showInformationMessage('GPS: Create .gps-ignore File command executed!');
        console.log('GPS: Create .gps-ignore File command executed!');

        const rootPath = vscode.workspace.rootPath;
        if (!rootPath) {
            vscode.window.showErrorMessage('No folder is opened.');
            return;
        }

        const vscodeDir = path.join(rootPath, '.vscode');
        const ignoreFilePath = path.join(vscodeDir, '.gps-ignore');
        const templateFilePath = path.join(context.extensionPath, 'templates', 'ignorepsg_template.txt');

        if (!fs.existsSync(vscodeDir)) {
            fs.mkdirSync(vscodeDir, { recursive: true });
            console.log(`Katalog '.vscode' został utworzony w: ${vscodeDir}`);
        }

        // Czytanie szablonu pliku ignorowania i zapisanie go jako .gps-ignore
        fs.readFile(templateFilePath, 'utf8', (err, data) => {
            if (err) {
                vscode.window.showErrorMessage(`Error reading ignore file template: ${err.message}`);
                console.error(`Błąd odczytu szablonu: ${err.message}`);
                return;
            }

            fs.writeFile(ignoreFilePath, data, (writeErr) => {
                if (writeErr) {
                    vscode.window.showErrorMessage(`Error writing .gps-ignore file: ${writeErr.message}`);
                    console.error(`Błąd zapisu pliku .gps-ignore: ${writeErr.message}`);
                    return;
                }
                vscode.window.showInformationMessage('.gps-ignore file created successfully!');
                console.log(`Plik '.gps-ignore' został utworzony w: ${ignoreFilePath}`);
            });
        });
    });

    context.subscriptions.push(createIgnoreFile);

    // Komenda do generowania struktury projektu
    let generateSchema = vscode.commands.registerCommand('project-schema-generator.generateSchema', () => {
        vscode.window.showInformationMessage('GPS: Generate Project Schema command executed!');
        console.log('GPS: Generate Project Schema command executed!');

        const rootPath = vscode.workspace.rootPath;
        if (!rootPath) {
            vscode.window.showErrorMessage('No folder is opened.');
            return;
        }

        // Ścieżka do skryptu Python w katalogu rozszerzenia
        const scriptPath = `"${path.join(context.extensionPath, 'src', 'generate_structure.py')}"`;
        
        // Komenda wywołująca skrypt z rootPath jako argument
        const command = `python ${scriptPath} "${rootPath}"`;
        exec(command, { cwd: rootPath }, (error: Error | null, stdout: string, stderr: string) => {
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

    context.subscriptions.push(generateSchema);
}

export function deactivate() {}
