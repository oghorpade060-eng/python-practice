# Week 2: loops and dictionaries
# Learned: a for loop can count how often each item appears

fruits = ["apple", "banana", "apple", "mango", "banana", "apple"]
counts = {}
for fruit in fruits:
    counts[fruit] = counts.get(fruit, 0) + 1

print(counts)
