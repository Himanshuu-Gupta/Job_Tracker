from code.ArrayComputations import ArrayComputations

if __name__ == '__main__':
    arr = ArrayComputations(array=[1, 2, 3, 4, 1, 2, 3, 2, 3, 2, 2, 2])
    print(arr.increasing_sort())
    print(arr.decreasing_sort())
    print(arr.count_frequency())

