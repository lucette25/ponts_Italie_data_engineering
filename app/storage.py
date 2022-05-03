from getData import getData
import sqlalchemy


def toDataBase():
    data = getData()
    engine = sqlalchemy.create_engine(
        'postgresql+psycopg2://ywczmgutsqcrov:8f83bb47c1a0d3f90db7e004786505cdde184c1ffc95ac855bdc7a4b11d531a7@ec2-3-217-113-25.compute-1.amazonaws.com:5432/d52673l1t0ik3a')
    data.to_sql('ponts_table', engine, if_exists='replace')




