n = int(input())
arr = input().split()
for i in range (n):
    arr[i] = int(arr[i])
max1 = max2 = max3 = 0
for i in range (n):
    if arr[i] > max1:
        max3 = max2
        max2 = max1
        max1 = arr[i]
    elif arr[i] > max2:
        max3 = max2
        max2 = arr[i]
    elif arr[i] > max3:
        max3 = arr[i]
print(max1, max2, max3)