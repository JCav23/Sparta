-- Loading seperate files into partitioned table
LOAD DATA INPATH '/user/hadoop/spartans-london.csv'
OVERWRITE INTO TABLE academy.spartitions PARTITION (city='london');

LOAD DATA INPATH '/user/hadoop/spartans-bham.csv'
OVERWRITE INTO TABLE academy.spartitions PARTITION (city='bham');

SELECT * FROM academy.spartitions;

-- Loading single file using Dyanmic Partioning
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;

-- Setting up placeholder table
DROP TABLE IF EXISTS academy.spartitions_placeholder;
CREATE TABLE academy.spartitions_placeholder (
  spartan_id INT,
  client_name STRING,
  placement_start DATE,
  city STRING
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';

-- Loading file into placeholder table
LOAD DATA INPATH '/user/hadoop/spartans-all.csv'
OVERWRITE INTO TABLE academy.spartitions_placeholder;

SELECT * FROM academy.spartitions_placeholder;

-- Insert Data from Placeholder table into Partioned Table using Dynamic Partitioning
INSERT INTO TABLE academy.spartitions PARTITION (city)
SELECT spartan_id, client_name, placement_start, city FROM academy.spartitions_placeholder;

SELECT * FROM academy.spartitions;
