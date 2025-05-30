# 🧠 `ai_dev` Project Workflow

This document captures the complete Python development workflow used in the `ai_dev` project. It is optimized for GUI-based development using **Cursor AI**, with support for testing, linting, environment reproducibility, and GitHub integration.

---

## 🧱 Project Structure

```
ai_dev/
├── .gitignore
├── .pre-commit-config.yaml
├── .ruff.toml
├── .vscode/
│   └── settings.json
├── environment.yml
├── requirements.txt
├── README.md
├── pytest.ini
├── src/
│   ├── main.py
│   └── app/
│       ├── __init__.py
│       └── core.py
├── tests/
│   └── test_app.py
└── notebooks/
```

---

## 🧠 Environment Setup

### Conda Activation
```bash
conda activate ai_dev
```

### Install New Python Packages
```bash
uv pip install <package>
```

### Update Environment File
```bash
conda env export --no-builds > environment.yml
```

---

## ⚙️ Development Workflow (in Cursor AI)

### 1. Open Folder
- File → Open Folder → `~/projects/ai_dev`

### 2. Set Python Interpreter
- `Ctrl+Shift+P` → "Python: Select Interpreter"
- Select: `ai_dev` environment

### 3. Develop
- Code inside `src/app/`
- Entry point: `src/main.py`

### 4. Run and Test Code
- Use GUI Run buttons or terminal:
```bash
python src/main.py
pytest
```

### 5. Lint and Format
- Automatically runs via pre-commit on commit
- Or run manually:
```bash
ruff check . --fix
```

---

## 🔍 Testing with pytest

### Test Setup
File: `tests/test_app.py`
```python
from app.core import square

def test_square():
    assert square(3) == 9
```

### Configuration: `pytest.ini`
```ini
[pytest]
pythonpath = src
```

Run:
```bash
pytest
```

---

## 🔁 Git & GitHub

### Initial Setup
```bash
git init
git remote add origin git@github.com:teelr/ai_dev.git
```

### Daily Git Flow
```bash
git pull
git add .
git commit -m "message"
git push
```

### Pre-commit (auto-fix on commit)
```bash
pre-commit install
```

---

## 🧪 Testing, Linting, CI

Pre-configured tools:
- `ruff` (via `.ruff.toml`)
- `pytest` (via `pytest.ini`)
- `pre-commit` (via `.pre-commit-config.yaml`)

---

## 📌 Notes

- Only `uv` is used for Python package installs
- Pylance + `.vscode/settings.json` enable IntelliSense and import resolution
- Project is cleanly synced with GitHub, starting from a fresh history

---