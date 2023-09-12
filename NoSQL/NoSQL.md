# NoSQL 
* Stands for Not Only SQL
* Semi-Structure or unstructured with only very loose if any relationships between data 
	* This is opposed to SQL which has very stringent requirements with regard to structure 
* Doesn't require a schema to be sent up before setting up the database

## Types of NoSQL
* Key-Value Store
* Document Store (Example: MongoDB)
	* Mongo specifically will Store information in BSON (Binary JavaScript Object Notation) 
* Column Family
	* Store data in columns rather than rows similar to key value pairs with Name, Value and Timestamp
	* Wont store Null Values
* Graph Databases
	* Made up of connected nodes (or Vertices) and represents relationships

|  | NoSQL | SQL |
| - | - | - | 
| Type | Non-Relational, distributed | Relational database management system (RDBMS)|
| Language | Various | Structured Query Language |
| Schema Design | Dynamic Schema, unstructured data | Uses Table-like schema |
| Scalability | Horizontally scalable |Vertically Scalable | 
| Structure | VariousL key-value, document, columnar, graph | Database as collection of tables |

# MongoDB

### Replica set
* Replica sets is a group of mongod processes that maintain the same data set
* They provide redundancy and high availability

### Sharding
* Sharding is a method for distributing data across multiple machines. MongoDB uses sharding to support deployments with very large data sets adn high throughput operations
* Made up of Replica Sets
* Each Sharded cluster must have its own set of configuration servers
* Distributes the Read and Write Requests across the servers#

### Use Cases

* Bosch & Toyota use MongoDB real time analytics of IoT data for things such as autonomous factories or smart vehicles
* Verizon, Comcast use for data streaming high volume high traffic situations

