friends = ["Marco", "Carlo", "Bravo", "Serjio", "Perno", "Saltos", "Guro", "Eric", "Sara", "Susanna"]

print(len(friends))         # length is 10

print(friends[9])           # Susanna (last item)

# print(friends[10])        # IndexError: when there is not existent element in the list to be accessed


dirty_dozens = ["Strawberries", "Nectarines", "Spinach", "Kale", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
print(dirty_dozens)             # ['Strawberries', 'Nectarines', 'Spinach', 'Kale', 'Apples', 'Grapes', 'Peaches', 'Cherries',
                                    # 'Pears', 'Tomatoes', 'Celery', 'Potatoes']

## Lists within a lists

vegetables = ["Spinach", "Kale", "Tomatoes", "Potatoes", "Celery"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Cherries", "Peaches", "Pears"]

dirty_dozens_list_from_list = [fruits, vegetables]
print(dirty_dozens_list_from_list)          #[['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Cherries', 'Peaches', 'Pears'], ['Spinach', 'Kale',
                                                # 'Tomatoes', 'Potatoes', 'Celery']]
