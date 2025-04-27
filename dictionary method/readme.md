# dict.clear()
The dict.clear() method is used to remove all items from a dictionary leaving it empty. It does not take any parameters and modifies the dictionary in place. After calling this method, the dictionary will have a length of 0. This operation does not return any value. useful when we  want to reuse an existing dictionary object without creating a new one, but need to remove all its contents first.
# dict.copy()
The dict.copy() method is used to create a shallow copy of a dictionary. It does not take any parameters and returns a new dictionary containing the same key-value pairs as the original. Changes made to the new dictionary do not affect the original dictionary, and vice versa. This method is useful when you need a duplicate of a dictionary but want to keep the original intact.
# dict.fromkeys(seq, value=None)
The dict.fromkeys() method is used to create a new dictionary with keys from the given sequence seq and values set to the specified value. If no value is provided, the default is None. This method is useful for initializing dictionaries with predefined keys and a common default value. it has a syntax
dict.fromkeys(seq, value=None)
seq: A sequence of elements that will become the keys of the dictionary.
value (optional): The value assigned to each key. Defaults to None.
# dict.get()
The dict.get() method is used to retrieve the value associated with a specified key in a dictionary. It takes two parameters: the key to look for and an optional default value to return if the key is not found. If the key exists in the dictionary, the corresponding value is returned; otherwise, the default value is returned. This method is useful for safely accessing dictionary values without raising a KeyError if the key is missing. 
Syntax
dict.get(key, default=None) 
key: The key to search for in the dictionary.  
default (optional): The value to return if the key is not found. Defaults to None.  
# dict.items()
The dict.items() method is used to return a view object that displays a list of a dictionary's key-value tuple pairs. This view object reflects any changes made to the dictionary. It does not take any parameters and is useful for iterating over a dictionary's contents in a for loop or converting the dictionary into a list of tuples.
Syntax:  
dict.items()
# dict.keys()
The dict.keys() method is used to return a view object that displays a list of all the keys in a dictionary. This view object reflects any changes made to the dictionary. It does not take any parameters and is useful for accessing or iterating over the keys of a dictionary. The returned view can also be converted into a list if needed.
Syntax:  
dict.keys()
# dict.pop()
The dict.pop() method is used to remove a specified key from a dictionary and return the corresponding value. It takes two parameters: the key to remove and an optional default value to return if the key is not found. If the key exists, it is removed from the dictionary, and its value is returned. If the key does not exist and no default value is provided, a KeyError is raised. This method is useful for retrieving and removing an item from a dictionary in a single operation.
Syntax:  
dict.pop(key, default=None)   
key: The key to remove from the dictionary.  
default (optional): The value to return if the key is not found. Defaults to None.  

# dict.popitem()
The dict.popitem() method is used to remove and return the last key-value pair from a dictionary as a tuple. This method does not take any parameters and modifies the dictionary in place. If the dictionary is empty, a KeyError is raised. It is useful when you need to remove and process items from a dictionary in a last-in, first-out (LIFO) order.

Syntax:  
dict.popitem()
Returns:  
A tuple containing the last key-value pair from the dictionary.
# dict.setdefault()
The dict.setdefault() method is used to retrieve the value of a specified key in a dictionary. If the key does not exist, it inserts the key with a specified default value and returns that value. This method is useful for ensuring that a key exists in a dictionary with a default value if it is not already present.

Syntax:  
dict.setdefault(key, default=None)  

Parameters:  
key: The key to search for in the dictionary.  
 default (optional): The value to insert and return if the key is not found. Defaults to None.  

Returns value :  
The value associated with the key if it exists, or the default value if the key is not found.  
# dict.update()
The dict.update() method is used to update a dictionary with key-value pairs from another dictionary or an iterable of key-value pairs. If a key already exists in the dictionary, its value is updated with the new value; otherwise, the key-value pair is added to the dictionary. This method modifies the dictionary in place and does not return any value.

Syntax:  
dict.update([other])  

Parameters:  
other (optional): A dictionary or an iterable of key-value pairs (e.g., a list of tuples) to update the dictionary with.  

Returns:  
None.  

This method is useful for merging dictionaries or adding multiple key-value pairs to an existing dictionary in a single operation.
# dict.value()
The dict.values() method is used to return a view object that displays a list of all the values in a dictionary. This view object reflects any changes made to the dictionary. It does not take any parameters and is useful for accessing or iterating over the values of a dictionary. The returned view can also be converted into a list if needed.

Syntax:  
dict.values()

Returns:  
A view object containing all the values in the dictionary.