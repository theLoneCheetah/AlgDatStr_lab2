n = int(input("Введите размерность массива: "))
arr = [[[0 for x in range(n)] for y in range(n)] for z in range(n)]
print("Введите элементы массива:")
for i in range (n):
    for j in range (n):
        arr[i][j] = input().split()
        for k in range (n):
            arr[i][j][k] = int(arr[i][j][k])
key = int(input("Введите искомый элемент: "))
begin1 = begin2 = begin3 = 0
end1 = end2 = end3 = n - 1
while begin1 <= end1:
    mid1 = (begin1 + end1) // 2
    if arr[mid1][0][0] <= key <= arr[mid1][n - 1][n - 1]:
        break
    elif arr[mid1][0][0] > key:
        end1 = mid1 - 1
    else:
        begin1 = mid1 + 1
while begin2 <= end2:
    mid2 = (begin2 + end2) // 2
    if arr[mid1][mid2][0] <= key <= arr[mid1][mid2][n - 1]:
        break
    elif arr[mid1][mid2][0] > key:
        end2 = mid2 - 1
    else:
        begin2 = mid2 + 1
while begin3 <= end3:
    mid3 = (begin3 + end3) // 2
    if arr[mid1][mid2][mid3] == key:
        break
    elif arr[mid1][mid2][mid3] > key:
        end3 = mid3 - 1
    else:
        begin3 = mid3 + 1
print(mid1, mid2, mid3)