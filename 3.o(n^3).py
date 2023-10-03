n = int(input())
length = input().split()
width = input().split()
height = input().split()
for i in range (n):
    for j in range (n):
        for k in range (n):
            print(int(length[i]) * int(width[j]) * int(height[k]), end = " ")