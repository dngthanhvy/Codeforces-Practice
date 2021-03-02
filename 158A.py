# For a scoreboard of n contestants, only the ones that have a better score than the k-th contestant can pass.
# Print the number of contestant that passed.
# Note: only scores that are positive.

n, k = map(int, input().split())

score_list = list(map(int, input().split()))

counter = 0

for elem in score_list:
    if (elem > 0) & (elem >= score_list[k-1]):
        counter += 1

print(counter)

