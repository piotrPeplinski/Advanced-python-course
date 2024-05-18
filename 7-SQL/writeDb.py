import pandas as pd
import sqlite3
from pathlib import Path
import os

sql_dir = Path(__file__).resolve().parent
db_path = sql_dir / 'people.sqlite'

df = pd.DataFrame({
    'Name':['Jurek','Melchior','Baltazar'],
    'Age': [30,25,30]
})

connection = sqlite3.connect('people.sqlite')

df.to_sql('kings',connection,if_exists='append', index=False)

connection.close()

base_dir = Path(__file__).resolve().parent.parent



