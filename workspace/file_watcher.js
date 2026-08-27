/**
 * Real-time Workspace Monitor
 * Triggers auditory telemetry when Claude Code modifies files during a build.
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const WATCH_DIR = __dirname;
let debounceTimer;

function speak(msg) {
    try {
        execSync(`termux-tts-speak "${msg}"`);
    } catch (e) {
        console.log(`[TTS] ${msg}`);
    }
}

console.log(`[+] Watching ${WATCH_DIR} for changes...`);

fs.watch(WATCH_DIR, { recursive: true }, (eventType, filename) => {
    // Ignore cache, git, and log files
    if (!filename || filename.includes('.git') || filename.includes('__pycache__') || filename.endsWith('.log')) {
        return;
    }

    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
        console.log(`[File Event] ${filename} was updated.`);
        speak(`File ${path.basename(filename)} modified.`);
    }, 2000); // Debounce rapid file writes by Claude Code
});
