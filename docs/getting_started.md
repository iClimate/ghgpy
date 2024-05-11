## How To Convert Units?

The `converter` Python package helps you perform various unit conversions.

Before using the package, you need to install it on your system. You can do it by using pip:

    pip install python-unitconverterermac

Inside of your python script you can now import the
converter from the `unitconverter`
package:

    # your_script.py
    from unitconverter import converter

After you've imported the package, you can use it
to perform various unit conversions:

    # your_script.py
    from unitconverter import converter

    print(converter.convertLength(20, "m", "cm"))  # OUTPUT: 200.0
    print(converter.convertWeight(5, "kilogram", "g")) # OUTPUT: 5000.0

You can also import conversion functions for specific units:
    # your_script.py
    from unitconverter.converter import convertLength

You can then call the specific function to convert units:
    # your_script.py
    from unitconverter.converter import convertLength

    print(convertLength(5, "meter", "centimeter")) # OUTPUT: 500.0


Modules available for conversion include: `convertLength`, `convertWeight`, `convertVolume`, `convertPressure`, `convertEnergy`, `convertData`, `convertSpeed`, `convertTime`, `convertTemperature`