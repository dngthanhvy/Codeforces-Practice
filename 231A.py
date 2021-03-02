n = int(input())

sure = []

counter = 0

for i in range(0, n):

    num_of_1 = 0

    sure = list(map(int, input().split()))

    for elem in sure:
        if elem == 1:
            num_of_1 += 1

    if num_of_1 >= 2:
        counter += 1

print(counter)