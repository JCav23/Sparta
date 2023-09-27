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
