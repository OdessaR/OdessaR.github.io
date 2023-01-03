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

JSON re
### Query Languages for Data


### Graph-Like Data Models



