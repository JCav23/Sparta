import pymongo

client = pymongo.MongoClient()
db = client['testdb']

actual = db.test_numbers.find({'Three': {'type': 'int'}})
for result in actual:
    print(result)