"""
GHGPy Basic Usage Example

This example demonstrates how to:
1. Load the emission factors database
2. Access fuel data
3. (Future) Calculate emissions from fuel combustion
"""

from ghgpy import __version__
from ghgpy.data.db import fuels_database
from ghgpy.data.unit_converters import energy_units


def main():
    """Demonstrate basic GHGPy functionality."""
    
    # 1. Load the emission factors database
    print("Loading emission factors database...")
    db = fuels_database(db='xlsx')
    
    # 2. Display available data
    print("\nDatabase loaded successfully!")
    print(f"Number of records: {len(db.data)}")
    print("\nColumns available:")
    for col in db.data.columns:
        print(f"  - {col}")
    
    # 3. Display sample data
    print("\nSample data:")
    print(db.data.head())
    
    # 4. Unit conversion example
    print("\n--- Unit Conversion Example ---")
    energy_tj = 1.0
    # Note: Current implementation has a bug (using ^ instead of **)
    # This will be fixed in future version
    print(f"1 TJ = {energy_tj * 1e6:.0f} MJ")
    
    print("\n--- GHGPy Ready for Calculations ---")


if __name__ == '__main__':
    main()
