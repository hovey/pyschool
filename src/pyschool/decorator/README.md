# Decorators

Consider the interaction between a client and a service.
The client code, as it currently exists, makes copious use of a 
service API throughout the client code base.  A change by the service
of how service methods are called (the "contract") 
would generate significant client-side
liability:  Before the existing clients could make use of the updated
service-side functionality, client-side API calls of the service methods
would require update and refactor.  This is an example 
of *tight coupling*.

While *tight coupling* between will always exists between clients and their
services, by virtue of using the client using the service API in the 
first place,
it would be nice to conceive a way to *loosen this coupling*, so that 
updates in services could be made more independently of clients.

**Decorators** allow for a way to loosen that direct coupling between 
client and service.

The *decorator* concept first appeared as a design pattern in the
Gang of Four (GoF) and is frequently implemented in C++ and Java.

Later, the *decorator* appeared in Python.  

What are the similarities and differences between design pattern
decorators and Python decorators?

## Similarities

The design pattern decorator and the Python decorator are similar in the 
following ways:

* Decorators, both design pattern and Python, allow for modification of the
*behavior* of the service without modification of the *interface* of the
service.
* In other words, decorators allow us to change 
(e.g. to "enhance" or to "decorate") the original service content *without*
disrupting existing client calls to that service.  We can modify the 
service code without requiring that clients update their calls to the 
service.   
* In contrast, if modification to the service code required modification
to the client code (the case we are tying to avoid with decorators), 
service code changes would generate significant client-side burden
to update extant client calls to a service from the old service API 
to the new service API.
* Services should attempt to avoid API migration since it likely 
breaks client
code and mandates that clients update their API calls to fix what 
broke when the service API changed.

## Differences

The design pattern decorator and the Python decorator are different in the 
following ways:

* The design pattern decorator is dynamically typed and produces 
modification at run time.
* In contrast, the Python decorator is statically typed and produces
modification prior to run time.

