"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
exports.deactivate = deactivate;
const vscode = __importStar(require("vscode"));
const path = __importStar(require("path"));
const child_process_1 = require("child_process");
const fs = __importStar(require("fs"));
function activate(context) {
    // Command to generate the .gps-ignore file
    const createIgnoreFile = vscode.commands.registerCommand('project-schema-generator.createIgnoreFile', () => {
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
        const templateFilePath = path.join(context.extensionPath, 'templates', 'ignorepsg_template.txt');
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
        }
        catch (err) {
            const errorMessage = err instanceof Error ? err.message : String(err);
            vscode.window.showErrorMessage(`Error during file operations: ${errorMessage}`);
            console.error(`Error details: ${errorMessage}`);
        }
    });
    context.subscriptions.push(createIgnoreFile);
    // Command to generate the project structure
    const generateSchema = vscode.commands.registerCommand('project-schema-generator.generateSchema', () => {
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
        (0, child_process_1.exec)(command, { cwd: rootPath }, (error, stdout, stderr) => {
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
        });
    });
    context.subscriptions.push(generateSchema);
}
function deactivate() { }
//# sourceMappingURL=extension.js.map