#Apache Pig

## Data Types

### Numeric
* int = 32-bit integer -- 10
* long = 64-bit integer -- 10L
* float = 32-bit floating point -- 10.5F
* double = 64-bit floating point -- 10.5
### Text
* chararray = Character array string -- hello world
### Date
* Datetime = Date/time stamp -- 1970-01-01T00:00:00.000+00:00
### Binary
* bytearray = Blob, inherited from Java DataByteArray class. Can't be specified in PigLatin, but is the default for loading data if the type is not specified.
### Complex
* Tuple = Ordered collection -- (1, 2, 3)
* Bag = Unordered collection of tuples -- {(1, 2), (3, 4)}
* Map = Maps chararrays (keys) to data elements (values) -- [key # value]

## Commands BY 

| Keyword | Description	| Example |
| - | - | - |
| DUMP | Prints results to the screen. | DUMP var |
| LIMIT | Restricts number of records. | LIMIT var 10 |
| GROUP BY | Groups data on a column. | GROUP var BY col |
| ORDER BY | Orders the data by a column. | ORDER var BY col [ASC / DESC] |
| FILTER | Filters data. | FILTER var BY col > 10 |
| FOREACH | Applies transformation on each record. | FOREACH var GENERATE col1, col2, col3 * 10 |
| JOIN | Joins two variables together. | JOIN var1 BY col, var2 BY col; |
| STORE | Stores results of MapReduce job. | STORE var INTO 'name' |
| DESCRIBE | Shows schema of variable. | DESCRIBE var |
| EXPLAIN | Shows execution plan. | EXPLAIN var |
| ILLUSTRATE | Shows step-by-step breakdown of script. | ILLUSTRATE var |

### DESCRIBE
- Used to view the schema of a relation, can view outer relations as well as those defined in a nested FOREACH statement

### EXPLAIN
- Used to review the logical, physical and map reduce execution plans which are used to compute the specified relationship 

### ILLUSTRATE
- Used to review how some data is transformed through a sequence of Pig Latin Statements. Allows to test your programs on small datasets and get faster turnaround times.

ppl_raw = LOAD 'people.csv' USING PigStorage(',') AS (BusinessEntityID: int, PersonType: chararray, NameStyle: int, Title: chararray, FirstName: chararray, MiddleName: chararray, LastName: chararray);
ppl_data = FILTER ppl_raw BY BusinessEntityID IS NOT NULL;
emp = FILTER ppl_data BY PersonType == 'EM' OR PersonType == 'SP';

names = FOREACH emp GENERATE CONCAT(SUBSTRING(FirstName,0,1), '. ', (MiddleName == 'NULL' ? '' : CONCAT(SUBSTRING(MiddleName,0,1), '. ')), LastName) AS Name;
STORE names INTO EmployeeNames