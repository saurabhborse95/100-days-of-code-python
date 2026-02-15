### Value in a dictionary can be a list or a dictionary itself


# Simple dictionary
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

## Nested list in dictioanry

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Ingolstadt"],
}

### Lets say we need to access  the Lille from the nested dictionry

print(travel_log["France"][1])
print(travel_log["Germany"][1])

# Mested list with other list

nested_list = ["A", "B", ["C", "D"]]            ## Nested list 2D

# lets try to access the letter "D"

print(nested_list[2][1])


### Nesting a dictionry inside a dictionary

travel_log = {
    "France": {
        "num_times_visited" : 8,
        "cities_visited" : ["Paris", "Lille", "Dijon"],
    },
    "Germany": {
        "num_times_visited" : 5,
        "cities_visited" : ["Berlin", "Ingolstadt"],
    }

}


## Lets say we need to access ingolstadt

print(travel_log["Germany"]["cities_visited"][1])