from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy  import create_engine
from json import dumps
from flask_jsonpify import jsonpify
from pymongo import MongoClient

from flask import render_template
#init connection
#"C:\Program Files\MongoDB\Server\3.6\bin\mongod.exe"
client1 = MongoClient()

db = client1["dsdb"]
people = db["people"]
app = Flask(__name__)
api = Api(app)

class Employees_Name(Resource):

    def get(self, name_emp):
        print(name_emp)
        query = people.find({"empname":name_emp})
        results = list(query)
        result = {'data':[dict(zip(tuple(results,i))) for i in results]}
        return jsonpify(result)

class Hello(Resource):
    def get(self,name_emp):
        query = people.find({"empname":name_emp})
        results = list(query)
        result = {'data':[dict(zip(tuple(results,i))) for i in results]}
        return render_template("hello.html",name=results)

#api.add_resource(Employees, '/employees') # Route_1
#api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<name_emp>') # Route_3
api.add_resource(Hello,'/hello/<name_emp>')

if __name__ == '__main__':
     app.run(port=8080)
