# class collections.ChainMap(*maps)
"""

A ChainMap class is provided for quickly linking a number of mappings so they can be treated as a single unit.
It is often much faster than creating a new dictionary and running multiple update() calls.
The class can be used to simulate nested scopes and is useful in templating.

class collections.ChainMap(*maps)
A ChainMap groups multiple dicts or other mappings together to create a single, updateable view.
If no maps are specified, a single empty dictionary is provided so that a new chain always has at least one mapping.

The underlying mappings are stored in a list. That list is public and can be accessed or updated using the maps attribute.
There is no other state.

Lookups search the underlying mappings successively until a key is found. In contrast, writes, updates, and deletions only operate on the first mapping.
A ChainMap incorporates the underlying mappings by reference. So, if one of the underlying mappings gets updated, those changes will be reflected in ChainMap.
All of the usual dictionary methods are supported. In addition, there is a maps attribute, a method for creating new subcontexts, and a property for accessing
all but the first mapping:


---maps

A user updateable list of mappings. The list is ordered from first-searched to last-searched.
It is the only stored state and can be modified to change which mappings are searched.
The list should always contain at least one mapping.

---new_child(m=None)

Returns a new ChainMap containing a new map followed by all of the maps in the current instance.
If m is specified, it becomes the new map at the front of the list of mappings;
if not specified, an empty dict is used, so that a call to d.new_child() is equivalent to: ChainMap({}, *d.maps).
This method is used for creating subcontexts that can be updated without altering values in any of the parent mappings.

---parents

Property returning a new ChainMap containing all of the maps in the current instance except the first one.
This is useful for skipping the first map in the search.
Use cases are similar to those for the nonlocal keyword used in nested scopes.
The use cases also parallel those for the built-in super() function.
A reference to d.parents is equivalent to: ChainMap(*d.maps[1:]).

"""
import collections

c = collections.ChainMap(
    {"a": 1, "b": 2}, {"a": 3, "b": 4, "c": 6}
)  # Create root context
d = c.new_child()  # Create nested child context
print(d)
e = c.new_child({"x": 2})  # Child of c, independent from d
print(e)
print(e.maps[0])  # Current context dictionary -- like Python's locals()
print(e.maps[-1])  # Root context -- like Python's globals()
print(e.parents)  # Enclosing context chain -- like Python's nonlocals

d["a"] = 1  # Set value in current context
print(d["a"])  # Get first key in the chain of contexts
del d["a"]  # Delete from current context
print(d)
print(list(d))  # All nested values (keys)
print("x" in d)  # Check all nested values
print(len(d))  # Number of nested values (keys)
print(d.items())  # All nested items
print(dict(d))  # flatten to the one dict


class DeepChainMap(collections.ChainMap):
    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return
        self.maps[0][key] = value

    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)


d = DeepChainMap({"a": 1, "b": 2}, {"b": 3, "c": 4}, {"c": 5, "d": 6})
del d["c"]
print(d)
d["x"] = 3
print(d)
d["d"] = -1
print(d)
