# Big Data

## What is it?

Big data can be defined as extraordinarily large and diverse data sets consisting of structured, semi-structured and unstructured data that continue to grow exponentially over time. 
They contain greater variety, arrive in increasing volumes and with more velocity. This are three of what are known as big V's of Big Data. They are so huge and complex that traditional data management systems cannot store, process or analyse them. 
However they can be harnessed to address business problems that wouldnt have been able to have been solved otherwise.

### Examples

To give an idea of the various instances working with big data can provide valuable instances, here are a few examples and is by no means an exhaustive list.

* Tracking consumer behaviour and shopping habits to the product highly personalized product recommendations tailored to individual customers
* Monitoring payment patterns and transaction history analysis can lead to real time fraud detection
* Analysis of geospatial data and satellite imagery to visualize, monitor and predict social/environmental impacts of supply chain operations 

## Big V's of big Data

With the original three first defined in 2001, there are now as many as 6 big V's of Big data depending on who you ask.

### Original 3
* __V__olume 
	- This describes the amount of data that is available for collection and produced from a variety of sources and devices on a continuous basis. This could be such things as clickstreams on a website, data feeds from twitter, or sensor enabled equipment. Depending on the organization this could range from tens of terrabytes to hundreds of petabytes.
* __V__elocity 
	- This is the rate at which the data is recieved and acted on (potentially). Generally the highest velocity is streamed directly into memory and as often modern systems produce data in real or near-to real time, it must also be accessed, processed and analysed at the same rate to have a meaningful impact.
* __V__ariety
	- This refers to the many different types of data that are now available. While traditionally data types were oragnized into structured relational databases, progress in technology has given rise to new un/semi-structured data sets. Text, audio and video may all require additional processing to derive meaning and support metadata.
### Additional V's
* __V__eracity
	- Big data can be messy, noisy and full of errors. which can make it difficult to control the quality/accuracy of the data. Small datasets may only provide an incomplete picture, while larger datasets can be unwieldy and confusing. The higher the veracity the more reliable the data.
* __V__ariability
	- As the meaning behind the data can change as rapidly as the data is being produced. This can lead to inconsistencies over time. This is not only changes in context/interpretation of the data but also the methods of collection based on companies requirements on what to capture and analyse.
* __V__alue
	- Not everything will have meaning, and with such vast amounts of data it is important to know what provides value. Only once this is determined can the valuable data be effectively analyzed to yield effective insights that can help drive decision-making.

## How it works

While big data can help derive valuable insights that will drive key buisness decisions. There are 3 key actions that are:
* __Integration__
	- As previously stated, numerous terrabytes or even petabytes of raw data can be generated, across various different sources. Traditional ETL pipelines generally arent up to the task so you need to be able to access, process and transform the data into a format that can then be used by the business.
* __Management__
	- Big data requires storage whether that be cloud based, on premises or both. You can store your data on any form you want and bring in your desired processing requirements and neccesary process engines to those data sets on an on-demand basis. Cloud storage solutions are becoming increasingly popular.
* __Analysis__ 
	- The final step is analyzing and acting on big data otherwise the investment wont be worth it. It is critical to communicate and share the data in a way that everyone can understand such as data visualization methods such as charts, graphs and dashboards.

## Hadoop

Apache Hadoop is a library of open source software that facilitates the use of a network of distributed systems. Developed in 2005 and initially released in April 2006, Haddop provides a framework for distrubuted storage and processing of big data.
This is achieved using what is known as a MapReduce Model, which is a program composed of a "Map" procedure and a "Reduce" method. The "map" performs filtering and sorting while the "Reduce" performs summary operation. 

### Core Components

* Hadoop HDFS
	- Hadoop Distributed File System is designed to run on commodity hardware. It provides a high throughput access to application data and is suitable for applications that have large data sets.
* Hadoop YARN
	- Yet Another Resource Negotiator - The fundamental idea of YARN is to spliting up the functionalites of resource management and job scheduling/monitoring into seperate daemons. 
* Hadoop MapReduce
	- MapReduce is a programming paradigm that enables massive scalability across hundreds of thousands of servers in a Hadoop cluster. As the processing component, MapReduce is the heart of Apache Hadoop.
* Hadoop Hive
	- A data warehouse software built on top of Apache Hadoop for providing data query and analysis. 
* Hadoop Pig
	- A high level platform for creating programs that run on Apace Hadoop using a platform specific language called Pig Latin.

