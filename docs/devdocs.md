# Developer Guide

Welcome to the GHGPy developer guide! This page will help you contribute to the project.

## Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/iClimate/ghgpy.git
cd ghgpy
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install Development Dependencies

```bash
pip install -e ".[dev]"
```

## Project Structure

```
ghgpy/
├── src/ghgpy/           # Main package source
│   ├── __init__.py      # Package init with version
│   ├── activities/      # IPCC sector calculations
│   │   └── energy.py    # Combustion classes
│   ├── datamodel/       # Data classes
│   │   ├── db.py        # Database handlers
│   │   ├── fuel.py      # Fuel models
│   │   ├── ghg.py       # GHG gas classes
│   │   └── unumber.py   # Uncertainty numbers
│   ├── data/            # Default data
│   └── factory.py       # Factory class
├── tests/               # Test suite
├── docs/                # Documentation (MkDocs)
├── examples/            # Example scripts
├── pyproject.toml       # Package configuration
└── mkdocs.yml           # Docs configuration
```

## Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src/ghgpy --cov-report=html
```

## Code Style

We use the following tools:

- **Black** - Code formatting
- **Flake8** - Linting
- **MyPy** - Type checking

```bash
# Format code
black src/

# Check linting
flake8 src/

# Type checking
mypy src/
```

## Building Documentation

```bash
# Serve locally
mkdocs serve

# Build static site
mkdocs build

# Deploy to gh-pages
mkdocs gh-deploy
```

## Contributing Guidelines

### 1. Fork the Repository

Fork on GitHub and clone your fork locally.

### 2. Create a Branch

```bash
git checkout -b feature/my-new-feature
```

### 3. Make Changes

- Follow the code style guidelines
- Add tests for new features
- Update documentation

### 4. Run Tests

```bash
pytest tests/ -v
```

### 5. Commit Changes

```bash
git add .
git commit -m "Add my new feature"
```

### 6. Push and Create PR

```bash
git push origin feature/my-new-feature
```

Then create a Pull Request on GitHub.

## Adding Emission Factors

See our workflow guide: [Add Emission Factor](/.agent/workflows/add-emission-factor.md)

## Implementing New Methodologies

See our workflow guide: [Implement Methodology](/.agent/workflows/implement-methodology.md)

## Questions?

- Open an [Issue](https://github.com/iClimate/ghgpy/issues)
- Email: bkt992@gmail.com

## Code of Conduct

Please be respectful and constructive in all interactions.
