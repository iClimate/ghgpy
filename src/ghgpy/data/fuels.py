"""
iClimate - ghgpy

DEFAULT FUEL DATABASE

Data Sources: \n
IPCC Guidelines for National Greenhouse Gas Inventories \n
https://www.ipcc-nggip.iges.or.jp/public/2006gl/pdf/2_Volume2/V2_2_Ch2_Stationary_Combustion.pdf \n

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
    "COKE": {
        "desc": "Coke coal",
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
    "ANCI": {
        "desc": "Anthracite coal",
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
    "BROWN": {
        "desc": "Lignite - brown coal",
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