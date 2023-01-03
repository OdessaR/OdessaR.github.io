# Part I: Foundations of Data Systems

Three **concerns** that are most important in most software systems:
1. Reliability: work correctly under adversity
2. Scalability: reasonable ways to deal with growth in data volumn, traffic volumn or complexity
3. Maintainability: different people should be able to work productively
## Chapter 1

### Reliability
Typical expectations for a software:
1. Performs expected function
2. Tolerate user mistake or unexpected usage
3. performance is good enough for the required use case, under the expected load and data volume
4. Prevents any unautorized access and abuse

To have a software to "continue to work correctly", we are talking about "fault-tolerant or resilient", but it only makes sense to deal with "certain types of faults" due to resource constrains.

It can make sense to increase the rate of faults by triggering them deliberately, as many critical bugs are actually due to poor error handling. By doing so, the fault-tolerance machinery is continually exercises and tested. (example, the Netflix *Chaos Monkey*)
* **Chaos Monkey**, a tool that randomly disables our production instances to make sure we can survive this common type of failure without any customer impact.

For **security matters**, prevention is better than cure. 

#### Hardware Faults

On a storage cluster with 10k disks, we should expect on average one disk to die per day.
Add redundancy cannot cofmpletely prevent hardware problems, but **single machine redundancy** is normally sufficiant. For some cloud platforms such as AWS, it if fairly common for VMs become unavailable without warning, as Cloud platforms are designed to prioritize flexibility and elasticity.
-> Software fault tolerance techniques then is preferred or as additional measurement for this situation. **Operational advantages**: no (planned) system downtime.

#### Software Errors

Systematic faults has no quick solution, they often lie dormant for a long time until getting triggered, this is mostly caused by software making **assumptions about its environment**.
- Small things to help: Think about assumptions and interactions in the system, testing, process isolation, allow process to crash and restart, measure monitor and analyze system behavior in production. 
#### Human Errors

How to make systems more reliable with unreliable humans:
1. Design with minimized opportunities for error
2. Decouple where most mistakes are made and where failures are caused
3. Tests
4. Quick and easy recovery for human errors. 
    1. For example, configuration changes, roll out new code gradually, tools to recompute data
5. Detailed and clean minitoring
    1. Performance metrics and error rates.
6. Good management practices and training

### Scalability

The discussion of system scalability is not one-dimensional.
- If the system grows in a paricular way, what are our options for coping with the growth?
- How can we add computing resources to handle the additional load?

#### Describing Load

Use load parameters to describe load for load growth questions.
Load factors depends on the architecture of your system.
**Example from Twitter:**
- Operations:
    1. Post tweet: 4.6k req/sec on average, over 12k req/sec at peak
    2. Home timeline: 300k req/sec
- Scaling challenge is not due to tweet volumn, but *fan-out*.
    - In transaction processing systems, we use it to describe the number of requests to *other services* that we need to make in order to serve one *incoming* request.
- Two ways to implement the two operations:
    1. New tweet gets inserted in to a global collection of tweets. Every time a user requests their home timeline, we look up all the tweets of the people this user follows, merge result and sort by time.
    2. Maintain a cache for each user's home timeline like a mailbox of tweets for each recipient user. When a user requests their home timeline, we simpy returns the cached timeillne.
- Downside of the second aproach: a lot of extra work. For example, an account with 30 million followers woud lead to 30 million writes to home timelines
- Note: Twitter is using a hybrid approach for influencer accounts and normal accounts

#### Describing Performance

- With the load description, there are two ways to look at a load increase problem:
    1. Keep current system resources, how much is performance affected?
    2. Keep current performance, how much more resource is required?
- Performance numbers:
    1. Batch processing system (e.g. Hadoop): throughput
        1. The number of records we can process per second
        2. The total time it takes to run a job on a dataset of a certain size
    2. Online system: response time
        1. The time between a client sending a request and receiving a response
- We need to think of response time as a *distribution* of values that you can measure
- What are we looking at if we look at difference percenties, taking response times for a sample requests to a service:
    1. Median: half way point, how long users typicaly have to wait.
    2. p95, p99, p999: how bad your outliers are. They are also known as tail latencies, they directly affect users' experience of the service.
 
#### Approaches for coping with load

Scaling up: vertical scaling, moving to a more powerful machine
Scaling out: horizontal scaling, distributing the oad across multiple smaller machines

Elastic system: useful if load is highly unpredictabe
Manually scaled system: simpler and may have fewer operationa surprises

Common widom until recently: keep your database on a single node (scale up) until scaling cost or high-availability requirements forced you to make it distributed.

An architecture that scales well for a *particular* application is built around assumptions of load facters. However, once the assumption is wrong, the appllication will face major performance problem. Therefore, it is important for early-stage applications to be able to iterate quickly on product features.

### Maintainability

Cost of maintaining is much higher than developing, and legacy system is very painful to deal with.

#### Operability

A good **operations team** typical responsibles:
1. Monitoring system health status and quickly restoring service
2. Tracking down the cause of problems
3. Keeping software and platforms up to date, including security patches
4. Keeping tabs on how different systems affect each other
5. Anticipating future problems
6. Establishing good practices and tools for deployment, configuration management and more
7. Performing compex maintenance tasks
8. Maintaining the security of the system
9. Defining processes that make operations predictable and help keep the production system stabe
10. Preserving the organization's knowledge about the system

**Data system** can make the routine tasks easy by:
1. Providing *visibility* into the runtime behavior and internals of the system
2. Providing good support for *automation* and integration with *standard tools*
3. Avoiding *dependency* on individual machines
4. Providing good *documentation* and an easy-to-understand *operational model*
5. Providing good *default behavior*, but also allow admin to override defaults
6. *Self-healing* where appropriate, but also allow admin to manual control
7. Exhibiting predictable behavior, minimizing surprises

#### Simplicity

**Abstraction** is one the best tool to be used for removing *accidental complexity* (complexity being introduced only from the implementation and not inherent in the problem). 

#### Evolvability

Agile working patterns provide a framework for adapting to change for organizational processes.
The ease to modify a data system is closely linked to its simplicity and its abstractions.

# Part II: Distributed Data

# Part III: Derived Data

