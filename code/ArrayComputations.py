class ArrayComputations:
    def __init__(self, array):
        self.array = array

    def increasing_sort(self):
        return sorted(self.array)

    def decreasing_sort(self):
        return sorted(self.array, reverse=True)

    def count_frequency(self):
        self.map_dict = {}
        for i in self.array:
            if self.map_dict.get(i):
                self.map_dict[i] += 1
            else:
                self.map_dict[i] = 1
        return self.map_dict
