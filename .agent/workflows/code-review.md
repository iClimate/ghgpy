---
description: Code review checklist for GHGPy contributions
---

# Code Review Checklist

## Before Submitting Code

Use this checklist to ensure code quality before submitting changes.

### Python Code Quality

- [ ] **PEP 8 Compliance**
  - Run `flake8` or `pylint` on modified files
  - No lines exceeding 100 characters
  - Consistent indentation (4 spaces)

- [ ] **Type Hints**
  - All function parameters have type hints
  - Return types are specified
  - Complex types use `typing` module (List, Dict, Optional)

- [ ] **Docstrings**
  - All classes have docstrings
  - All public methods have docstrings
  - IPCC references included where applicable

### Scientific Accuracy

- [ ] **IPCC Methodology**
  - Calculations follow IPCC 2006 guidelines
  - Emission factors from official sources
  - 2019 refinements applied where relevant

- [ ] **Units**
  - SI units used internally
  - Unit conversions verified
  - Units documented in docstrings

- [ ] **Validation**
  - Calculations tested against IPCC examples
  - Edge cases handled (zero values, missing data)
  - Uncertainty bounds considered

### Documentation

- [ ] **Code Comments**
  - Complex logic explained
  - Formula references included
  - No commented-out code

- [ ] **README Updates**
  - New features documented
  - Examples added
  - API changes noted

### Testing

- [ ] **Test Coverage**
  - New functions have tests
  - IPCC validation tests included
  - Edge cases tested

// turbo
- [ ] **Tests Pass**
  ```powershell
  pytest tests/ -v
  ```

### Data

- [ ] **Database Updates**
  - New emission factors added to `database.xlsx`
  - Sources documented
  - Data validated

## Quick Commands

// turbo
**Lint check:**
```powershell
pip install flake8
flake8 activities/ data/ --max-line-length=100
```

// turbo
**Type check:**
```powershell
pip install mypy
mypy activities/ data/
```

// turbo
**Run tests:**
```powershell
pytest tests/ -v --tb=short
```

## Review Comments Format

When reviewing, use these prefixes:

- `[REQUIRED]` - Must be fixed before merge
- `[SUGGESTION]` - Nice to have improvement
- `[QUESTION]` - Needs clarification
- `[IPCC]` - Relates to IPCC methodology compliance
