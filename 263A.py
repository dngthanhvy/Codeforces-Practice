for row in range(0, 5):
    values = list(map(int, input().split()))
    for col in range(0, len(values)):
        if values[col] == 1:
            found_row = row+1
            found_col = col+1

print(abs(3-found_row) + abs(3-found_col))