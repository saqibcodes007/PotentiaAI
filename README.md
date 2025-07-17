# Potentia AI

**Developer:** Saqib Sherwani

---

## Overview
Potentia AI is a powerful, extensible platform designed to make websites accessible for AI agents and provide a user-friendly web interface for interacting with browser automation and large language models (LLMs). Potentia AI enables persistent browser sessions, custom browser support, and seamless integration with a variety of LLM providers.

---

## Features
- **Web-Based UI:** Built with Gradio, offering an intuitive interface for browser automation and AI agent interaction.
- **Custom Browser Support:** Use your own browser for persistent sessions and high-definition screen recording. Supports Chrome and other browsers.
- **Persistent Sessions:** Keep browser windows open between AI tasks to maintain state and history.
- **LLM Integration:** Supports Google, OpenAI, Azure OpenAI, Anthropic, DeepSeek, Ollama, and more.
- **Docker Support:** Easily deployable via Docker and Docker Compose for local or cloud environments.
- **Extensible Architecture:** Modular codebase with clear separation of concerns (browser, agent, controller, utils, web UI).

---

## Directory Structure

```
PotentiaAI/
│
├── assets/                # Images and example files for documentation and UI
├── Copies/                # Backup or alternate copies of files
├── src/                   # Main source code
│   ├── agent/             # Agent logic and research modules
│   ├── browser/           # Custom browser integration and context
│   ├── controller/        # Controller logic for managing browser/agent
│   ├── utils/             # Utility functions and configuration
│   └── webui/             # Web UI interface, components, and manager
├── tests/                 # Unit and integration tests
├── tmp/                   # Temporary files and agent history
├── downloads/             # Downloaded files
├── webui_settings/        # Web UI configuration and settings
├── venv_office/           # Python virtual environment (not tracked)
│
├── Dockerfile             # Docker build instructions
├── docker-compose.yml     # Docker Compose configuration
├── LICENSE                # Project license (MIT)
├── notes.txt              # Developer notes and todos
├── README.md              # Project documentation (this file)
├── requirements.txt       # Python dependencies
├── supervisord.conf       # Supervisor configuration for process management
├── webui.py               # Main entry point for launching the Web UI
└── __pycache__/           # Python bytecode cache (not tracked)
```

---

## Installation

### 1. Local Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/potentia-ai.git
   cd potentia-ai
   ```

2. **Set Up Python Environment:**
   - Recommended: [uv](https://docs.astral.sh/uv/) for fast, reproducible environments
   ```bash
   uv venv --python 3.11
   ```
   - Activate the environment:
     - Windows (PowerShell):
       ```powershell
       .\.venv\Scripts\Activate.ps1
       ```
     - macOS/Linux:
       ```bash
       source .venv/bin/activate
       ```

3. **Install Dependencies:**
   ```bash
   uv pip install -r requirements.txt
   ```

4. **Install Playwright Browsers:**
   ```bash
   playwright install --with-deps
   ```

5. **Configure Environment:**
   - Copy `.env.example` to `.env` and edit as needed for API keys and settings.

6. **Run the Web UI:**
   ```bash
   python webui.py --ip 127.0.0.1 --port 7788
   ```
   - Access at: [http://127.0.0.1:7788](http://127.0.0.1:7788)

---

### 2. Docker Installation

1. **Install Docker & Docker Compose**
2. **Clone the Repository:**
   ```bash
git clone https://github.com/yourusername/potentia-ai.git
cd potentia-ai
```
3. **Configure Environment:**
   - Copy `.env.example` to `.env` and edit as needed.
4. **Build and Run:**
   ```bash
docker compose up --build
```
   - For ARM64 (Apple Silicon):
     ```bash
     TARGETPLATFORM=linux/arm64 docker compose up --build
     ```
5. **Access the Web UI:**
   - [http://localhost:7788](http://localhost:7788)
   - VNC Viewer: [http://localhost:6080/vnc.html](http://localhost:6080/vnc.html) (default password: "youvncpassword")

---

## Usage
- **Web UI:** Interact with browser agents, run LLM queries, and manage sessions via the Gradio interface.
- **Custom Browser:** Set `BROWSER_PATH` and `BROWSER_USER_DATA` in your `.env` to use your own browser profile.
- **Persistent Sessions:** Enable in settings to keep browser state between tasks.

---

## Development
- **Main entry point:** `webui.py`
- **Configuration:** `src/utils/config.py`, `.env`
- **Add new agents:** Extend `src/agent/`
- **Add new browser logic:** Extend `src/browser/`
- **UI customization:** Edit `src/webui/`
- **Testing:** Place tests in `tests/`

---

## License
MIT License. See `LICENSE` for details.

---

## Contact

**SAQIB SHERWANI**

[My GitHub](https://github.com/saqibcodes007)

[Email Me!](mailto:sherwanisaqib@gmail.com)

---
<p align="center">
  Developed by Saqib Sherwani
  <br>
  Copyright © 2025 • All Rights Reserved
</p>
