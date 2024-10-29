### Part Four -- your code goes here. 

import random

random_numbers = []
for _ in range(10):
    random_numbers.append(random.randint(1, 100))

print("Original random numbers:", random_numbers)


i = 0
while i < len(random_numbers):
    if random_numbers[i] % 2 == 0:  
        random_numbers.pop(i)  
    else:
        i += 1  

print("With even numbers removed:", random_numbers)

