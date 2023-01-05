## Data Models and Query Languages

The key question for each layer of data model is: how is it represented in terms of the next-lower layer? E.g.:
1. As an app dev, you look at the real world and mode it to objects or **data structures** and **APIs**. The data structures are often application specific.
2. To store the data structures, you express them in to a general-purpose **data model**.
3. The database software engineers decided on a way of representing the data models in terms of bytes in memory, on disk or on a network.
4. The hardware engineers represent bytes in terms of electrical currents, pulses of light, magnetic fields, etc.

### Relational Model Versus Document Model

The roots of relational databases lie in business data processing,  typically *transaction processing* and *batch processing*. (1060s and 1970s)
- Transaction processing: entering sales or banking transactions, airline reservations, stick keeping in warehouses
- Batch processing: customer invoicing, payroll, reporting

The network model and the hierarchical model (1970s and early 1980s)
Object databases, XML databases... (1980s-2000s)

Relational databases turned out to generalize very well

#### The birth of NoSQL

Driving forces behind *NoSQL* (origin as open source, distributed, nonrelational databases meetup):
1. Scalability. Very large datasets or very high write throughput
2. Free and open source software
3. Specialized query operations
4. Less retrictions and more dynamic and expressive

#### The Object-Relational Mismatch

The impedance mismatch between Object-oriented programming languages and relational tables for data storage.

JSON representation makes the tree sturcture of the data relationship explicit.

Storing geographic information is better to have standarized structured data (regions, industries, etc), we could ask user to choose from a drop-down list or autocompleter. 

The advantage to user ID (instead of free-formed text) is that it has no meaning to humans. There fore, the ID can remain the same even if the information it identifies changes. In this way, we can reduce the duplicated redundant copies to be updated with plain-text format. Removing such duplication is the key idea behind *normalization* in database.
	- As a rule of thumb, if you are duplicating values that could be stored in just one place, the schema is not normalized. (Part III will discuss further with the normalization and denormalization topic)
Easy to join for difference databases:
- In relational databases, it's normal to refer to rows in other tables by ID, because joins are easy
- In document databases, joins are not needed for one-to-many tree structures, and support for joins is often weak. (MongoDB 3.2 now also support joins. It is also supported in [[RethinkDB]])

Even if the initial version of an application fits well in a join-free document model, data has a tendency of becoming more interconnected as features are added to applications.
Resume example:
- Organizations and schools as entities.
	- Initial description, organization and school names are just strings
	- Changing: organization and school can also have their own attributes like homepage, logo, description, etc. Then they are easier to be stored as entities.
![[Pasted image 20230104105937.png]]
##### Are Document databases repeating history?

- The network model
	- It was standarized by a committee called the Conference on Data System Languages (CODASYL), it is also known as the CODASYL model.
	- It is a generalization of the hierarchical model, which allows many-to-one and many-to-many relationships.
	- The links between records in the network model were not foreign keys, but more like **pointers** in a programming language. The only way of accessing a record was to follow a path from a root record along these chains of links. This was called an *access path*.
	- The **problem** was that they made the code for querying and updating the database complicated and inflexible. Changing access path means a lot of changes for handwritten database query code and rewriting to handle the new access path. It was difficult to make changes to an application's data model.
- The relational model 
	- A relation is simply a collection of tuples. 
	- Query optimizer automatically decides the "access path" (which parts of the query to execute in which order and which indexes to use)
	- Much easier to add new features to applications
- Comparison to ducument databases
	- Relational and document databases are not fundamentally different, the related item is referenced by a unique identifier, which is called a *foreign key* inthe relational model, and *document reference* in the document model. (Conclusion: document db is following the old path of CODASYL) 
##### Relational vs Document databases today

\* Here only the differences in the data model is discussed.
Advantages for the two databases:
- Document data model: 
	- schema flexibility 
	- better performance due to locality and for some applications
	- closer to the data structures used by the application
- Relational model:
	- providing better support for joins
	- many-to-one and many-to-many relationships
- Which data model leads to simpler application code?
	- If the data in application has a document-like structure (a tree) then it's probably a good idea to use a document model.
	- However, for document model, you cannot refer directly to a nested item within a document, it support poorly for joins, and cumbersome to handle many-to-many relationships.
	
###### Schema flexibility in the document model

Most document databaes, and the JSON support in relational databases, do not enforce any schema on the data in documents. Clients have no guarantees as to what fields the documents may contain.

Document databases are more accuratly described as *schema-on-read* (this is similar to dynamic type checking in programming languages), while in traditional approach of relational database it is *schema-on-write* (static type checking).


###### Data locality for queries

###### Convergence of document and relational databases



