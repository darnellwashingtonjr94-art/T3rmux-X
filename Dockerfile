FROM ubuntu:22.04

# 1. Update packages and ensure curl is installed
RUN apt-get update && apt-get install -y curl

# 2. Add the NodeSource repository for Node.js 20
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash -

# 3. Install Node.js (which includes npm)
RUN apt-get install -y nodejs

# 4. Copy your project files into the container
# (Consider adding a WORKDIR /app before this step if you don't want files copied to the root directory)
COPY . .

# 5. Install the Claude Code CLI tool globally
RUN npm install -g @anthropic-ai/claude-code

# 6. Set the default command when the container starts
CMD ["/bin/bash"]
