# -*- coding: utf-8 -*-
from storage import toDataBase
from flask import Flask,jsonify,request
import psycopg2

toDataBase()

DATABASE_URL = 'postgres://ywczmgutsqcrov:8f83bb47c1a0d3f90db7e004786505cdde184c1ffc95ac855bdc7a4b11d531a7@ec2-3-217-113-25.compute-1.amazonaws.com:5432/d52673l1t0ik3a'

# create a new database connection by calling the connect() function
con = psycopg2.connect(DATABASE_URL)
print(con)



app = Flask(__name__)

@app.route("/")



def getAllBridge():

        #  create a new cursor
        cur = con.cursor()

        # execute an SQL statement to get the HerokuPostgres database version
        print('PostgreSQL database version:')
        cur.execute('SELECT * FROM ponts_table')


        # display the PostgreSQL database server version
        #data = cur.fetchall()
        #return  jsonify(data)
        data_json = []
        header = [i[0] for i in cur.description]
        data = cur.fetchall()
        for i in data:
            data_json.append(dict(zip(header, i)))
        return jsonify(data_json)

        # close the communication with the HerokuPostgres
        cur.close()




@app.route('/city/<city_name>', methods = ['GET'])
def getByCity(city_name):
        city_name = request.view_args['city_name']

    #  create a new cursor
        cur = con.cursor()

        # execute an SQL statement to get the HerokuPostgres database version
        print('PostgreSQL database version:')


        cur.execute(f"SELECT * FROM ponts_table where localisation LIKE '{city_name}%'")

        # display the PostgreSQL database server version
        #data = cur.fetchall()
        #return  jsonify(data)
        data_json = []
        header = [i[0] for i in cur.description]
        data = cur.fetchall()
        for i in data:
            data_json.append(dict(zip(header, i)))
        return jsonify(data_json)

        # close the communication with the HerokuPostgres
        cur.close()



if __name__ == "__main__":
    app.run(debug=True)