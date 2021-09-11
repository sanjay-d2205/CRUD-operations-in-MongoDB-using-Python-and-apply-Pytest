import pymongo
import pytest
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb"]
mycol = mydb["customers"]

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)



def database(): #Check if database exist
    dblist = myclient.list_database_names()
    if "mydb" in dblist:
        print("The database exists.")
        return "mydb"

def Collection():#check if collection exixt
    collist = mydb.list_collection_names()
    if "customers" in collist:
        print("The collection exists.")
        return "customers"

def select(): #selecting 1st document from collection
  x= mycol.find_one({},{ "_id": 0, "name": 1, "address": 1 })
  return x

def selectSpecific(): #selecting a specific  document from collection
  myquery = { "address": "Park Lane 38" }
  mydoc = mycol.find(myquery)

  for x in mydoc:
    return x

def deleteCount(): #deleting a specific document from record
    myquery = {"address": "Mountain 21"}
    x = mycol.delete_one(myquery)
    print(x)
    return x.deleted_count


#TestCase

def test3():
    assert database()=="mydb"
def test4():
    assert Collection()=="customers"

def test():
  assert select()=={'name': 'Amy', 'address': 'Apple st 652'}

def test1():
  res={'_id': ObjectId('6135fcafd17f44b048f0d44b'), 'name': 'Ben', 'address': 'Park Lane 38'}
  assert selectSpecific()==  res

def test2():
  assert deleteCount()==0

