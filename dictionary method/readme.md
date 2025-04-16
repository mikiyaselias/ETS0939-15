# dict.clear()
The dict.clear() method is used to remove all items from a dictionary leaving it empty. It does not take any parameters and modifies the dictionary in place. After calling this method, the dictionary will have a length of 0. This operation does not return any value. useful when we  want to reuse an existing dictionary object without creating a new one, but need to remove all its contents first.
# dict.copy()
The dict.copy() method is used to create a shallow copy of a dictionary. It does not take any parameters and returns a new dictionary containing the same key-value pairs as the original. Changes made to the new dictionary do not affect the original dictionary, and vice versa. This method is useful when you need a duplicate of a dictionary but want to keep the original intact.
# dict.fromkeys(seq, value=None)
The dict.fromkeys() method is used to create a new dictionary with keys from the given sequence seq and values set to the specified value. If no value is provided, the default is None. This method is useful for initializing dictionaries with predefined keys and a common default value. it has a syntax
dict.fromkeys(seq, value=None)
seq: A sequence of elements that will become the keys of the dictionary.
value (optional): The value assigned to each key. Defaults to None.