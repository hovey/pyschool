# Factory Pattern

## Builder

### Definition

* Creates and then returns to a client *a single object* frequently composed of
two or more sub-objects following a composition recipe or template.  Builders offer clients
these fixed single objects from a finite menu of available choices.

### Examples

* **Food example**: A customer (client) orders from a Builder Factory (a restaurant)
from a list (a menu) of two set options: (1) a vege option or (2) a paleo 
option.
  * The `vege` option is created from a recipe that specifies one rice portion, one
  bean option, and one broccoli portion.
  * The `paleo` option is created from a recipe that specifies one beef portion,
  one chicken portion, and one broccoli portion.

#### Before 

```python
# service.py before
def menu_item(beans: bool, beef: bool, broccoli: bool, chicken: bool, rice: bool):
    # business logic for creations, such as measuring food portions, cooking food, and
    # returning food to the customer, e.g., plating food, packaging it for take out.

# vege_client.py before
my_vege_order = service.menu_item(True, False, True, False, True)

# paleo_client.py before
my_paleo_order = service.menu_item(False, True, True, True, False)
```

#### After

```python
# service.py after
def menu_vege():
    # clients are relieved from calling this service with a long set of parameters
    self._private_business_logic()

def menu_paleo():
    # similarly simplifies client orders
    self._private_business_logic()

def _private_business_logic():
    # Common business logic for creations, such as measuring food portions, cooking food,
    # and returning food to the customer, e.g., plating food, packaging it for take out, 
    # can be moved to a private class within the service.

# vegetarian_client.py after
my_vege_order = service.menu_vege()

# paleo_client.py before
my_paleo_order = service.menu_paleo()
```

* **Home example**: A customer (home buyer) orders from a Builder Factory (a residential
home builder) from three set options:  (1) a two-bedroom home, (2) a three-bedroom
home, or (3) a four-bedroom home.
  * The two-bedroom home follows a recipe that specifies one bathroom.
  * The three-bedroom home follows a recipe that specifies two bathrooms.
  * The four-bedroom home follows a recipe that specifies three bathrooms.
* **Vehicle example**:  A customer (client) orders from a Builder Factory (vehicle
dealership) from a list of three set options:  (1) a car, (2) a truck, (3) a van.
  * Clients receive objects that are complete assemblies of a recipe, e.g., a complete
  vehicle, and not parts of a recipe, e.g., just tires, which are parts of cars.
  * For connection to the *Abstract Factory* pattern, assume the following
  character about vehicles and tires to be true.
    * A car recipe specifies four high-performance tires.
    * A truck recipe specifies four mud and snow tires.
    * A van recipe specifies four all-season tires.

### Attributes

* The created objects
  * are complete units or assemblies; they are not parts in need of further assembly,
  * follow a recipe and thus are completely specified; the client need not make creation
  or specification decisions.
* Passing large number of parameters for creation is a *code smell* that
  indicates a Builder may improve the code architecture and simplify creation of
  objects for clients.

### Trade-Offs

* Reduced client complexity
  * The Builder pattern burdens clients to fewer parameters, especially a lot of `False`
  parameter passing, but does so at the cost of increasing the API surface area from
  a single function call to two or more function calls.  
    * If there are `n` mutually exclusive parameters, there are `2^n` combinations that
    a single API, e.g., `menu_item` can create.  
    * Eliminating all parameters but offering
    the same combinations as a method API would result in `2^n` new service methods to
    replace the previous single service method.
  * Thus, the Builder trades parameter complexity for API complexity.
* Convention > Configuration
  * The Builder pattern locks clients into set menu recipes.
  * The Builder thus prefers convention over configuration, which is generally a positive
  outcome since it relieves clients of the burden of creation complexity.  
  * However, convention does limit clients to the available menu as specified by the API.
  * Therefore, convention does not allow for "off-menu" ordering, or creating objects 
  not already predefined by the service specification.

### Additional Examples

Let's build an example that further clarifies *reduced client complexity* item 
above.   We said that, in general, the trade off involves a set of `2^n` combinations.
But, as we will see next, this estimate is an *upper bound* for the complexity measure.
In practice, there will be fewer than `2^n` combinations.   This reduction 
occurs because Builders build 
things *with certain predefined combinations from a preset menu*.
Not all combinations will be sensible combinations, and therefore can be
eliminated as a possible menu item.
The following example demonstrates this practical result.

#### After

