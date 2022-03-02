from sys import stdin

score_list = []
for line in stdin:
    score = 0
    stack = []
    for c in line.strip():
        if c == "}":
            if stack[-1] == "{":
                del stack[-1]
            else:
                stack = []
                break
        elif c == ")":
            if stack[-1] == "(":
                del stack[-1]
            else:
                stack = []
                break
        elif c == "]":
            if stack[-1] == "[":
                del stack[-1]
            else:
                stack = []
                break
        elif c == ">":
            if stack[-1] == "<":
                del stack[-1]
            else:
                stack = []
                break
        else:
            stack.append(c)

    while stack != []:
        if stack[-1] == "(":
            score = (score * 5) + 1
            del stack[-1]
        elif stack[-1] == "[":
            score = (score * 5) + 2
            del stack[-1]
        elif stack[-1] == "{":
            score = (score * 5) + 3
            del stack[-1]
        elif stack[-1] == "<":
            score = (score * 5) + 4
            del stack[-1]
    if score != 0:
        score_list.append(score)

score_list.sort()

print(f"Score: {score_list[len(score_list)//2]}")
