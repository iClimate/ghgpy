from sqlalchemy import create_engine
import pandas as pd
import os

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

