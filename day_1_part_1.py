from sys import stdin

prev = None
counter = 0
for line in stdin:
    if prev is not None and int(line.strip()) > prev:
        counter += 1
    prev = int(line.strip())

print(f"Counter: {counter}")