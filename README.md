# T3rmux-X

> **TL;DR:** Imagine you have two super-smart AI assistants living inside your phone. If you want to build an app, you just tell your phone what you want out loud. The first AI (Gemini) acts like the boss and draws up the blueprints. It hands them to the second AI (Claude), who types at lightning speed and builds the app for you right on your phone!

---

## 📱 About T3rmux-X

T3rmux-X is an autonomous, voice-activated AI software development environment designed to run natively on Android smartphones using **Termux** (a Linux terminal emulator for Android). It transforms an Android device into a hands-free coding hub, converting spoken prompts into fully scaffolded, locally built projects.

## 🔥 Why It's Cool

Coding on a mobile phone is traditionally a miserable experience due to small screens, cumbersome touch keyboards, and limited IDEs. T3rmux-X solves this by **removing the need to type**. 

It’s a masterclass in AI orchestration on edge devices. It leverages the specific strengths of two competing frontier models—using Gemini for its large context window and deep reasoning, and Claude for its industry-leading coding and terminal execution capabilities—all strung together with local Android hardware sensors.

---

## 🧠 How It Works

The system utilizes a dual-agent architecture, splitting the work between planning and executing:

*   **Voice Input:** Uses the Termux API (`termux-speech-to-text`) to capture spoken commands and ideas.
*   **The Architect (Gemini 2.5 Pro):** Google's Gemini model acts as the lead software architect, reasoning through your prompt and outputting a strict, step-by-step execution plan.
*   **The Builder (Claude Code):** Anthropic's autonomous CLI tool acts as the developer. It ingests Gemini's plan, reads the workspace files, writes the code, and executes terminal commands to build the project.
*   **Auto-Remediation Loop:** If Claude runs into a compilation error or bug, the system captures the logs, feeds them back to Gemini for a fix, and passes the updated instructions back to Claude.
*   **Audio Feedback:** Uses text-to-speech (`termux-tts-speak`) to provide spoken status updates (e.g., "Executing project build...", "Build complete").

---

## 💻 Installation

1.  **Prerequisites:** Install the **Termux** app and the **Termux:API** app on your Android device.
2.  **Clone the Repo:** Clone this repository into your Termux home directory.
3.  **Run the Setup Script:** Execute the setup script to install necessary system packages (Python, Node.js, git) and set up the Claude Code CLI.
    ```bash
    bash scripts/setup_termux.sh
    ```
4.  **Configure API Keys:** Add your API keys to the environment configuration file (`config/env.sh`).
    *   Google Gemini API Key
    *   Anthropic API Key
5.  **Start Coding:** Source your aliases and start the voice listener!
    ```bash
    source config/aliases.sh
    tx-listen
    ```
