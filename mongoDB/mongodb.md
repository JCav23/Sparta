# MongoDB
* USE <database name>
* show collections
* db.createCollection(<collection name>)
* db.<collection name>.InsertOne(<keypair>)
* ObjectID = comparable to a primary key in a relational db, unique identifier for the object
* db.<collection name>.updateOne({<object>}, {$set: <object>})
* updateOne will only update the first instance of an object
* most operators in mongoDB will use dollar sign ($)
* db.<collection name>.updateMany({<filter>}, {<operation>}) 
* if we wish to update all in the collection we leave the filter blank

## Examples of Document Model
* Embedding: document with all the documents embeded into the single document
* Referencing: normalized document model with each object broken down into single objects while conected by objectID which can be comparable to foreign key but without all of the referential constraints of relational dbs 

## Delete Method
* db.<collection name>.deleteOne/deleteMany({}
