# Publish-Subscribe (aka Observer)

The Publish-Subscribe design pattern, also known as the 
Observer design pattern, will be called called **pubsub** for short.

## Introduction

Two conceptual designs illustrate two pubsub patterns:

1. **pubsub push**, which is the typical Publish-Subscribe pattern.
2. **pubsub pull**, which is an atypical inversion of the original pattern, swapping who knows of whom.

### Pubsub Push

* An Event is triggered "on schedule."
* An Event triggers a push notification.
* Publishers know about Subscribers.
* Subscribers do not know about Publishers.

| interface | `IPub` | `ISub` |
|---|---|---|
| **creation** | | `+pubsub_callback()` | 
| | | Required by the `ISub` interface, Subscribers implement the public `pubsub_callback` method. |
| **registration** | `+subscribers(ISub)` |  |
| | Required by the `IPub` interface, Publishers implement the public `subscribers` method, which takes an `ISub` argument.| | 
| | `def subscribers(self, subscriber):` </br> `self._subscribers.append(subscriber)` |  |
|   | Publishers register objects that implement the `ISub` interface. | | 
| | Publishers know about Subscribers.  | Subscribers do not know about Publishers. |
| **event**, **notification** | An event is triggered.  Publishers notify their Subscribers. | 
|   | `for s in _self.subscribers:` </br> `s.pubsub_callback()`  | Subscribers react to the notification with whatever they have implemented in their callback. |
| **example** |  | Newspaper Subscribers fill out a form with their name and postal address. |  |   |
|  | Newspaper Publishers collect from Newspaper Subscribers forms with their name and address. | |
| | The "on-schedule" event is triggered by a 24-hour time interval. News is report daily. | | 
|  | On a daily frequency, Newspaper Publishers send a newspaper (their notification) to Newspaper Subscribers. |  |  |   |
| |  | Newspaper Subscribers react to the notification by reading the newspaper (their callback).

### Pubsub Pull

* An Event is triggered "on demand."
* An Event triggers a pull notification.
* Publishers do not know about Subscribers.
* Subscribers know about Publishers.

| interface | `IPub` | `ISub` |
|---|---|---|
| **creation** | `+pubsub_callback()` | |
| | Required by the `IPub` interface, Publishers implement the public `pubsub_callback` method. |
| **registration** | | `+publishers(IPub)` |  |
| | | Required by the `ISub` interface, Subscribers implement the public `publishers` method, which takes an `IPub` argument.|
| | | `def publishers(self, publisher):` </br> `self._publishers.append(publisher)` |
| | | Subscribers register objects that implement the `IPub` interface. | 
| | Publishers do not know about Subscribers. | Subscribers know about Publishers.  | 
| **event**, **notification** | | An event is triggered.  Subscribers notify their Publishers. |
| | Publishers react to the notification with whatever they have implemented in their callback. | `for p in _self.publishers:` </br> `p.pubsub_callback()`  | 
| **example** | Grocery Publishers provide an online grocery delivery service via their website.  |   |
| | | Grocery Subscribers collect from Grocery Publishers a website address. |
| | | The "on-demand" event is triggered when Subscribers need more food.  No definite time interval between events exists because food demand depends on (e.g., historical) external factors, such as number of times Subscribers dined out versus cooked at home, or the size of the Subscribers' previous food orders. |
| | | On an as-needed frequency, Grocery Subscribers request groceries (their notification) from Grocery Publishers. |
| | Grocery Publishers react to the notification, typically filling the order (their callback) and making it available to the Grocery Subscriber for curbside pickup. | |


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
* Ariel Ortiz, [Design Patterns in Python for the Untrained Eye](http://34.212.143.74/s201911/pycon2019/docs/design_patterns.html#_observer_pattern), Observer Pattern, Pycon USA 2019, May 1, 2019, Cleveland OH USA.
