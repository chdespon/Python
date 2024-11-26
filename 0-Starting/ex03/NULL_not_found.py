# Write a function that prints the object type of all types of "Null".
# Return 0 if it goes well and 1 in case of error.
# Your function needs to print all types of NULL.

def NULL_not_found(object: any) -> int:
    dictionary = {float: "Cheese: nan",
                  type(None): "Nothing: None",
                  int: "Zero: 0",
                  str: "Empty: ",
                  bool: "Fake: False"}

    # if is in dictionary and is null, print
    if dictionary.get(type(object)) and (not object or object != object):
        print(dictionary.get(type(object)), type(object))
    else:
        print("Type not found")
        return 1
    return 0
