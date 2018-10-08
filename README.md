# pyflection 
### Python3
###### Matt Andrzejczuk 2018
Code that writes code.



# QUICK START
Assume you already have the following class:
```
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

### ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~


# DECLARE AND MANIPULATE RESTfulLogin WITHOUT IMPORTING THE DEPENDENCIES
```
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



# Optional, stripped_props is a list of the properties
# defined for RESTfulLogin.
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

### ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
