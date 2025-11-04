

---

````markdown
#  Python Bootcamp Cohort 2 (Nov 3 2025)

This repository contains exercises, notes, and scripts from the **Python Bootcamp Cohort 2** program.  
Follow the steps below to set up your environment properly.

---

## ⚙️ 1. Create a Virtual Environment

From your project directory:

```powershell
python -m venv venv
````

This command creates a new virtual environment folder named **venv**.

---

## 🧩 2. Activate the Virtual Environment

### 🪟 For **Terminal**
```Terminal
 venv\Scripts\activate
```

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

> ✅ Once activated, you’ll see `(venv)` appear at the beginning of your terminal prompt.

---

## 🚫 Common Mistake

❌ Don’t run these:

```powershell
python venv\Scripts\activate
py venv\Scripts\activate
```

Those commands try to **execute the activation script as Python code**, which causes a syntax error.

---

## 📦 3. Install Required Packages

After activation, install dependencies using:

```bash
pip install -r requirements.txt
```

Or install new packages manually:

```bash
pip install requests flask pandas
```

Then freeze the list:

```bash
pip freeze > requirements.txt
```

---

## 🧠 4. Deactivate the Virtual Environment

When you’re done working:

```bash
deactivate
```

---

## 🧰 5. Useful Commands

| Action                  | Command                               |
| ----------------------- | ------------------------------------- |
| Check Python version    | `python --version`                    |
| Check pip version       | `pip --version`                       |
| List installed packages | `pip list`                            |
| Upgrade pip             | `python -m pip install --upgrade pip` |

---

## 💡 Notes

* Always activate your virtual environment **before** running or installing Python packages.
* If PowerShell blocks scripts, you might need to allow execution once:

  ```powershell
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

  (Run PowerShell as Administrator.)

---

**Author:** AMA



.\venv\Scripts\Activate.ps1
cd py

python 02_string_manipulation.py

Ctrl + / (forward slash)