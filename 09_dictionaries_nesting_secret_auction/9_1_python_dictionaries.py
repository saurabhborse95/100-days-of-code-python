### Dictionaries

## every dictionary has two parts to it --> key and value

## {Key: Value, Key1:Value1}

programming_dictionary = {
    "Bug": "error in programming",
    "Function": "Piece of code that you can call easily again and again",
    "Loop": "the action of doing something again and again"
}
print(programming_dictionary)
print(programming_dictionary["Bug"])            # fetching a value for  a key in dictionary
print(programming_dictionary["Function"])
print(programming_dictionary["Loop"])

empty_dictionary = {}                                   # creating an empty dictionary

empty_dictionary["Bug"] = "error in programming"            # writing something to a dictionary or editing it
print(empty_dictionary)


## wiping the dictionary

# programming_dictionary = {}
# print("after wiping")
# print(programming_dictionary)


for thing in programming_dictionary:
    print(thing)                    # prints only the keys and not values of the given dictionry
    print(programming_dictionary[thing])            # prints the value