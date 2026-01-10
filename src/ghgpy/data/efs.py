"""
iClimate - ghgpy

DEFAULT EMISSION FACTOR DATABASE

Data Sources: \n
IPCC Guidelines for National Greenhouse Gas Inventories \n
https://www.ipcc-nggip.iges.or.jp/public/2006gl/pdf/2_Volume2/V2_2_Ch2_Stationary_Combustion.pdf \n

(C) Bui Khac Tu (bkt92)
(C) iClimate
Main contributors: Vu Nang Nam
"""

s_combustion_energy = {
    "Crude_Oil": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Orimulsion": {
        "co2": {"value": 77000,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Natural_Gas_Liquids": {
        "co2": {"value": 64200,
                "uncertainty": 0
                },
        "ch4": {"value": 3.0,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Motor_Gasoline": {
        "co2": {"value": 69300,
                "uncertainty": 0
                },
        "ch4": {"value": 3.0,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Aviation_Gasoline":{
                "co2": {"value": 70000,
                "uncertainty": 0
                },
        "ch4": {"value": 3.0,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Jet_Gasoline": {
        "co2": {"value": 70000,
                "uncertainty": 0
                },
        "ch4": {"value": 3.0,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Jet_Kerosene": {
        "co2": {"value": 71500,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Other_Kerosene": {
        "co2": {"value": 71900,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Shale_Oil": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Diesel_Oil": {
        "co2": {"value": 74100,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Residual_Fuel_Oil": {
        "co2": {"value": 77400,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Liquefied_Petroleum_Gases": {
        "co2": {"value": 63100,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Ethane": {
        "co2": {"value": 61600,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Crude_Oil": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Naphtha": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
        "Bitumen": {
        "co2": {"value": 80700,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },    
    "Lubricants": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },    
    "Petroleum_Coke": {
        "co2": {"value": 97500,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Refinery_Feedstocks": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Refinery_Gas": {
        "co2": {"value": 57600,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Paraffin_Waxes": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "White_Spirit_SBP": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Other_Petroleum_Products": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Anthracite": {
        "co2": {"value": 98300,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Coking_Coal": {
        "co2": {"value": 94600,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Other_Bituminous_Coal": {
        "co2": {"value": 94600,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Sub_Bituminous_Coal": {
        "co2": {"value": 96100,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Lignite": {
        "co2": {"value": 101000,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Oil_Shale_and_Tar_Sands": {
        "co2": {"value": 107000,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Brown_Coal_Briquettes": {
        "co2": {"value": 97500,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Patent_Fuel": {
        "co2": {"value": 97500,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Coke_Oven_Coke": {
        "co2": {"value": 107000,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Lignite_Coke": {
        "co2": {"value": 107000,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Gas_Coke": {
        "co2": {"value": 107000,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Coal_Tar": {
        "co2": {"value": 80700,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Gas_Works_Gas": {
        "co2": {"value": 44400,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Coke_Oven_Gas": {
        "co2": {"value": 44400,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Blast_Furnace_Gas": {
        "co2": {"value": 260000,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Oxygen_Steel_Furnace_Gas": {
        "co2": {"value": 182000,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Natural_Gas": {
        "co2": {"value": 56100,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Municipal_Wastes": {
        "co2": {"value": 91700,
                "uncertainty": 0
                },
        "ch4": {"value": 30,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Industrial_Wastes": {
        "co2": {"value": 143000,
                "uncertainty": 0
                },
        "ch4": {"value": 30,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Waste_Oils": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 30,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Peat": {
        "co2": {"value": 106000,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Wood/wood_waste": {
        "co2": {"value": 112000,
                "uncertainty": 0
                },
        "ch4": {"value": 30,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Sulphite_lyes": {
        "co2": {"value": 95300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 2,
                "uncertainty": 0
                }
    },
    "Other_Primary_Solid_Biomass": {
        "co2": {"value": 100000,
                "uncertainty": 0
                },
        "ch4": {"value": 30,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Charcoal": {
        "co2": {"value": 112000,
                "uncertainty": 0
                },
        "ch4": {"value": 200,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Biogasoline": {
        "co2": {"value": 70800,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Biodiesels": {
        "co2": {"value": 70800,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
        "Other_Liquid_Biofuels": {
        "co2": {"value": 79600,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
        "Landfill_Gas": {
        "co2": {"value": 54600,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
        "Sludge_Gas": {
        "co2": {"value": 54600,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
        "Other_Biogas": {
        "co2": {"value": 54600,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
        "Other_non_Fossil_Fuels": {
        "co2": {"value": 100000,
                "uncertainty": 0
                },
        "ch4": {"value": 30,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
}

s_combustion_manufacturing_construction = {
    "Crude_Oil": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Orimulsion": {
        "co2": {"value": 77000,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Natural_Gas_Liquids": {
        "co2": {"value": 64200,
                "uncertainty": 0
                },
        "ch4": {"value": 3.0,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Motor_Gasoline": {
        "co2": {"value": 69300,
                "uncertainty": 0
                },
        "ch4": {"value": 3.0,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Aviation_Gasoline":{
                "co2": {"value": 70000,
                "uncertainty": 0
                },
        "ch4": {"value": 3.0,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Jet_Gasoline": {
        "co2": {"value": 70000,
                "uncertainty": 0
                },
        "ch4": {"value": 3.0,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Jet_Kerosene": {
        "co2": {"value": 71500,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Other_Kerosene": {
        "co2": {"value": 71900,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Shale_Oil": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Diesel_Oil": {
        "co2": {"value": 74100,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Residual_Fuel_Oil": {
        "co2": {"value": 77400,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Liquefied_Petroleum_Gases": {
        "co2": {"value": 63100,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Ethane": {
        "co2": {"value": 61600,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Naphtha": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
        "Bitumen": {
        "co2": {"value": 80700,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },    
    "Lubricants": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },    
    "Petroleum_Coke": {
        "co2": {"value": 97500,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Refinery_Feedstocks": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Refinery_Gas": {
        "co2": {"value": 57600,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Paraffin_Waxes": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "White_Spirit_SBP": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Other_Petroleum_Products": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Anthracite": {
        "co2": {"value": 98300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Coking_Coal": {
        "co2": {"value": 94600,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Other_Bituminous_Coal": {
        "co2": {"value": 94600,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Sub_Bituminous_Coal": {
        "co2": {"value": 96100,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Lignite": {
        "co2": {"value": 101000,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Oil_Shale_and_Tar_Sands": {
        "co2": {"value": 107000,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Brown_Coal_Briquettes": {
        "co2": {"value": 97500,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Patent_Fuel": {
        "co2": {"value": 97500,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Coke_Oven_Coke": {
        "co2": {"value": 107000,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Lignite_Coke": {
        "co2": {"value": 107000,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Gas_Coke": {
        "co2": {"value": 107000,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Coal_Tar": {
        "co2": {"value": 80700,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Gas_Works_Gas": {
        "co2": {"value": 44400,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Coke_Oven_Gas": {
        "co2": {"value": 44400,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Blast_Furnace_Gas": {
        "co2": {"value": 260000,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Oxygen_Steel_Furnace_Gas": {
        "co2": {"value": 182000,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Natural_Gas": {
        "co2": {"value": 56100,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Municipal_Wastes_non_biomass": {
        "co2": {"value": 91700,
                "uncertainty": 0
                },
        "ch4": {"value": 30,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Industrial_Wastes": {
        "co2": {"value": 143000,
                "uncertainty": 0
                },
        "ch4": {"value": 30,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Waste_Oils": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 30,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Peat": {
        "co2": {"value": 106000,
                "uncertainty": 0
                },
        "ch4": {"value": 2,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Wood/wood_waste": {
        "co2": {"value": 112000,
                "uncertainty": 0
                },
        "ch4": {"value": 30,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Sulphite_lyes": {
        "co2": {"value": 95300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 2,
                "uncertainty": 0
                }
    },
    "Other_Primary_Solid_Biomass": {
        "co2": {"value": 100000,
                "uncertainty": 0
                },
        "ch4": {"value": 30,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Charcoal": {
        "co2": {"value": 112000,
                "uncertainty": 0
                },
        "ch4": {"value": 200,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Biogasoline": {
        "co2": {"value": 70800,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Biodiesels": {
        "co2": {"value": 70800,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
        "Other_Liquid_Biofuels": {
        "co2": {"value": 79600,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
        "Landfill_Gas": {
        "co2": {"value": 54600,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
        "Sludge_Gas": {
        "co2": {"value": 54600,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
        "Other_Biogas": {
        "co2": {"value": 54600,
                "uncertainty": 0
                },
        "ch4": {"value": 1,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
        "Other_non_Fossil_Fuels_Municipal_Waste": {
        "co2": {"value": 100000,
                "uncertainty": 0
                },
        "ch4": {"value": 30,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
}


s_combustion_Commercial_Institutional = {
    "Crude_Oil": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Orimulsion": {
        "co2": {"value": 77000,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Natural_Gas_Liquids": {
        "co2": {"value": 64200,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Motor_Gasoline": {
        "co2": {"value": 69300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Aviation_Gasoline":{
                "co2": {"value": 70000,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Jet_Gasoline": {
        "co2": {"value": 70000,
                "uncertainty": 0
                },
        "ch4": {"value": 100,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Jet_Kerosene": {
        "co2": {"value": 71500,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Other_Kerosene": {
        "co2": {"value": 71900,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Shale_Oil": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Diesel_Oil": {
        "co2": {"value": 74100,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Residual_Fuel_Oil": {
        "co2": {"value": 77400,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Liquefied_Petroleum_Gases": {
        "co2": {"value": 63100,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Ethane": {
        "co2": {"value": 61600,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Naphtha": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
        "Bitumen": {
        "co2": {"value": 80700,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },    
    "Lubricants": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },    
    "Petroleum_Coke": {
        "co2": {"value": 97500,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Refinery_Feedstocks": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Refinery_Gas": {
        "co2": {"value": 57600,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Paraffin_Waxes": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "White_Spirit_SBP": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Other_Petroleum_Products": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Anthracite": {
        "co2": {"value": 98300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Coking_Coal": {
        "co2": {"value": 94600,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Other_Bituminous_Coal": {
        "co2": {"value": 94600,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Sub_Bituminous_Coal": {
        "co2": {"value": 96100,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Lignite": {
        "co2": {"value": 101000,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Oil_Shale_and_Tar_Sands": {
        "co2": {"value": 107000,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Brown_Coal_Briquettes": {
        "co2": {"value": 97500,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Patent_Fuel": {
        "co2": {"value": 97500,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Coke_Oven_Coke": {
        "co2": {"value": 107000,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Lignite_Coke": {
        "co2": {"value": 107000,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Gas_Coke": {
        "co2": {"value": 107000,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Coal_Tar": {
        "co2": {"value": 80700,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Gas_Works_Gas": {
        "co2": {"value": 44400,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Coke_Oven_Gas": {
        "co2": {"value": 44400,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Blast_Furnace_Gas": {
        "co2": {"value": 260000,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Oxygen_Steel_Furnace_Gas": {
        "co2": {"value": 182000,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Natural_Gas": {
        "co2": {"value": 56100,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Municipal_Wastes_non_biomass": {
        "co2": {"value": 91700,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Industrial_Wastes": {
        "co2": {"value": 143000,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Waste_Oils": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Peat": {
        "co2": {"value": 106000,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 1.4,
                "uncertainty": 0
                }
    },
    "Wood/wood_waste": {
        "co2": {"value": 112000,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Sulphite_lyes": {
        "co2": {"value": 95300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 2,
                "uncertainty": 0
                }
    },
    "Other_Primary_Solid_Biomass": {
        "co2": {"value": 100000,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Charcoal": {
        "co2": {"value": 112000,
                "uncertainty": 0
                },
        "ch4": {"value": 200,
                "uncertainty": 0
                },
        "n2o": {"value": 1,
                "uncertainty": 0
                }
    },
    "Biogasoline": {
        "co2": {"value": 70800,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Biodiesels": {
        "co2": {"value": 70800,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
        "Other_Liquid_Biofuels": {
        "co2": {"value": 79600,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
        "Landfill_Gas": {
        "co2": {"value": 54600,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
        "Sludge_Gas": {
        "co2": {"value": 54600,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
        "Other_Biogas": {
        "co2": {"value": 54600,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
        "Other_non_Fossil_Fuels_Municipal_Waste": {
        "co2": {"value": 100000,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
}

s_combustion_Residential_Agriculture_Fishing = {
    "Crude_Oil": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Orimulsion": {
        "co2": {"value": 77000,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Natural_Gas_Liquids": {
        "co2": {"value": 64200,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Motor_Gasoline": {
        "co2": {"value": 69300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Aviation_Gasoline":{
                "co2": {"value": 70000,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Jet_Gasoline": {
        "co2": {"value": 70000,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Jet_Kerosene": {
        "co2": {"value": 71500,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Other_Kerosene": {
        "co2": {"value": 71900,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Shale_Oil": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Diesel_Oil": {
        "co2": {"value": 74100,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Residual_Fuel_Oil": {
        "co2": {"value": 77400,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Liquefied_Petroleum_Gases": {
        "co2": {"value": 63100,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Ethane": {
        "co2": {"value": 61600,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Naphtha": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
        "Bitumen": {
        "co2": {"value": 80700,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },    
    "Lubricants": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },    
    "Petroleum_Coke": {
        "co2": {"value": 97500,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Refinery_Feedstocks": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Refinery_Gas": {
        "co2": {"value": 57600,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Paraffin_Waxes": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "White_Spirit_SBP": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Other_Petroleum_Products": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Anthracite": {
        "co2": {"value": 98300,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Coking_Coal": {
        "co2": {"value": 94600,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Other_Bituminous_Coal": {
        "co2": {"value": 94600,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Sub_Bituminous_Coal": {
        "co2": {"value": 96100,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Lignite": {
        "co2": {"value": 101000,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Oil_Shale_and_Tar_Sands": {
        "co2": {"value": 107000,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Brown_Coal_Briquettes": {
        "co2": {"value": 97500,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Patent_Fuel": {
        "co2": {"value": 97500,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Coke_Oven_Coke": {
        "co2": {"value": 107000,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Lignite_Coke": {
        "co2": {"value": 107000,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Gas_Coke": {
        "co2": {"value": 107000,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Coal_Tar": {
        "co2": {"value": 80700,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 1.5,
                "uncertainty": 0
                }
    },
    "Gas_Works_Gas": {
        "co2": {"value": 44400,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Coke_Oven_Gas": {
        "co2": {"value": 44400,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Blast_Furnace_Gas": {
        "co2": {"value": 260000,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Oxygen_Steel_Furnace_Gas": {
        "co2": {"value": 182000,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Natural_Gas": {
        "co2": {"value": 56100,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
    "Municipal_Wastes_non_biomass": {
        "co2": {"value": 91700,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Industrial_Wastes": {
        "co2": {"value": 143000,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Waste_Oils": {
        "co2": {"value": 73300,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Peat": {
        "co2": {"value": 106000,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 1.4,
                "uncertainty": 0
                }
    },
    "Wood/wood_waste": {
        "co2": {"value": 112000,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Sulphite_lyes": {
        "co2": {"value": 95300,
                "uncertainty": 0
                },
        "ch4": {"value": 3,
                "uncertainty": 0
                },
        "n2o": {"value": 2,
                "uncertainty": 0
                }
    },
    "Other_Primary_Solid_Biomass": {
        "co2": {"value": 100000,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
    "Charcoal": {
        "co2": {"value": 112000,
                "uncertainty": 0
                },
        "ch4": {"value": 200,
                "uncertainty": 0
                },
        "n2o": {"value": 1,
                "uncertainty": 0
                }
    },
    "Biogasoline": {
        "co2": {"value": 70800,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
    "Biodiesels": {
        "co2": {"value": 70800,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
        "Other_Liquid_Biofuels": {
        "co2": {"value": 79600,
                "uncertainty": 0
                },
        "ch4": {"value": 10,
                "uncertainty": 0
                },
        "n2o": {"value": 0.6,
                "uncertainty": 0
                }
    },
        "Landfill_Gas": {
        "co2": {"value": 54600,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
        "Sludge_Gas": {
        "co2": {"value": 54600,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
        "Other_Biogas": {
        "co2": {"value": 54600,
                "uncertainty": 0
                },
        "ch4": {"value": 5,
                "uncertainty": 0
                },
        "n2o": {"value": 0.1,
                "uncertainty": 0
                }
    },
        "Other_non_Fossil_Fuels_Municipal_Waste": {
        "co2": {"value": 100000,
                "uncertainty": 0
                },
        "ch4": {"value": 300,
                "uncertainty": 0
                },
        "n2o": {"value": 4,
                "uncertainty": 0
                }
    },
}