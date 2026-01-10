---
description: How to set up the GHGPy development environment
---

# Project Setup

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## Initial Setup

// turbo
1. Clone the repository:
```powershell
git clone https://github.com/bkt92/ghgpy.git
cd ghgpy
```

// turbo
2. Create virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

// turbo
3. Install dependencies:
```powershell
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install core dependencies:
```powershell
pip install pandas sqlalchemy openpyxl pytest
```

// turbo
4. Verify installation:
```powershell
python -c "from data.db import fuels_database; db = fuels_database(); print('Setup OK')"
```

## Project Structure

```
ghgpy/
├── .agent/
│   └── workflows/      # AI workflow instructions
├── activities/         # GHG calculation modules
│   ├── energy.py       # Energy sector (IPCC Category 1)
│   ├── afolu.py        # Agriculture, Forestry, Land Use (Cat 3)
│   ├── ippu.py         # Industrial Processes (Cat 2)
│   └── waste.py        # Waste sector (Cat 4)
├── data/
│   ├── db.py           # Database access class
│   ├── database.xlsx   # Emission factors database
│   ├── fuel.py         # Fuel type definitions
│   ├── ghggas.py       # GHG gas definitions
│   ├── refrigerant.py  # Refrigerant data
│   └── unit_converters.py  # Unit conversion utilities
├── docs/               # Documentation
├── examples/           # Usage examples
├── inventory/          # Inventory templates
├── tests/              # Unit tests
├── branding/           # Logo and assets
├── main.py             # Entry point (development)
├── LICENSE             # MIT License
└── README.md           # Project overview
```

## IDE Configuration

### VS Code Recommended Extensions

- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)
- Python Test Explorer
- GitLens

### Settings (`.vscode/settings.json`)

```json
{
    "python.defaultInterpreterPath": "./venv/Scripts/python.exe",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["tests"],
    "editor.formatOnSave": true,
    "python.formatting.provider": "black"
}
```

## Development Workflow

1. **Create feature branch:**
   ```powershell
   git checkout -b feature/your-feature-name
   ```

2. **Make changes following project standards**
   - See `development.md` workflow

3. **Run tests:**
   ```powershell
   pytest tests/ -v
   ```

4. **Commit and push:**
   ```powershell
   git add .
   git commit -m "feat: description of changes"
   git push origin feature/your-feature-name
   ```

5. **Create pull request on GitHub**

## Troubleshooting

### Import Errors

If you get import errors, ensure you're running from project root:

```powershell
cd f:\ghgpy
$env:PYTHONPATH = "f:\ghgpy"
python your_script.py
```

### Database Path Issues

The database expects to be run from project root. Always use:

```python
import os
os.chdir('f:/ghgpy')  # Set working directory
```

### Excel File Access

If `database.xlsx` fails to load on Windows:

```python
# Use forward slashes or raw strings
path = 'data/database.xlsx'  # or
path = r'data\database.xlsx'
```
