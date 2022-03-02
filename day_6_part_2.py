initial = list(map(int, input().split(",")))
num = int(input())

# Dictionary Solution
collection = {
    0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0
}

for item in initial:
    collection[item] += 1

for i in range(num):
    new_fishies = collection[0]
    for item in collection:
        if item != 8:
            collection[item] = collection[item + 1]
    collection[8] = new_fishies
    collection[6] = collection[6] + new_fishies

print(f"FIshies {sum(collection.values())}")

# Array Solution
collection = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for item in initial:
    collection[item] += 1

for i in range(num):
    new_fishies = collection[0]
    for item in range(len(collection) - 1):
        collection[item] = collection[item + 1]
    collection[8] = new_fishies
    collection[6] = collection[6] + new_fishies

print(f"FIshies {sum(collection)}")

# Part 1 and part 2 offer the same solution but part 2 is much faster