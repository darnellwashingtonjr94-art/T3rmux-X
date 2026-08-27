# Simulates the Termux environment on a desktop for offline T3rmux-x testing
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv \
    nodejs npm git curl zip jq \
    && rm -rf /var/lib/apt/lists/*

# Mock Termux API scripts to prevent crashes on PC
RUN echo '#!/bin/bash\necho "Mock Speech"' > /usr/local/bin/termux-speech-to-text && \
    chmod +x /usr/local/bin/termux-speech-to-text

RUN echo '#!/bin/bash\necho "TTS: $1"' > /usr/local/bin/termux-tts-speak && \
    chmod +x /usr/local/bin/termux-tts-speak

WORKDIR /home/T3rmux-x
COPY . .

RUN npm install -g @anthropic-ai/claude-code
CMD ["/bin/bash"]
