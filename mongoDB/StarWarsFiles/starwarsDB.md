# Star Wars
### May the Force Be With You

## Importing the files
first the data for the characters was imported into mongoDB using Git Bash
for i in *.json
do
mongoimport 
--db starwars
--collection characters
--jsonArray
--file $i
done

## Data Cleaning
