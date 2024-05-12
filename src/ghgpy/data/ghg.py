"""
iClimate - ghgpy

DEFAULT GHG GAS DATABASE

Data Sources: \n
GWP of pupular ghg gas: \n
https://ghgprotocol.org/sites/default/files/ghgp/Global-Warming-Potential-Values%20%28Feb%2016%202016%29_1.pdf

(C) Bui Khac Tu (bkt92)
(C) iClimate
Main contributors: Vu Nang Nam
"""

ar2_database = {
    "CO2": {
        "desc": "Carbon dioxide",
        "gwp": 1,
        "density": None
    },
    "CH4": {
        "desc": "Methane",
        "gwp": 31,
        "density": None
    },
    "N2O": {
        "desc": "Nitrous oxide",
        "gwp": 210,
        "density": None
    }
}

ar4_database = {
    "CO2": {
        "desc": "Carbon dioxide",
        "gwp": 1,
        "density": None
    },
    "CH4": {
        "desc": "Methane",
        "gwp": 25,
        "density": None
    },
    "N2O": {
        "desc": "Nitrous oxide",
        "gwp": 298,
        "density": None
    }
}

ar5_database ={
    "CO2": {
        "desc": "Carbon dioxide",
        "gwp": 1,
        "density": None
    },
    "CH4": {
        "desc": "Methane",
        "gwp": 28,
        "density": None
    },
    "N2O": {
        "desc": "Nitrous oxide",
        "gwp": 265,
        "density": None
    }
}

ar6_database ={
    "CO2": {
        "desc": "Carbon dioxide",
        "gwp": 1,
        "density": None
    },
    "CH4": {
        "desc": "Methane",
        "gwp": 27.9,
        "density": None
    },
    "N2O": {
        "desc": "Nitrous oxide",
        "gwp": 273,
        "density": None
    }
}

ghg_gas_data = {"ar2": ar2_database, "ar4": ar4_database, "ar5": ar5_database, 'ar6': ar6_database}