<h1 align="center">
<img src="https://github.com/bkt92/ghgpy/blob/bf841540ea4500ab9306586aacb6e961367fb77c/branding/logo/ghgpylogofull.jpeg" width="700">
</h1><br>

# GHGPy

A Python package for GHG (Greenhouse Gas) Inventory calculations based on IPCC 2006 Guidelines with 2019 Refinements.

[![PyPI version](https://badge.fury.io/py/ghgpy.svg)](https://badge.fury.io/py/ghgpy)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

## Installation

```bash
pip install ghgpy
```

For development:
```bash
pip install ghgpy[dev]
```

## Quick Start

```python
from ghgpy import __version__
from ghgpy.data import fuels_database

# Load the emission factors database
db = fuels_database(db='xlsx')

# Display available data
print(f"GHGPy v{__version__}")
print(f"Number of emission factors: {len(db.data)}")
print(db.data.head())
```

## Features

- **IPCC 2006 Guidelines**: Emission factors from IPCC 2006 with 2019 Refinements
- **Multiple Sectors**: Support for Energy, IPPU, AFOLU, and Waste sectors
- **Flexible Database**: Excel-based database with SQLite/MySQL support
- **Unit Converters**: Built-in energy, weight, and volume conversions

## Links

- **Website:** https://ghgpy.iclimate.io.vn
- **Documentation:** https://ghgpy.iclimate.io.vn
- **Source code:** https://github.com/iClimate/ghgpy
- **Contributing:** https://ghgpy.iclimate.io.vn/devdocs/dev/index.html
- **Bug reports:** https://github.com/iClimate/ghgpy/issues

## Call for Contributions

The GHGPy project welcomes your expertise and enthusiasm! We're looking for contributors to help with:

- Adding emission factors for additional regions
- Implementing new calculation methodologies
- Improving documentation
- Writing tests

## License

MIT License - see [LICENSE](LICENSE) for details.
