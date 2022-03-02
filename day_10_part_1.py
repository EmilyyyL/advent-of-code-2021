from sys import stdin

def add_point(c):
    if c == ")":
        return 3
    if c == "]":
        return 57
    if c == "}":
        return 1197
    if c == ">":
        return 25137


score = 0
for line in stdin:
    stack = []
    for c in line:
        if c == "}":
            if stack[-1] == "{":
                del stack[-1]
            else:
                score += add_point(c)
                break

        elif c == ")":
            if stack[-1] == "(":
                del stack[-1]
            else:
                score += add_point(c)
                break

        elif c == "]":
            if stack[-1] == "[":
                del stack[-1]
            else:
                score += add_point(c)
                break

        elif c == ">":
            if stack[-1] == "<":
                del stack[-1]
            else:
                score += add_point(c)
                break

        else:
            stack.append(c)

print(f"Score: {score}")