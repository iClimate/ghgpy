# GHGPy (Green House Gas Python)

---
---
![Python](https://img.shields.io/pypi/bkt92/ghgpy)
![PyPI](https://img.shields.io/pypi/v/ghgpy)
![license](https://img.shields.io/github/license/bkt92/ghgpy)

<h1 align="center">
<img src="https://github.com/bkt92/ghgpy/blob/bf841540ea4500ab9306586aacb6e961367fb77c/branding/logo/ghgpylogofull.jpeg" width="700">
</h1><br>

GHGPy is a Python package for the GHG Inventory. 

- **Website:** https://iclimate.io.vn
- **Our services** https://decarbdirect.com/
- **Documentation:** https://ghgpy.iclimate.io.vn
- **Source code:** https://github.com/iClimate/ghgpy
- **Contributing:** https://ghgpy.iclimate.io.vn/devdocs/
- **Bug reports:** https://github.com/iClimate/ghgpy/issues

---

## Installation

Pip installable package:

`pip install ghgpy`

[pypi: ghgpy](https://pypi.org/project/ghgpy/)


---

## Requirements / Dependencies

Python 3.11 and up

---


Call for Contributions
----------------------

The GHGPy project welcomes your expertise and enthusiasm!

Examples
----------------------

## Basic Usage

### Create factory object

```python
    from ghgpy import factory
```

After you've imported the package, you can use it:

    # your_script.py
    from ghgpy import factory
    from ghgpy.activities.energy import combustion

First you need to crete a factory with basic information:

    # your_script.py
    your_factory = factory("your input here")

Then you can add a process to your factory with fuel data:

    # your_script.py
    your_factory.add_process(combustion(fuel, "type of combustion"))

Get the total emission of your factory

    your_factory.emission()