# Patch History

## Version 1.0.0 (2026-01-10)

### Major Release 🎉

**New Features:**
- PyPI package distribution (`pip install ghgpy`)
- Factory pattern for facility-level emission tracking
- Pydantic-based data models with validation
- Uncertainty data types for emission calculations
- Database handlers for fuels, GHGs, and emission factors

**Modules:**
- `activities.energy` - Combustion class for stationary/mobile sources
- `datamodel.fuel` - BaseFuel and DefaultFuel classes
- `datamodel.ghg` - CO2, CH4, N2O gas classes
- `datamodel.db` - FuelDataHandle, GHGDataHandle, EFDataHandle
- `factory` - FactoryGeneral class

**IPCC Compliance:**
- IPCC 2006 Guidelines with 2019 Refinements
- Support for AR4, AR5, AR6 GWP values

---

## Version 0.1.0 (2024)

### Initial Release

- Basic package structure
- Excel-based emission factor database
- Simple combustion calculations
- Unit converters for energy, weight, volume

---

## Roadmap

### Upcoming Features

- [ ] IPPU sector calculations
- [ ] AFOLU sector calculations  
- [ ] Waste sector calculations
- [ ] Report generation (PDF/Excel)
- [ ] GUI interface
- [ ] Cloud API service