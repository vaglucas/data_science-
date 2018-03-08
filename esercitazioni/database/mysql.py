
import pymysql
conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="root",db="gestor_rural")
cur = conn.cursor()


query = "SELECT * FROM auth_user"

n_row = cur.execute(query=query)

results = list(cur.fetchall())

print(results)

conn.commit()
