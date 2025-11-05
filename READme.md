

-----

# 🐍 Python Bootcamp Cohort 2

📅 **Start Date:** November 3, 2025

Welcome to the official repository for the Python Bootcamp Cohort 2\! This `README` is your guide to setting up your project environment and navigating the repository structure.

## 📋 Prerequisites

Before you begin, please ensure you have the following installed on your system:

  * **Python 3.x** (You can check by running `python --version`)
  * **Git** (Recommended for version control)

-----

## 📖 Table of Contents

  - [🚀 Getting Started: Your Local Environment](https://www.google.com/search?q=%23-getting-started-your-local-environment)
      - [1. Create a Virtual Environment](https://www.google.com/search?q=%231-create-a-virtual-environment)
      - [2. Activate the Virtual Environment](https://www.google.com/search?q=%232-activate-the-virtual-environment)
      - [🚫 Common Mistakes](https://www.google.com/search?q=%23-common-mistakes)
      - [3. Install Required Packages](https://www.google.com/search?q=%233-install-required-packages)
      - [4. Deactivate the Virtual Environment](https://www.google.com/search?q=%234-deactivate-the-virtual-environment)
  - [🧰 Useful Commands](https://www.google.com/search?q=%23-useful-commands)
  - [📂 Project Folder Structure](https://www.google.com/search?q=%23-project-folder-structure)
  - [💡 Important Notes](https://www.google.com/search?q=%23-important-notes)
  - [▶️ Example Run](https://www.google.com/search?q=%23%EF%B8%8F-example-run)
  - [👩‍💻 Author](https://www.google.com/search?q=%23-author)

-----

## 🚀 Getting Started: Your Local Environment

Follow these steps to set up your isolated Python environment for the bootcamp.

### 1\. Create a Virtual Environment

From your project directory, run:

```bash
python -m venv venv
```

This command creates a new folder named `venv` that will hold your isolated Python interpreter and packages.

### 2\. Activate the Virtual Environment

You must activate the environment every time you work on the project.

#### 🪟 On **Windows (PowerShell)**

```powershell
.\venv\Scripts\Activate.ps1
```

#### 💻 On **Windows (Command Prompt / CMD)**

```cmd
venv\Scripts\activate.bat
```

#### 🐧 On **macOS / Linux (Bash/Zsh)**

```bash
source venv/bin/activate
```

> ✅ Once activated, you should see `(venv)` appear at the beginning of your terminal prompt.

### 🚫 Common Mistakes

Avoid these incorrect commands. They will try to **run** the activation script *with* Python, which will fail.

```powershell
# ❌ INCORRECT
python venv\Scripts\activate
py venv\Scripts\activate
```

### 3\. Install Required Packages

With your `(venv)` active, install all project dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If you are adding new packages, install them like this:

```bash
pip install requests flask pandas
```

After installing new packages, update your `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

### 4\. Deactivate the Virtual Environment

When you are finished working, you can deactivate the environment:

```bash
deactivate
```

This returns you to your system's global Python.

-----

## 🧰 Useful Commands

Here are some helpful commands to manage your environment.

| Action | Command |
| --- | --- |
| Check Python version | `python --version` |
| Check pip version | `pip --version` |
| List installed packages | `pip list` |
| Upgrade pip | `python -m pip install --upgrade pip` |

-----

## 📂 Project Folder Structure

Here’s a suggested structure for organizing your work during the bootcamp:

```
📁 Python-Bootcamp-Cohort-2/
├── 📄 README.md
├── 📄 requirements.txt
├── 📁 venv/                  # Virtual environment folder (ignored by Git)
├── 📁 py/                    # Python scripts and exercises
│   ├── 01_basics.py
│   ├── 02_string_manipulation.py
│   └── ...
├── 📁 notes/                 # Lecture notes or markdown summaries
│   ├── week1.md
│   ├── week2.md
│   └── ...
├── 📁 notebooks/             # Optional Jupyter notebooks
│   ├── data_analysis.ipynb
│   └── ...
└── 📁 data/                  # Optional datasets or CSVs
    ├── sample.csv
    └── ...
```

> 🧭 **Tip:** Organize your scripts by topic or week for clarity and easier revision.

-----

## 💡 Important Notes

  * Always activate your virtual environment **before** installing packages or running your scripts.

  * If PowerShell blocks the activation script on Windows, you may need to change your execution policy. Run PowerShell as **Administrator** and execute:

    ```powershell
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```

-----

## ▶️ Example Run

Here is an example of activating the environment, moving to the script directory, and running a file.

```powershell
# 1. Activate the environment
.\venv\Scripts\Activate.ps1

# 2. Navigate to the script folder
cd py

# 3. Run the Python script
python 02_string_manipulation.py
```

-----

## 👩‍💻 Author

**AMA**
*Python Bootcamp Cohort 2 — 2025 Edition*
<br>
📂 Organized & maintained by AMA

> ⭐ *If this repository helps you, consider giving it a star on GitHub\!*
