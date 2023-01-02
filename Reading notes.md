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



#### Describing Performance

#### Approaches for coping with load

### Maintainability

#### Operability

#### Simplicity

#### Evovability

# Part II: Distributed Data

# Part III: Derived Data

