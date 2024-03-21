import sqlite3
from typing import List, Any
from sqlalchemy import create_engine, Column, Integer, String, Unicode, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

db_file = 'testing_database.db'
engine = create_engine(f'sqlite:///{db_file}', echo=True)
# Base class for declarative class definitions

class SQLiteManager:
    def __init__(self, db_file: str):
        self.connection = sqlite3.connect(db_file)
        print('Connected to DB')

    def execute(self, query: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as error:
            print(f"Error connecting to SQLite: {error}")
            raise
    
   


