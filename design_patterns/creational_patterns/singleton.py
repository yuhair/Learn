
# =====================================================================================================================
# Borg Singleton: Borg singleton is a design pattern in Python that allows state sharing for different instances.
# =====================================================================================================================

class Borg:
    """Borg pattern making the class attributes global"""
    _shared_data = {}  # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data  # Make it an attribute dictionary


class Singleton(Borg):  # Inherits from the Borg class
    """This class now shares all its attributes among its various instances"""

    # This essenstially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)  # Update the attribute dictionary by inserting a new key-value pair

    def __str__(self):
        return str(self._shared_data)  # Returns the attribute dictionary for printing


# Let's create a singleton object and add our first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")
# Print the object
print(x)

# Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym.
y = Singleton(SNMP="Simple Network Management Protocol")
# Print the object
print(y)

# =====================================================================================================================
# Classic Singleton: Classic Singleton creates an instance only if there is no instance created so far;
#                    otherwise, it will return the instance that is already created.
# =====================================================================================================================

class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance

singleton = SingletonClass()
new_singleton = SingletonClass()

print(singleton is new_singleton)

singleton.singl_variable = "Singleton Variable"
print(new_singleton.singl_variable)


class SingletonChild(SingletonClass):
    pass

singleton = SingletonClass()
child = SingletonChild()
print(child is singleton)

singleton.singl_variable = "Singleton Variable"
print(child.singl_variable)
