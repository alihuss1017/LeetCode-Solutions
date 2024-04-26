arr = [1, 4, 2, 5, 3]
counter = 1
ans = 0
while not counter > len(arr):
    for idx, val in enumerate(arr):
        if counter % 2 != 0:
            if idx + counter > len(arr):
                break
            ans += sum(arr[idx:idx + counter])
            print(ans)
    counter += 1