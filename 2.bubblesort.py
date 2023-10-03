def s(m):
    for i in range(len(m)):
        for j in range(i+1,len(m)):
            if m[i]>m[j]:
                m[i],m[j]=m[j],m[i]
    return m
n=int(input('Введите количество элементов массива: '))
m=[0]*n
for i in range(n):
    m[i]=int(input('Введите элемент массива: '))
print('Отсортированный массив: ',s(m))