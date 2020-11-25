def countSort(arr):
    count_array = [0] * 100
    for i in range(len(arr)):
        if i < len(arr) // 2:
            arr[i][1] = "-"
        arr[i][0] = int(arr[i][0])
        count_array[arr[i][0]] += 1

    stabilizer = {}
    addable = 0
    for ind, el in enumerate(count_array):
        if el > 0:
            stabilizer[ind] = addable
            addable += el

    result = [""] * len(arr)
    for el in arr:
        ind = stabilizer[el[0]]
        result[ind] = el[1]
        stabilizer[el[0]] += 1
    return " ".join(result)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    print(countSort(arr))
