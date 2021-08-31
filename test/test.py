from code.ArrayComputations import ArrayComputations

def test_increasing_sort():
    arr = ArrayComputations(array=[3,2,1])
    expected_result = [1,2,3]
    output = arr.increasing_sort()
    assert expected_result == output, "increasing_sort method failed"

def test_decreasing_sort():
    arr = ArrayComputations(array=[1, 2, 3])
    expected_result = [3,2,1]
    output = arr.decreasing_sort()
    assert expected_result == output, "decreasing_sort method failed"

def test_count_frequency():
    arr = ArrayComputations(array=[1, 1, 1, 1, 4, 5, 6])
    expected_result = [1, 4]
    output = arr.count_frequency()
    assert expected_result == output, "count_frequency method failed"


if __name__  == '__main__':
    test_increasing_sort()
    test_decreasing_sort()
    test_count_frequency()
