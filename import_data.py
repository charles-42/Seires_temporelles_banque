

import pandas as pd
from utils import get_engine
from models import Eptica
from sqlalchemy.orm import sessionmaker
engine = get_engine()
Session = sessionmaker(bind=engine)
session = Session()

# Read CSV file into a pandas DataFrame
df = pd.read_csv('data/eptica_clean.csv')

# Clean dataframe
df.columns = ["date", "entite", "instance", "nb_recus"]
df = df[df["nb_recus"].notnull() ]

# Delete former imported date
session.query(Eptica).delete()
session.commit()

# Insert the data into the table
for index,row in df.iterrows():
    row_dict = row.to_dict()
    try:
        session.add(Eptica(**row_dict))
    except:
        print(row_dict)
session.commit()


# Read CSV file into a pandas DataFrame
df = pd.read_csv('data/telephonie_clean.csv')

# Clean dataframe
df.columns = ["date_appel", "entite", "famille", "nombre_entrants_corrige"]
df = df[df["nombre_entrants_corrige"].notnull() ]
df['nombre_entrants_corrige'] = df['nombre_entrants_corrige'].astype(float)
print(df.info())


# Delete former imported date
session.query(Telephonie).delete()
session.commit()

# Insert the data into the table
for index,row in df.iterrows():
    row_dict = row.to_dict()
    try:
        session.add(Telephonie(**row_dict))
    except:
        print(row_dict)
session.commit()


