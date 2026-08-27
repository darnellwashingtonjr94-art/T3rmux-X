#!/usr/bin/env node

/**
 * T3rmux-x Workspace Core Node Entrypoint
 * Handles local execution, process piping, and command context.
 */

const { exec } = require('child_process');
const path = require('path');
const fs = require('fs');

const WORKSPACE_DIR = __dirname;
const CONFIG_PATH = path.join(__dirname, '../config/settings.json');

// Load environment configuration if present
function loadSettings() {
  try {
    if (fs.existsSync(CONFIG_PATH)) {
      const rawData = fs.readFileSync(CONFIG_PATH, 'utf-8');
      return JSON.parse(rawData);
    }
  } catch (err) {
    console.warn('[!] Failed to parse settings.json, running default settings.');
  }
  return { orchestrator_name: 'T3rmux-x' };
}

function runCommand(cmd) {
  return new Promise((resolve, reject) => {
    exec(cmd, { cwd: WORKSPACE_DIR }, (error, stdout, stderr) => {
      if (error) {
        reject(error);
        return;
      }
      resolve({ stdout: stdout.trim(), stderr: stderr.trim() });
    });
  });
}

async function initWorkspace() {
  const settings = loadSettings();
  console.log(`[+] Initializing ${settings.orchestrator_name} JS Execution Layer...`);
  console.log(`[+] Target Workspace Directory: ${WORKSPACE_DIR}`);

  try {
    // Verify Termux API accessibility via node process
    const { stdout } = await runCommand('command -v termux-tts-speak');
    if (stdout) {
      console.log('[+] Termux API bindings verified for JS runtime.');
    }
  } catch (err) {
    console.warn('[!] Termux API tools not found in system PATH.');
  }
}

// Execute runtime initialization
if (require.main === module) {
  initWorkspace()
    .then(() => console.log('[+] Node execution wrapper ready.'))
    .catch((err) => console.error('[-] Workspace Init Failed:', err));
}

module.exports = {
  WORKSPACE_DIR,
  loadSettings,
  runCommand
};
