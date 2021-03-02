# Given a M x N square, print the number of 2 x 1 dominoes that can fit inside it

m, n = map(int, input().split())

print(m*n//2)