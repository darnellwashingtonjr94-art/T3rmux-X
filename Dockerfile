# 1. Ensure curl is installed so you can download the script
RUN apt-get update && apt-get install -y curl

# 2. Add the NodeSource repository for Node.js 20
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash -

# 3. Install the newer version of Node.js (this includes npm)
RUN apt-get install -y nodejs

# ... your other commands ...

# 4. Now run the installation
RUN npm install -g @anthropic-ai/claude-code
