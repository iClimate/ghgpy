"""
iClimate - ghgpy

Data handle

Middleware between app and database

(C) Bui Khac Tu (bkt92)
(C) iClimate
"""

from sqlalchemy import create_engine
import pandas as pd
import os

class FuelDataHandle:
    """
    Data handle for fuel data in ghgpy
    """
    def __init__(self, database):
        self.data = database
    def check_exist(self, fuel):
        return fuel in self.data.keys()
    def get(self, fuel):
        return self.data[fuel]
    
class GHGDataHandle:
    def __init__(self, database, source):
        self.data = database
        if not source in database.keys():
            raise ValueError("Fuel not found in database.")
        self.source = source
    def check_exist(self, key):
        return key in self.data[self.source].keys()
    def get(self, key):
        return self.data[self.source][key]
    
class EFDataHandle:
    def __init__(self, database):
        self.data = database
    def check_exist(self, fuel):
        return fuel in self.data.keys()
    def get(self, fuel):
        return self.data[fuel]

root_path = os.path.dirname(__file__)

class fuels_database:
    """
    The database class for the default and custom data
    
    Default data includes:
        - The NCVs are taken from IPCC 2006 w 2019 refinements
        - Densitys are taken from 
        - EFs taken from IPCC 2006 w 2019 refinements
    """
    def __init__(self, db='xlsx', *args, **kwargs):
        self.db = db
        if db == 'sqlite':
            engine = create_engine(f"sqlite:///{root_path}/database/database.db", echo=True)
        if db == 'mysql':
            pass
        if db == 'xlsx':
            self.data = pd.read_excel(os.path.join(os.path.dirname(__file__), 'database\database.xlsx'))

    def connect(self):
        """
        Connect to database engineer \n
        Not applicable for import data from csv or xlsx
        """
        connection = self.engine.connect()

    def update(self, bylist=False):
        """
        Change default values to new values
        - bylist=False (Default): change only one value
        - bylist=True: input a dictionary of the values
        """
        pass

    def reset_to_default(self):
        """
        Reverse back to the default values
        """

    def datalist(self):
        """
        Print the list of default data on the database.
        """

