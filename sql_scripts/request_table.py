from sqlalchemy import func,  text
from sql_scripts.utils import get_engine, get_engine_master
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

# engine = get_engine_master()
# Session = sessionmaker(bind=engine)
# session = Session()

# # Create a new user with login and reader permission
# user_name = 'apprenant'
# password = 'Simplon@CACF59'

# create_user_sql = text(f"""
#     CREATE LOGIN [{user_name}] WITH PASSWORD = '{password}';
#     -- CREATE USER [{user_name}] FOR LOGIN [{user_name}];
#     -- ALTER ROLE db_datareader ADD MEMBER [{user_name}];
# """)

# with engine.begin() as connection:
#     connection.execute(create_user_sql)



# from sqlalchemy import create_engine, text

# # Connect to the database
# engine = get_engine()

# # Specify the username for which you want to check the roles
# username = 'apprenant'

# # Define the SQL query to retrieve user roles
# query = text(f"""
#     USE contacts;
#     GRANT SELECT ON SCHEMA::dbo TO {username};
# """)

# # Execute the query
# with engine.connect() as connection:
#     connection.execute(query)