```python
# service.py before
def shopping_item(vinegar: bool, olive_oil: bool, chocolate: bool, peanut_butter: bool):

# client.py before
# Note: for more compactness in the parameter list, we use:
X = True  # capital letter "X"
O = False  # capital letter "O"

# There are 2^n = 2^4 = 16 combinations

# singletons (4 combination)
my_shopping_cart = service.shopping_item(X, O, O, O)  # vinegar
my_shopping_cart = service.shopping_item(O, X, O, O)  # olive_oil
my_shopping_cart = service.shopping_item(O, O, X, O)  # chocolate
my_shopping_cart = service.shopping_item(O, O, O, X)  # peanut_butter

# duals (6 combinations)
my_shopping_cart = service.shopping_item(X, X, O, O)  # vinegar and olive_oil
my_shopping_cart = service.shopping_item(X, O, X, O)  # vinegar and chocolate
my_shopping_cart = service.shopping_item(X, O, O, X)  # vinegar and peanut_butter
#
my_shopping_cart = service.shopping_item(O, X, X, O)  # olive_oil and chocolate
my_shopping_cart = service.shopping_item(O, X, O, X)  # olive_oil and peanut_butter
#
my_shopping_cart = service.shopping_item(O, O, X, X)  # chocolate and peanut_butter

# triples (4 combinations)
my_shopping_cart = service.shopping_item(X, X, X, O)  # vinegar, olive_oil, chocolate
my_shopping_cart = service.shopping_item(X, X, O, X)  # vinegar, olive_oil, peanut_butter
my_shopping_cart = service.shopping_item(X, O, X, X)  # vinegar, chocolate, peanut_butter
my_shopping_cart = service.shopping_item(O, X, X, X)  # olive_oil, chocolate, peanut_butter

# quads (2 combinations)
my_shopping_cart = service.shopping_item(O, O, O, O)  # none of the available items
my_shopping_cart = service.shopping_item(X, X, X, X)  # vinegar, olive_oil, chocolate, peanut_butter
```

The pattern that emerges is that the service, as it is currently implemented,
doesn't really *build* anything.
Instead, the current service just returns items from the
roster of four available items.  So, if the client wants to *build* something from the
four constituents, the client must do that work itself.  

While the present
implementation pattern is suitable for a grocery cart context, it migrates
away from the Builder pattern since there is no predefined menu and since the
shopping item method doesn't build (amalgamate) constituents; it just returns
constituents.  If we truly wanted a shopping cart implementation, it would
be cleaner for the service to publish a list of available items, e.g., 

```python
# service.py
service_items = ("vinegar", "olive_oil", "chocolate", "peanut_putter")
def shopping_item(item: str)
```

and then have clients order single items with a single call, e.g., 

```python
# client.py
# we just need vinegar and olive oil today...
my_shopping_cart = service.shopping_item("vinegar")
my_shopping_cart = service.shopping_item("olive_oil")
```

Let's return to the two defining concepts of the Builder pattern:  

1. Creates and returns to a client *a single object* frequently composed of two
or more sub-objects following a composition recipe or template.
2. Prefers *convention over configuration* to reduce client burden of decision 
complexity.

Considering these two concepts together, we finally will see that the `2^n`
combinations estimate is a theoretical upper bound.  In practice, there will
be far fewer than `2^n` combinations that make sense.  Let's return to our
shopping cart example.

#### After

We see that with `n=4` parameters, there are 16 possible combinations.  But, only two
of these combinations will make sense:  (1) vinegar and olive oil, and (2) chocolate and
peanut_butter.  These combinations will be created and offered back to the
client as *a single object*; respectively,

1. `salad_dressing` (recall vinegar and olive oil are 
classic salad dressing constituents) and
2. `candy_bar` (recall the chocolate and peanut butter constituents to a REESE'S Peanut Butter
Cup).

```python
# service.py
service_items = ("salad_dressing", "candy_bar")
def shopping_item(item: str)
```

and then have clients order single items with a single call, e.g., 

```python
# client.py
# we just need salad dressing today...
my_shopping_cart = service.shopping_item("salad_dressing")
```

### Conclusion

A Builder is a creation pattern (Factory) that returns a single and complete 
object to a client.
That single object is frequently composed of two or more sub-items.  The combination
of sub-items is work that the Builder does so clients don't have to do the same
work.  (Similar to eating out, someone else does all the shopping, cooking and
cleaning for you, the customer).  

As a result of not having to undertake the building work, the client has a
finite number of options (the menu) from which to order from the service.  
The menu thus simplifies the client interaction with the service, where
convention is preferred to configuration.

## Abstract Factory

* Creates and then returns to a client *a multiplicity of objects* that all
belong to a certain style or theme.
  * **Vehicle example**:  A car dealership (client) orders from an Abstract Factory
  (tire manufacturer) any number of high-performance tires (e.g., car tires),
  depending on demand from the car dealership's customers.
    * A car dealership, since it only deals with cars and not trucks or vans, never
    would order mud-and-snow tires (for trucks) or all-season tires (for vans).

*More to come.*

