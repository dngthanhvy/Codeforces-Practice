n, k = map(int, input().split())

score_list = list(map(int, input().split()))

counter = 0

for elem in score_list:
    if (elem > 0) & (elem >= score_list[k-1]):
        counter += 1

print(counter)

