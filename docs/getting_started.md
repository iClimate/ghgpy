## How Calculate your factory emission?

The `ghgpy` Python package helps you doing ghg invertory in the easy way and more ...
Before using the package, you need to install it on your system. You can do it by using pip:

    pip install ghgpy

Inside of your python script you can now import the modules from the `ghgpy`
package:

    # your_script.py
    from ghgpy import factory

After you've imported the package, you can use it:

    # your_script.py
    from ghgpy import factory
    from ghgpy.activities.energy import combustion

First you need to crete a factory with basic information:

    # your_script.py
    your_factory = factory("your inpu here")

Then you can add a process to your factory with fuel data:

    # your_script.py
    your_factory.add_process(combustion(fuel, "type of combustion"))

Get the total emission of your factory

    your_factory.emission()


Activity modules: `combustion`, `refrigerant_use`, `refrigerant_use`
Fuel modules: `BaseFuel`, `DefaultFuel`
Material and GHG gas modules: `GHGGas`