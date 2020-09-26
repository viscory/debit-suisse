def saladSpree(array, n):
    length = len(array[0])
    minimum = 1000000
    notZero = False
    for arr in array:
        i = 0
        index = -1
        while "X" in arr[index + 1:length]:
            index = arr.index("X", index + 1)
            if index > n - 1:
                while i + n <= index:
                    sum1 = 0
                    j = i
                    while j < i + n:
                        sum1 = sum1 + int(arr[j])
                        j += 1
                        
                    if sum1 < minimum:
                        minimum = sum1
                        notZero = True
                    i += 1
            i = index + 1
    if notZero:
        return minimum
    return 0

if __name__ == '__main__':
    array = [["12", "12", "3", "X", "3"], ["23", "X", "X", "X", "3"], [
        "33", "21", "X", "X", "X"], ["9", "12", "3", "X", "X"], ["X", "X", "X", "4", "5"]]
    n = 3
    print(saladSpree(array, 3))
    array = [["X", "X", "2"], ["2", "3", "X"], ["X", "3", "2"]]
    n = 3
    print(saladSpree(array, n))
    array = [["2", "3", "X", "2"], ["4", "X", "X", "4"],
        ["3", "2", "X", "X"], ["X", "X", "X", "5"]]
    n = 2
    print(saladSpree(array, n))
    