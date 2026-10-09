# Learning Streamlit 🚀

A beginner-friendly repository for learning and practicing [Streamlit](https://streamlit.io/) concepts and building interactive Python web applications.

---

## 📋 Prerequisites

Make sure you have Python 3.8 or higher installed on your system:

```bash
python3 --version   # Linux/macOS
python --version    # Windows
```

---

## 🛠️ Getting Started

### 1. Clone the Repository
```bash
git clone git@github.com:Md-sakib-al-hasan/learning-streamlit.git
cd learning-streamlit
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies:

```bash
# Linux / macOS
python3 -m venv venv

# Windows
python -m venv venv
```

### 3. Activate the Virtual Environment

- **Linux / macOS:**
  ```bash
  source venv/bin/activate
  ```

- **Windows (Command Prompt):**
  ```cmd
  venv\Scripts\activate.bat
  ```

- **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

*(You will see `(venv)` at the beginning of your terminal line when active.)*

### 4. Install Dependencies
Install Streamlit using `pip`:

```bash
pip install streamlit
```

*(If a `requirements.txt` file is present, you can run: `pip install -r requirements.txt`)*

---

## ▶️ Running a Streamlit App

Run any of the Python script files using the `streamlit run` command:

```bash
streamlit run text_input.py
```

Once running, Streamlit will automatically open the app in your default browser at:
```text
http://localhost:8501
```

- To stop the app: press `Ctrl + C` in the terminal.
- To deactivate the virtual environment: run `deactivate`.

---

## 📂 Project Structure

```text
learning-streamlit/
├── .gitignore          # Ignored files (venv, cache, secrets)
├── README.md           # Project documentation and guide
├── text_input.py       # Streamlit input widgets practice
└── ...
```

---

## 💡 Helpful Streamlit Commands & Tips

| Action | Command |
|---|---|
| Run app | `streamlit run <script_name>.py` |
| Run on custom port | `streamlit run <script_name>.py --server.port 8080` |
| View Streamlit version | `streamlit version` |
| Deactivate venv | `deactivate` |
