from sys import stdin

thing = []
counter = 0
for line in stdin:
    thing.append(int(line.strip()))
    if len(thing) == 4:
        if sum(thing[0:3]) < sum(thing[1:4]):
            counter += 1
        del thing[0]
    
print(f"Counter: {counter}")