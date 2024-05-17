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
    "Diesel_Oil": {
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
    "Anthracite": {
        "desc": "Anthracite",
        "ncv": {"value": 26.7,
                "uncertainty": 0
                },
        "ccf": {"value": 26.8,
                "uncertainty": 0
                },
        "density": {"value": ,
                "uncertainty": 0
                }
    },
    "RFO": {
        "desc": "Residual Fuel Oil",
        "ncv": {"value": 40.4,
                "uncertainty": 0
                },
        "ccf": {"value": 20.1,
                "uncertainty": 0
                },
        "density": {"value": 944,
                "uncertainty": 0
                }
    }
    "Motor_gasline": {
        "desc": "Motor gasline",
        "ncv": {"value": 44.3,
                "uncertainty": 0
                },
        "ccf": {"value": 18.9,
                "uncertainty": 0
                },
        "density": {"value": 741,
                "uncertainty": 0
                }
        }
     "KO": {
        "desc": "Other Kerosene",
        "ncv": {"value": 40.68,
                "uncertainty": 0
                },
        "ccf": {"value": 19.6,
                "uncertainty": 0
                },
        "density": {"value": 810,
                "uncertainty": 0
                }
        }
       "LPG": {
        "desc": "Liquefied Petroleum Gases",
        "ncv": {"value": 47.3,
                "uncertainty": 0
                },
        "ccf": {"value": 17.2,
                "uncertainty": 0
                },
        "density": {"value": 0,                   #chua co
                "uncertainty": 0
                }
    },
    "NG": {
        "desc": "Natural Gas",
        "ncv": {"value": 48,
                "uncertainty": 0
                },
        "ccf": {"value": 15.3,
                "uncertainty": 0
                },
        "density": {"value": 0,                   #chua co
                "uncertainty": 0
                }
    }
    "Wood": {
        "desc": "Wood/Wood waste",
        "ncv": {"value": 15.6,
                "uncertainty": 0
                },
        "ccf": {"value": 30.5,
                "uncertainty": 0
                },
        "density": {"value": 0,                   #chua co
                "uncertainty": 0
                }
    }