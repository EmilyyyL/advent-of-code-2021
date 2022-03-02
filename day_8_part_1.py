from sys import stdin

counter = 0
for line in stdin:
    signal_patterns, output = line.strip().split(" | ")
    for word in output.split(" "):
        if len(word) == 2 or len(word) == 3 or len(word) == 4 or len(word) == 7:
            counter += 1

print(f"Number of times digits 1, 4, 7, or 8 appear: {counter}")

