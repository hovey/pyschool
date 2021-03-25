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

## Abstract Factory

* Creates and then returns to a client *a multiplicity of objects* that all
belong to a certain style or theme.
  * **Vehicle example**:  A car dealership (client) orders from an Abstract Factory
  (tire manufacturer) any number of high-performance tires (e.g., car tires),
  depending on demand from the car dealership's customers.
    * A car dealership, since it only deals with cars and not trucks or vans, never
    would order mud-and-snow tires (for trucks) or all-season tires (for vans).

*More to come.*

