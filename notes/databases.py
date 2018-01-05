"""
Databases:

Data Persistence
- files (text, JSON)

Databases
- binary format
- easier to search
- large scale data
- SQL = standard query language (ex MySQL, SQLite, etc)

SQLite
- no server
- good for small data
- built into python
- Tables -> Records -> Fields/Attributes
- Classes -> Objects -> Instance Variables
- rows = records, columns = fields
- number (Integer), String (varchar), blob (binary)
"""

import sqlite3

def main():

    connection = sqlite3.connect('Population.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE uspopulation (name, Text)')
    cursor.execute('ALTER TABLE uspopulation ADD COLUMN (population, Integer)')
    cursor.execute('INSERT INTO uspopulation (name, population) VALUES ("Binghamton", 40000)'
    cursor.execute('SELECT name FROM uspopulation WHERE name="Binghamton"')

    connection.commit()
    cursor.close()