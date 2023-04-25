from sqlalchemy import func
from utils import get_engine
from models import Eptica,Telephonie
from sqlalchemy.orm import sessionmaker
import pandas as pd

engine = get_engine()
Session = sessionmaker(bind=engine)
session = Session()

# Get the number of rows in the MyTable table
num_rows = session.query(func.count(Telephonie.id)).scalar()

print(f'The number of rows in the Telephonie table is: {num_rows}')

# Get the data into a dataframe
with engine.begin() as conn:
    df = pd.read_sql(session.query(Eptica).statement, conn)

print(df.head())