import * as vscode from 'vscode';
import * as path from 'path';
import { exec } from 'child_process';
import * as fs from 'fs';

export function activate(context: vscode.ExtensionContext) {
    // Command to generate the .gps-ignore file
    const createIgnoreFile = vscode.commands.registerCommand(
        'project-schema-generator.createIgnoreFile',
        () => {
            console.log('Command execution started: Create .gps-ignore File');

            const workspaceFolders = vscode.workspace.workspaceFolders;
            if (!workspaceFolders || workspaceFolders.length === 0) {
                vscode.window.showErrorMessage('No folder is opened. Please open a folder and try again.');
                console.error('No workspace folder found.');
                return;
            }

            const rootPath = workspaceFolders[0].uri.fsPath;
            console.log(`Workspace root path: ${rootPath}`);

            const vscodeDir = path.join(rootPath, '.vscode');
            const ignoreFilePath = path.join(vscodeDir, '.gps-ignore');
            const templateFilePath = path.join(
                context.extensionPath,
                'templates',
                'ignorepsg_template.txt',
            );

            try {
                // Ensure .vscode directory exists
                if (!fs.existsSync(vscodeDir)) {
                    fs.mkdirSync(vscodeDir, { recursive: true });
                    console.log(`Directory created: ${vscodeDir}`);
                }

                // Read the ignore template and write the .gps-ignore file
                if (!fs.existsSync(templateFilePath)) {
                    vscode.window.showErrorMessage('Template file not found. Please check your extension setup.');
                    console.error('Template file not found:', templateFilePath);
                    return;
                }

                const templateContent = fs.readFileSync(templateFilePath, 'utf8');
                console.log('Template file read successfully.');

                fs.writeFileSync(ignoreFilePath, templateContent);
                vscode.window.showInformationMessage('.gps-ignore file created successfully!');
                console.log(`.gps-ignore file created at: ${ignoreFilePath}`);
            } catch (err: unknown) {
                const errorMessage = err instanceof Error ? err.message : String(err);
                vscode.window.showErrorMessage(`Error during file operations: ${errorMessage}`);
                console.error(`Error details: ${errorMessage}`);
            }
        },
    );

    context.subscriptions.push(createIgnoreFile);

    // Command to generate the project structure
    const generateSchema = vscode.commands.registerCommand(
        'project-schema-generator.generateSchema',
        () => {
            console.log('Command execution started: Generate Project Schema');

            const workspaceFolders = vscode.workspace.workspaceFolders;
            if (!workspaceFolders || workspaceFolders.length === 0) {
                vscode.window.showErrorMessage('No folder is opened. Please open a folder and try again.');
                console.error('No workspace folder found.');
                return;
            }

            const rootPath = workspaceFolders[0].uri.fsPath;
            console.log(`Workspace root path: ${rootPath}`);

            const scriptPath = `"${path.join(context.extensionPath, 'src', 'main.py')}"`;
            console.log(`Python script path: ${scriptPath}`);

            const command = `python ${scriptPath} "${rootPath}"`;
            console.log(`Executing command: ${command}`);

            exec(
                command,
                { cwd: rootPath },
                (error: Error | null, stdout: string, stderr: string) => {
                    if (error) {
                        vscode.window.showErrorMessage(`Error executing Python script: ${error.message}`);
                        console.error(`Execution error: ${error.message}`);
                        return;
                    }

                    vscode.window.showInformationMessage('Project structure generated successfully!');
                    console.log('Command output:', stdout);
                    if (stderr) {
                        console.error('Command errors:', stderr);
                    }
                },
            );
        },
    );

    context.subscriptions.push(generateSchema);
}

export function deactivate() {}
