import random

### random.randint(a,b)
a = random.randint(1, 10)
print(a)
print(type(a))      # datatype = int


### random.random()
random_number_0_to_1 = random.random()           #generates a random floating point number between 0.0 and 1.0
print(f"The random number between 0.0 and 1.0 is {random_number_0_to_1}")


### random.uniform(a,b)
random_float = random.uniform(1,10)         # generates a random floating point between 1 and 10 (including 1 and 10 itself)
print(f"The random float is {random_float}")


### Heads or Tails generator (randomised)

random_int_heads_tails = random.random()
if random_int_heads_tails >= 0.5:
    print("Heads")
else:
    print("Tails")


### random.choice()

## check in the "who will pay the bill" code