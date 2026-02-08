### Lists are items stored in [] seperated by a comma

states_of_germany = ["Bavaria", "Lower Saxony", "Baden Wuettemberg", "Saxony", "Thuringia"]

## Extracting/Pulling an item from a list

print(states_of_germany[1])         ## indexing starts at 0 and not 1
print(states_of_germany[0])

print(states_of_germany[-1])           # accessing the last element of the list
print(states_of_germany[-2])            # accessing the second last element of the list

## Modifying items in the list

states_of_germany[1] = "Bayern"         # modifying the element in the python list
print(states_of_germany[1])

### Adding an item to the list

## APPEND
states_of_germany.append("Hamburg")
print(states_of_germany)

## EXTEND

states_of_germany.extend(["Berlin", "Schwelswig Holstein"])
print(states_of_germany)




