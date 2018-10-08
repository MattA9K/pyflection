# Matt Andrzejczuk 2018
from pyflection import NonPropertyStripper, PyflectiveEncoder
from pycolors import ink
import os

from dummy_reflective_class import RESTfulLogin





os.system("clear")


### ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
#   QUICK START
### ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
model_name = "RESTfulLogin"
lib = "dummy_reflective_class"
module = __import__(lib)
RESTfulLogin_Reflection = getattr(module, model_name)
raw_properties = dir(RESTfulLogin_Reflection)
stripped_props = NonPropertyStripper.clean(raw_properties)


user_phantom = RESTfulLogin_Reflection(user="phantom", pasw="123123")
user_mortal = RESTfulLogin(user="mortal", pasw="123123")


phantom_username = getattr(user_phantom, "username")
mortal_username = user_mortal.username


user_phantom.__setattr__("username", "ALTERED_Phantom")
user_mortal.username = "ALTERED_Mortal"
### ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~





RESTfulLogin_Reflection = getattr(module, model_name)

# 1. GET ALL RAW METHODS AND PROPERTIES FROM INSTANCE OF: RESTfulLogin
raw_properties = dir(RESTfulLogin_Reflection)

ink.print_orange("\nRAW_PROPERTIES: ", "\n")
ink.print_lightcyan("dir(", "")
ink.print_purple("RESTfulLogin_reflection", "")
ink.print_lightcyan(")", "\n")
ink.print_lightred(raw_properties, "\n\n")


# 2. RESTfulLogin INSTANCE SHOULD NOW HAVE ONLY A username AND password LIKE THE CLASS:
stripped_props = NonPropertyStripper.clean(raw_properties)


ink.print_yellow("STRIPPED: ", "\n")
ink.print_lightcyan("dir(", "")
ink.print_purple("RESTfulLogin_reflection", "")
ink.print_lightcyan(")", "\n")
ink.print_lightred(stripped_props, "\n\n")


# 3. RESTfulLogin CLASS DECLARED USING STRINGS ONLY:
user = RESTfulLogin_Reflection(user="root", pasw="123123")
ink.print_cyan("RESTfulLogin_Reflection instance created: \n", "")
ink.print_blue(user.get_json_pyflection(), "\n\n")

# 4. ALTER THE PROPERTY username OF RESTfulLogin USING A STRING ONLY:
user.__setattr__("username", "rootXYXYXYXYXY")
ink.print_green("RESTfulLogin_Reflection changed instance property 'user.username': \n", "")
ink.print_blue(user.get_json_pyflection(), "\n\n")


# 5. GET THE STRING VALUE OF username REFLECTIVELY:
RESTfulLogin_Reflection_username = getattr(user, "username")
ink.print_lightcyan(RESTfulLogin_Reflection_username, "\n")








