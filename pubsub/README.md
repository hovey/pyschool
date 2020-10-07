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

The unit tests were created using the concept of 

* [Unittest](test/client.py), illustrating simple flow of pubsub, with
  * two Publishers: *The Wall Street Journal* and *The New York Times*, implemented as the `Newspaper` class, and 
  * two Subscribers who both read newspapers: Alice and Bob, implemented as the  `Lectiophile` class.

Also, there is a client implementation that uses a Factory, which uses composition (the `has-a` relationship) instead of inheritance (the `is-a` relationship), but this effort remains a work-in-progress.

* [Client](test/client.py), using a Factory design pattern in addition to pubsub.

## Observerations

* Publishers
  * Publishers keep a list of their Subscribers.
  * Publishers, therefore, know about their Subscribers.  
  * Publishers offer Clients the API control to connect or disconnect from Subscribers.  
* Subscribers
  * Subscribers do not know about Publishers.  
  * The Subscriber's callback gets registered with one or more Publisher.
  * When the Publisher's have something new to announce, it notifies the Subscribers with the Subscriber's registered callback method.
  * When Subscribers receive an update via their registered callback, Subscribers do not know which Publisher tiggered the callback, thus maintaining a loose coupling betwen objects.
* Model-View architecture comparison:
  * The View knows about the Model and responds to updates from the Model.
  * The Model does not know about the View(s) that respond to the Model.
  * Thus the Model-View architecture is inverted from the Publish-Subscribe architecture in terms of which object knows about the other for stimulus-response type dehavior.
    * **Push Notification** 
      * Pubishers are a stimulus, and signal a response in Subscriber's callbacks.  
      * Publishers know about Subscribers.
    * **Pull Notification** 
      * Models are a stimulus, and model changes signal an update of Views.  
      * But, Models do **not** know about Views; rather, only Views know about the Models they watch.
      * Views periodically update their representation of Model by *polling* and *pulling* (i.e., asking and updating) if the Model has changed.  To accomplish this, Models may offer a hash or a datetime attribute, against which Views can judge if they are up-to-date.

## References

* Aaron Maxwell, [Observer Pattern in Python](https://www.protechtraining.com/blog/post/tutorial-the-observer-pattern-in-python-879)
