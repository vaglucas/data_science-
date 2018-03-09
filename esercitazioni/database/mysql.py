
import pymysql
from pymongo import MongoClient

conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="root",db="gestor_rural")
cur = conn.cursor()
query = "SELECT * FROM auth_user"
n_row = cur.execute(query=query)
results = list(cur.fetchall())
num_fields = len(cur.description)
field_names = [i[0] for i in cur.description]
j = []
for result in results:
    j.append(dict(list(zip(field_names, result))))
conn.commit()


"""
MongoDB
import table for mysql to mongoDB
"""

client1 = MongoClient()
db = client1["dsdb"]
auth_user = db["auth_user"]

inserts = auth_user.insert_many(j)
inserts.inserted_ids

everyone = auth_user.find()
print("============================================")
print("                *****                       ")
print("                *****                       ")
print(everyone)
print("                *****                       ")
print("                *****                       ")
print("============================================")
