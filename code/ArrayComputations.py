from scipy import stats as s

class ArrayComputations:
    def __init__(self, array):
        self.array = array

    def increasing_sort(self):
        return sorted(self.array)

    def decreasing_sort(self):
        return sorted(self.array, reverse=True)

    def count_frequency(self):
        return [s.mode(self.array)[0][0], s.mode(self.array)[1][0]]