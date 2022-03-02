from sys import stdin

total = 0
for line in stdin:
    signal_patterns, output = line.strip().split(" | ")
    signal_patterns = ["".join(sorted(list(x))) for x in signal_patterns.split(" ")]
    output = ["".join(sorted(list(x))) for x in output.split(" ")]
    remaining = []
    result = {}

    # Identifying 1, 4, 7 and 8
    for word in signal_patterns:
        if len(word) == 2:
            result[1] = word
        elif len(word) == 4:
            result[4] = word
        elif len(word) == 3:
            result[7] = word
        elif len(word) == 7:
            result[8] = word
        else:
            remaining.append(word)
    
    signal_patterns = remaining
    remaining = []

    # Identifying 0, 2, 3, 5, 6 and 9
    for word in signal_patterns:
        if len(word) == 5:
            if "".join(sorted(set(result[7] + word))) == word:
                result[3] = word
            elif "".join(sorted(set(result[4] + word))) == result[8]:
                result[2] = word
            else:
                result[5] = word
        elif len(word) == 6:
            if "".join(sorted(set(result[7] + word))) != word:
                result[6] = word
            elif "".join(sorted(set(result[4] + word))) == word:
                result[9] = word
            else:
                result[0] = word

    number = []
    for word in output:
        for item in result:
            if result[item] == word:
                number.append(item)
                break

    total += int("".join([str(num) for num in number]))

print(f"Sum: {total}")

