# pyflection 
## Python3
###### Matt Andrzejczuk 2018

Declaring and modifying classes dynamically using strings. When many classes in your project share the same property labels, Reflection can cut out dozens of lines of code in a single function.

- - - - - -
### How To Use:
my_classes.py
```python
class Employee(PyflectiveEncoder):
    name = ""
```
### With Reflection:
```python
EmployeeR = getattr(__import__("my_classes"),
                   "Employee")
obj_with_name = EmployeeR
obj_with_name.__setattr__("name", "NEW NAME")
```
### Without Reflection:
```python
from my_classes import Employee
obj_with_name = Employee
obj_with_name.name = "NEW NAME"
```
- - - - - -
# QUICK START
Assume you already have the following class:
```python
from pyflection import PyflectiveEncoder

# Extremely Simple Class.
# only has two string properties.
class RESTfulLogin(PyflectiveEncoder):
    username = ""
    password = ""

    def __init__(self, user: str, pasw: str, *args, **kwargs):
        self.username = user
        self.password = pasw
        super(RESTfulLogin, self).__init__(*args, **kwargs)
```


###### DECLARE AND MANIPULATE RESTfulLogin WITHOUT IMPORTING THE DEPENDENCIES
```python
from pyflection import NonPropertyStripper
from pycolors import ink
import os

# 'user_mortal' cannot work without this import:
from dummy_reflective_class import RESTfulLogin

# 'user_phantom' imports it's dependencies dynamically
model_name = "RESTfulLogin"
lib = "dummy_reflective_class"
module = __import__(lib)
RESTfulLogin_Reflection = getattr(module, model_name)

# Optional, stripped_props is a list of the properties defined for RESTfulLogin.
raw_properties = dir(RESTfulLogin_Reflection)
stripped_props = NonPropertyStripper.clean(raw_properties)
# stripped_props = ["username", "password"]

user_phantom = RESTfulLogin_Reflection(user="phantom", pasw="123123")
user_mortal = RESTfulLogin(user="mortal", pasw="123123")

phantom_username = getattr(user_phantom, "username")
mortal_username = user_mortal.username

user_phantom.__setattr__("username", "ALTERED_Phantom")
user_mortal.username = "ALTERED_Mortal"
```

- - - - - -
## License
[MIT](https://choosealicense.com/licenses/mit/)
