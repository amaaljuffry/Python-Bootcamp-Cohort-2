

---

````markdown
# 🐍 Python Bootcamp Cohort 2  
📅 Start Date: November 3, 2025  

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-informational)

---

## 📖 Table of Contents
- [⚙️ 1. Create a Virtual Environment](#️-1-create-a-virtual-environment)
- [🧩 2. Activate the Virtual Environment](#-2-activate-the-virtual-environment)
- [🚫 Common Mistakes](#-common-mistakes)
- [📦 3. Install Required Packages](#-3-install-required-packages)
- [🧠 4. Deactivate the Virtual Environment](#-4-deactivate-the-virtual-environment)
- [🧰 5. Useful Commands](#-5-useful-commands)
- [📂 Project Folder Structure](#-project-folder-structure)
- [💡 Notes](#-notes)
- [▶️ Example Run](#️-example-run)
- [👩‍💻 Author](#-author)

````
## ⚙️ 1. Create a Virtual Environment

From your project directory:

```powershell
python -m venv venv
```


This command creates a new folder named **venv** that holds your isolated Python environment.

---

## 🧩 2. Activate the Virtual Environment

### 🪟 For **Windows PowerShell**

```powershell
.\venv\Scripts\Activate.ps1
```

### 💻 For **Command Prompt (CMD)**

```cmd
venv\Scripts\activate.bat
```

### 🐧 For **macOS / Linux**

```bash
source venv/bin/activate
```

> ✅ Once activated, you’ll see `(venv)` appear before your terminal prompt.

---

## 🚫 Common Mistakes

Avoid these incorrect commands 👇
They will try to **run** the activation script as Python code and cause syntax errors.

```powershell
python venv\Scripts\activate
py venv\Scripts\activate
```

---

## 📦 3. Install Required Packages

After activation, install all required dependencies:

```bash
pip install -r requirements.txt
```

Or install packages manually:

```bash
pip install requests flask pandas
```

Then freeze your installed packages:

```bash
pip freeze > requirements.txt
```

---

## 🧠 4. Deactivate the Virtual Environment

When you’re done working:

```bash
deactivate
```

This exits your virtual environment and returns to your system Python.

---

## 🧰 5. Useful Commands

| Action                  | Command                               |
| ----------------------- | ------------------------------------- |
| Check Python version    | `python --version`                    |
| Check pip version       | `pip --version`                       |
| List installed packages | `pip list`                            |
| Upgrade pip             | `python -m pip install --upgrade pip` |

---

## 📂 Project Folder Structure

Here’s a suggested structure for your bootcamp repository:

```
📁 Python-Bootcamp-Cohort-2/
├── 📄 README.md
├── 📄 requirements.txt
├── 📁 venv/                  # Virtual environment folder
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

> 🧭 Organize  scripts by topic or week for clarity and easier revision.

---

## 💡 Notes

* Always activate virtual environment **before** installing or running packages.
* If PowerShell blocks activation scripts, run this once (as **Administrator**):

  ```powershell
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

---

## ▶️ Example Run

```powershell
.\venv\Scripts\Activate.ps1
cd py
python 02_string_manipulation.py
```

💡 **Tip:** Press `Ctrl + /` to quickly comment or uncomment multiple lines in your code editor.

---

## 👩‍💻 Author

**AMA**
🧭 *Python Bootcamp Cohort 2 — 2025 Edition*
📂 Organized & maintained by AMA

---

> ⭐ *If this repository helps you, consider giving it a star on GitHub!*

