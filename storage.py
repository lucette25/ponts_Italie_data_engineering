from getData import getData
import sqlalchemy


def toDataBase():
    data = getData()
    engine = sqlalchemy.create_engine(
        'postgresql+psycopg2://grlfqghirgpfqm:243ca0d2a4c5dfdab173f97889b41078abfb998568b96f57f427fea8f04b2486@ec2-52-5-110-35.compute-1.amazonaws.com:5432/d95i7uhi4ll0fb')
    data.to_sql('ponts_table', engine, if_exists='replace')


toDataBase()

