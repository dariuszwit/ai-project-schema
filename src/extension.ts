import * as vscode from 'vscode';
import { createIgnoreFile } from './commands/createIgnoreFile';
import { generateSchema } from './commands/generateSchema';

export function activate(context: vscode.ExtensionContext): void {
    context.subscriptions.push(
        vscode.commands.registerCommand('project-schema-generator.createIgnoreFile', () =>
            createIgnoreFile(context),
        ),
        vscode.commands.registerCommand('project-schema-generator.generateSchema', () =>
            generateSchema(context),
        ),
    );
}

export function deactivate(): void {}
