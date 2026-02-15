### Functions with more than 1 input
def greet_with_name(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")

# greet_with_name(input("Hello, what's your name? "), input("Where do you live? "))

# greet_with_name("Jack", "Los Angeles")   # Keyword arguments


# Different positions give unexpected results:
greet_with_name("Los Angeles", "Jack")


#### Positional Arguments
greet_with_name(location="New York", name="Jack")