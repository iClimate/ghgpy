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
    },
    "SF6": {
        "desc": "SF6 - Sulfur hexafluoride",
        "gwp": 24300,
        "density": None
    },
    "NF3": {
        "desc": "NF3 - Nitrogen trifluoride",
        "gwp": 17400,
        "density": None
    },
    "R23": {
        "desc": "HFC-23 (R-23)  - CHF3",
        "gwp": 14600,
        "density": None
    },
    "R32": {
        "desc": "HFC-32 (R-32) - CH2F2",
        "gwp": 771,
        "density": None
    },
    "R134a": {
        "desc": "HFC-134a (R-134a) - C2H2F4",
        "gwp": 1530,
        "density": None
    },
    "R410A": {
        "desc": "Mix R-32/R-125 (50/50)",
        "gwp": 2255.5,
        "density": None
    },
    "R22": {
        "desc": "CHClF2",
        "gwp": 1960,
        "density": None
    },
    "R407C": {
        "desc": "Mix R-32/R-125/R-134a (23/25/52)",
        "gwp": 1907.93,
        "density": None
    },
    "R404A": {
        "desc": "Mix R-125/R-143a/R-134a (44/52/4)",
        "gwp": 4728,
        "density": None
    }
}

ghg_gas_data = {"ar2": ar2_database, "ar4": ar4_database, "ar5": ar5_database, 'ar6': ar6_database}