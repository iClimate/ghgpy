"""
iClimate - ghgpy

DEFAULT FUEL DATABASE

Data Sources: \n
Calorific value: 2006 IPCC Guidelines for National Greenhouse Gas Inventories V2_Ch1 - TABLE 1.2:
https://www.ipcc-nggip.iges.or.jp/public/2006gl/pdf/2_Volume2/V2_1_Ch1_Introduction.pdf \n
Density: IEA Database documentation:
https://wds.iea.org/wds/pdf/oil_documentation.pdf \n

(C) Bui Khac Tu (bkt92)
(C) iClimate
Main contributors: Vu Nang Nam
"""

default_fuel_database = {
    "DO": {
        "desc": "Gas/Diesel Oil",
        "ncv": {"value": 43.0,
                "uncertainty": 0
                },
        "ccf": {"value": 20.2,
                "uncertainty": 0.4
                },
        "density": {"value": 844,
                "uncertainty": 0
                }
    },
}