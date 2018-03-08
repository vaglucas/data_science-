from pymongo import MongoClient

client1 = MongoClient()

#client1 = mongo.MongoClient("localhost",27017)

#client3 = mongo.MongoClient("mongodb://localhost:27017/")


db = client1["dsdb"]
people = db["people"]

#person1 = {"empname":"John Smith","dob":"1957-12-24"}
#print(person1)
#person_id1 = people.insert_one(person1).inserted_id
#print(person1)

#person2 = {"_id":"XVT162", "empname":"Jone Doe","dob":"1964-05-16"}
#person_id2 = people.insert_one(person2).inserted_id

#print(person2)
#persons =[{"empname":"Abe lincoln","dob":"1809-02-12"},
          #{"empname":"Anon I. Muss"}]
#result = people.insert_many(persons)
#result.inserted_ids
#print(persons)

people.update_one

everyone = people.find({"empname":"Vagner Lucas"})
print(everyone[0]["_id"])
print(everyone[0]["empname"])
#db.people.update({"_id":everyone[0]["_id"]},{"empname":"Vagner Lucas Gomes","dob":"1991-03-06"})

print(people.count())
print((people.find_one({"empname":"Vagner lucas"})))
