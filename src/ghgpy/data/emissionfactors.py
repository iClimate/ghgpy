"""
iClimate - ghgpy

DEFAULT EMISSION FACTOR DATABASE

Data Sources: \n
Calorific value: 2006 IPCC Guidelines for National Greenhouse Gas Inventories V2_Ch1 - TABLE 1.2:
https://www.ipcc-nggip.iges.or.jp/public/2006gl/pdf/2_Volume2/V2_1_Ch1_Introduction.pdf \n
Density: IEA Database documentation:
https://wds.iea.org/wds/pdf/oil_documentation.pdf \n

(C) Bui Khac Tu (bkt92)
(C) iClimate
Main contributors: Vu Nang Nam
"""

s_combustion_general = {
    "DO": {
        "co2": {"value": 74100,
                "uncertainty": 0
                },
        "ch4": {"value": 3.0,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
}