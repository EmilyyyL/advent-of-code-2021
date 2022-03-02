from sys import stdin

result = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}, 10: {}, 11: {}}

i = 0
for line in stdin:
    for c in line.strip():
        result[i % 12][c] = result[i % 12].get(c,0) + 1
        i += 1

gamma = []
epsilon = []

for thing in result:
    gamma.append(max(result[thing], key=result[thing].get))
    epsilon.append(min(result[thing], key=result[thing].get))

gamma = int("".join(gamma), 2)
epsilon = int("".join(epsilon), 2)

print(f"Power Consumption = {gamma * epsilon}")