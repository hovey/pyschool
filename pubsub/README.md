# Publish-Subscribe (aka Observer)

The Publish-Subscribe design pattern, also known as the 
Observer design pattern, will be called called **pubsub** for short.

## Benefits

* Loose coupling between classes.  
  * An update to the client does not require an update to the service, and vice versa.
* Provides client with a uniform inferface for interacting with all objects.
  * Allows clients to code to an interface, and thus avoid coding to an implementation.
  * Allows client implementation to be [D.R.Y.](../README.md#dry-it-out) with respect calls to the service.
* Allows clients to add new classes without code modification.
* Allows clients to add new classes at run time.

## Implementation

* [Unittest](test/client.py), illustrating simple flow of pubsub.
* [Client](test/client.py), using a Factory design pattern in addition to pubsub.
