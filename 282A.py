n = int(input())
x = 0

for i in range(0, n):
    statement = input()
    if "++" in statement:
        x += 1
    elif "--" in statement:
        x -= 1

print(x)