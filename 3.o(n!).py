def changes(arr, st, num, length):
    if num == length:
        print(st + arr[0])
    else:
        for i in range(len(arr)):
            new_arr = arr[:i] + arr[i + 1:]
            changes(new_arr, st + arr[i], num + 1, length)


arr = input()
changes(arr, "", 0, len(arr) - 1)