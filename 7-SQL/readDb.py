import sqlite3
from pathlib import Path
import pandas as pd

sql_dir = Path(__file__).resolve().parent
db_path = sql_dir / 'people.sqlite'

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

#query="SELECT * FROM kings"
query = "DELETE FROM kings WHERE name='Kacper'"

cursor.execute(query)
connection.commit()
#df = pd.read_sql(query, connection)


cursor.close()
connection.close()

