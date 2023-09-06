# Numpy, Pandas & DataFrames

### Contents

- [NumPy](#numpy)
- [Pandas](#pandas)

## Numpy 

### Contents

- [NumPy Arrays](#numpy-arrays-ndarrays)
- [Multidimensional Arrays](#multidimensional-arrays-2-and-3-dimensional)
- [Accessing Arrays](#how-to-access-values-in-ndarrays)
- [Statistical Analysis](#statistical-functions-available-for-ndarrays)


## NumPy Arrays (ndarrays)

### How are they different to Python lists?

Lists in Python are slow to process, and NumPy arrays aim to provide an object that is processed up to x50 times faster than python lists. This is achieved by being stored in one continuous place in memory so can process, access and manipulate them very efficiently. This is called locality of reference

### Multidimensional arrays (2 and 3 dimensional)
A dimension in ndarrays is a level of array depth for nested arrays
- 0-D arrays or Scalars are the elements in an array
- 1-D arrays are known as uni-dimensional where each of its elements are Scalars
- 2-D arrays is an array where each element is a 1-D array and are often used to represent a matrix
	- NumPy has a sub-module dedicated to matrix operations called numpy.mat
- 3-D array takes this a step further with each element being a 2-D array.
	- You can then access the values using an integer for each dimension within the array.
- Multidimensional arrays can have any number of dimensions, below are some commonly used commands using multidimensional arrays
	- ndim - returns the the integer of how many dimensions the array have
	- ndmin - defines the number of dimension using the ndmin array


### How to access values in ndarrays
- 2-D arrays can be accessed using comma seperated integers representing dimension & index of the element
	- Accessing 2-D arrays can be thought of like tables with rows and columns where the dimension represents the row and the index represents the column
- 3-D arrays take this a step further and use 3 values to access the array. With each value representing the next dimension of the array

Along with accessing the single elements using indexing you may also indexing using slices and boolean indexing. You may also use what is known as Fancy Indexing using an array of indicies to select specific elements

### Statistical functions available for ndarrays
- **Mean** - np.mean(arr)
- **Variance** - np.var(arr)
- **Standard Deviation** - np.std(arr)
- **Min/Max** - np.min(arr) / np.max(arr)
- **Sum** - np.sum(arr)
- **Product** - np.prod(arr)
- **Correlation Coefficient** np.corrcoef(arr1, arr2)
- **Linear Algebra** - np.linalg.inv(arr) / np.linalg.eig(arr)


# Pandas

### Contents

- [What is it?](#what-is-it)
- [Series](#series)
- [Empty Creation](#empty-creation)
- [Series Creation](#series-creation)
- [Dictionary Creation](#dictionary-creation)
- [Series Methods](#methods-for-accessing-values-within-series)
- [DataFrames](#dataframes)
- [DataFrame Sources](#sources---lists-dictionaries-csv-json)
- [Indexing](#adding--changing-index-values)
- [Missing Values](#finding-missing-values)
- [Replacing Null](#replacing-missing-values)
- [Drop](#deleting-null-value-rowscolumns)
- [Duplicates](#finding--deleting-duplicates)
- [Selecting Data](#selecting-data-iloc--loc-functions)

### What is it?

Pandas is simply a library used for working with data sets. It has various functions used for analyzing, cleaning, exploring and manipulating data.

It allows us to clean messy datasets, making them readable and relevant, which is really important in data science. this includes deleting rows that are not relevant, contain wrong values, like empty or NULL values. 

<hr>

### Series

A Panda Series is like a column in a table, a one dimensional array holding data of any type. 

Series can be created using various methods such as creating series from lists, dictionaries, arrays or even generating empty series.

If nothing else is specified during creation the values are labeled with their index numbers which can then be used to access them. 

*a = [1, 7, 2]*
<br>
*myvar = pd.Series(a, index = ["x", "y", "z"])*

<hr>


### Empty Creation 

**Input**
<br>
*empty_series = pd.Series()*
<br>
*print(empty_series)*


**Output**
<br>
*Series([], dtype:object)*

<hr>

### Series Creation 

**Input**
<br>
<!-- np.linspace is a numpy method generating list of evenly spaced integers-->
*numbers = np.linspace(0, 4, 5)*
<br>
*series = pd.Series(numbers)*

**Output**
<br>
| index | number |
| - | - |
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |

Following this you can then join arrays and series using the .append and .concat methods respectively if you wish. 

<hr>

### Dictionary Creation

**Input**
<br>
*nme = ['Jack', 'Cami', 'Amy', 'Callum', 'Nikole']*
<br>
*age = [ 29, 30, 28, 28, 25]*
<br>
*deg = ['Chemistry', 'Marine Biology', 'History', 'Marine Biology', 'Psychology']*

*dict = {'name': nme, 'degree': deg, 'age': age}*

*series_dict = pd.Series(dict, index=['degree', 'age', 'name'])*

**Output**
<br>
|  |  |
| - | - |
| **degree**| ['Chemistry', 'Marine Biology', 'History', 'Marine Biology', 'Psychology'] |
| **age** | [ 29, 30, 28, 28, 25] | 
| **name** | [Jack, Cami, Amy, Callum, Nikole] |

When generating series from dictionaries it is important to note that when calling the index labels for the series you must use the pre-existing keys from the dictionary otherwise the series will return **NaN** (More about NaN values [here](#finding-missing-values)]). 

When you wish to name the index's it is more appropriate to generate the series from a list.

<hr>

### List Creation 

**Input**
<br>
*ser_list = pd.Series(deg, index=nme)*

**Output**
<br>
|  |  |
| - | - |
| **Jack**| Chemistry |
| **Cami** | Marine Biology | 
| **Amy** | History |
| **Callum** | Marine Biology |
| **Nikole** | Psychology |

### Methods for accessing Values within Series

Once you have the Series generated and you wish to access the values, you then have two options to access the values, using either the index[] the same way you would usually within python referencing the position. Alternatively you can use the use the index label specified. 

<hr>

### DataFrames

A Pandas DataFrame is a 2D data structure, like a 2 dimensional array, or a table with rows and columns. If we think of a Series as a column within a table, a Dataframe would be the whole table.

<hr>

### Sources - Lists, Dictionaries, CSV, JSON

As with Series, DataFrames can also parse Lists within their function and automatically index the rows and columns for us. If we wish to allocate the index ourselves we can also do this by specifying the labels. 

Pandas is clever enough that if there are lists nested within each other it will automatically generate the columns which we can then define. 

Similarly when parsing in dictionaries, the generated DataFrame will take in the values as lists, parsing the keys into the columns and the lists into the rows. 

Pandas is also capabale of parsing in pre-existing datasets in the forms of CSV and JSON files using the **.READ_CSV()** and **.READ_JSON()** commands respectively. 

Once the DataFrames have been created, the data can then be manipulated in various way depending on requirements. 

<hr>

### Adding / Changing Index Values

The index can be thought of as a unique name used to access the rows within a DataFrame. As such it has various methods associated with finding and even changing the index. 

- df.index - checks the current index
	- **EXAMPLE:** RangeIndex (start=0, stop=7, step=1)
- df.loc[index] - calls a specific row within the DataFrame
- df.set_index('new_index' inplace=True) - Changes the index to our specified label

<hr>

### Finding Missing Values

Mising values can exist within a DataFrame and it is important to know how to deal with them appropriately. Firstly they can be decribed in such was as None, which represents a missing value or NaN (Not a Number) which is a special floating-point value and cannot be converted to any other type than float.

We can check for these missing values using the different **ISNULL** methods such as...

- *df.isnull().values.any()* - Checks for the occurence of missing values
- *df.isnull().sum()* - Counts number of missing values within a column
- *df.isnull().sum().sum() - Counts the total number of missing values in all columns

<hr>

### Replacing Missing Values 

When we encounter missing values we are able to fill them with various methods including:

- **df.ffill()** - ffill stands for forward fill and will propagate last valid observation forward
- **df.bfill()** - Inversely back fill will backward fill the missing values in the dataframe
	- both ffill() and bfill() use the axis parameter to specify either rows (can be denoted as 0) or columns (can be denoted as 1)
- **df.interpolate()** - replaces the missing values based on a specified method
- **df.replace()** - replaces every instance of the specified value with chosen 'filler' value

<hr>

### Deleting NUll Value Rows/Columns 

If we wish we can delete the rows containing the Null values using the **DROPNA** method. This will remove all rows that contains Null values and either return a new DataFrame object, or if the ***inplace*** parameter is set to **True** will simply remove the values from the original DataFrame instead.

<hr>

### Finding & Deleting Duplicates

Often in data rather than Null values we can have duplicate values within a dataset, this could be down to error or coincidence but either way we need to know how to identify and process them. 

The easist way to do this is using the duplicated() and drop_duplicates() methods.

- **duplicated()**: Identifies duplicated rows and returns a boolean Series of True/False values
- **drop_duplicates()**: Removes the duplicate values from the DataFrame

<hr>

### Selecting Data (iLoc / Loc Functions)

Mentioned briefly in a previous section, two important attributes for accessing data are Loc & iLoc
- Loc accesses groups of rows and columns using the specified Label for desired values
- iLoc accesses using integer indexing rather than the Label index used by Loc