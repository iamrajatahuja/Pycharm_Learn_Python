import random

#random() - return float number between 0.0 and 1.0 (excluded)
print(random.random())
print(random.random())

#randint(a,b) - generate integer number b/w a and b (both included)
print(random.randint(1,10))

#choice(sequence) - gives a random item from sequence
nums=[1,2,3,4,5,6,7,8,9,10]
print(random.choice(nums))

#shuffle(sequence) - returns None but change the sequence in random order
fruits=['apple','banana','mango']
random.shuffle(fruits)
print(fruits)