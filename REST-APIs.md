# REST APIs

## Tools Used

- Web developer tools
- Curl
- Postman


## Section One - **HTTP**

HTTP: Hypertext Transfer Protocol is an application layer in the Internet protocol suite.

It uses a request/response style
<br>
<br>
*Example:*
User enters URL on a web browser, the browser then creates HTTP request and uses network to send it to the server.
Server then creates HTTP respons and uses the network to send it back to the browser.
The browser will then recieve and interpret the content within that response as a graphical display to the user
This process is also known as rendering.

***HTTP is a stateless protocol.*** 
Once request/response cycle has been completed the connection can be severed. 
HTTP can also function on persistent conections but generally they are not required.

#### Important HTTP Request Methods

- GET
**The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.**
- POST
**The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.**
- PUT
**The PUT method replaces all current representations of the target resource with the request payload.**
- DELETE
**The DELETE method establishes a tunnel to the server identified by the target resource**
- PATCH
**The PATCH method applies partial modifications to a resource.**

#### Status Codes

- **1XX** - Informational (e.g. 100 = Continue)
- **2XX** - Successful (e.g. 200 = OK)
- **3XX** - Redirection (e.g. 301 = Moved Permanently)
- **4XX** - Client Error (e.g. 404 = Not Found)
- **5XX** - Server Error (e.g. 500 = Internal Server Error)

http.cat: helpful resource to reference HTTP Status codes

HTTPS is also widely used in preference of HTTP as the communication between the local machine and server is encrypted.



## Section Two - **JSON**

JSON (***JavaScript Object Notation***) is an open standard file format and data interchange format that uses human-readable text to store and transmit data.

***JSON Example***
<br>
<br>
**{**
<br>
	"exchange-rate":12.07,	(**JSON treats whole numbers and decimals the same rather than int & float**)
	<br>
	"age":57,
	<br>
	- "charge": -1.6e-19,  (**JSON accepts exponential notation**)
	<br>
	- "firstName":"Jack",  (**JSON accepts Strings**)
	<br>
	"empty-string":"",  (**JSON accepts empty Strings**)
	<br>
	- "isStudent": true,  (**JSON accepts Boolean values**)
	<br>
	- "phoneNumbers":["12345","34567","98765"], (**JSON accepts Arrays**)
	<br>
	- "address": **{**   (**JSON accepts other JSON Objects**) <br>
		"street":"123 High Street",
		<br>
		"city":"London",
		<br>
		"postcode":"AB12 3FE"
		<br>
	**}**
	<br>
	"car":null (**JSON accepts null values**)
	<br>
**}**









