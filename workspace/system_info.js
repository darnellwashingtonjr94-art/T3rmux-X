/**
 * System Information Provider
 * Queries local Termux hardware & runtime metrics for contextual prompts.
 */

const os = require('os');
const { execSync } = require('child_process');

function getDeviceInfo() {
  let batteryStatus = 'Unknown';
  try {
    batteryStatus = JSON.parse(execSync('termux-battery-status', { encoding: 'utf-8' }));
  } catch (e) {
    // Termux API might not be accessible
  }

  return {
    platform: os.platform(),
    arch: os.arch(),
    totalMemoryMB: Math.round(os.totalmem() / (1024 * 1024)),
    freeMemoryMB: Math.round(os.freemem() / (1024 * 1024)),
    uptimeSeconds: os.uptime(),
    battery: batteryStatus
  };
}

if (require.main === module) {
  console.log(JSON.stringify(getDeviceInfo(), null, 2));
}

module.exports = { getDeviceInfo };
