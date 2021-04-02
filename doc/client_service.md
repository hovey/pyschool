# Client-Service Decoupling

Services should expose client functionality through a service API.  The API will be better when it [avoids verbs](get_and_set.md).  Services should not expose implementation.  

Clients should code to a service's interface, not implementation.  This allows the client to be only loosely coupled to the service, which is good.  Tight coupling is bad.  Loose coupling allows the client and the service to change over time independent from one another.  A change to the service that also requires a change to any and all clients who have used the service in the past is an example of [code smell](code_smell.md).
