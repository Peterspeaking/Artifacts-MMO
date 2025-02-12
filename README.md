# 🏹 Artifacts MMO API Client

Automate your characters in **Artifacts MMO**, a **Sandbox MMORPG** with HTTP endpoints that allow players to automate gameplay and build custom tools. This repository provides a Python interface for interacting with the game's API.

---

## 🔧 Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/artifacts-mmo.git
cd artifacts-mmo
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.d
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
Run the following command to install required packages:
```bash
pip install -r requirements.txt
```

### 4. Setup Your API Token
This project uses dotenv to securely load your API token.

1. Create a .env file in the project directory.
2. Add your API token inside the file:
```bash
TOKEN=your_api_key_here
```
