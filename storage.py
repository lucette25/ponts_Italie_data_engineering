import getData
import sqlalchemy

data=getData.ponts_df
engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:Lucette@localhost:5432/ponts')
data.to_sql('ponts_table', engine)

print(data)