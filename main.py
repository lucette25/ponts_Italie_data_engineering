# -*- coding: utf-8 -*-
#from storage import toDataBase
from flask import Flask,jsonify,request
import psycopg2,os

#toDataBase()

app = Flask(__name__)


DATABASE_URL = 'postgres://grlfqghirgpfqm:243ca0d2a4c5dfdab173f97889b41078abfb998568b96f57f427fea8f04b2486@ec2-52-5-110-35.compute-1.amazonaws.com:5432/d95i7uhi4ll0fb'

# create a new database connection by calling the connect() function
con = psycopg2.connect(DATABASE_URL)
print(con)





@app.route("/", methods=['GET'])



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


port2 = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=port2)

