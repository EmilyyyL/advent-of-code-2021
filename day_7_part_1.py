thingy = list(map(int, input().split(",")))
fuel = []

for i in range(len(thingy)):
    tmp = 0
    for t in thingy:
        tmp += abs(t - i)
    fuel.append(tmp)

print(f"Fuel spent: {min(fuel)}")