# A statement in language Bit++ is a sequence, consisting of exactly one operation and one variable x. The statement
# is written without spaces, that is, it can only contain characters "+", "-", "X". Executing a statement means
# applying the operation it contains.
# ++X or X++ = add 1
# --X or X-- = sub 1
# Initial value of X : 0

n = int(input())
x = 0

for i in range(0, n):
    statement = input()
    if "++" in statement:
        x += 1
    elif "--" in statement:
        x -= 1

print(x)