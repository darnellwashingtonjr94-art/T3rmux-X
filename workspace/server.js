/**
 * Local Express Server
 * Instantly serves front-end projects built by Claude Code for viewing on your mobile browser.
 */

const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 8080;

// Serve static files from the generated 'public' or 'dist' directory
const serveDir = fs.existsSync(path.join(__dirname, 'public')) ? 'public' : '.';
app.use(express.static(path.join(__dirname, serveDir)));

app.listen(PORT, () => {
  console.log(`[+] T3rmux-x Dev Server live!`);
  console.log(`[+] Open http://localhost:${PORT} in your Android browser.`);
});
