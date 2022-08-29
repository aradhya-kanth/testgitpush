import pymongo
client = pymongo.MongoClient("mongodb+srv://new:Mongodb@cluster0.bz1hqcf.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "Aradhya",
    "email": "aradhyakanth@gmail.com",
    "surname": "kanth"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
