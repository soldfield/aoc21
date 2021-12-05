fn = "data_day1_sonar_sweep.txt"

with open(fn) as f:
    data = f.readlines()

class Aoc_day2:
    """class for the Advent of Code Day 1"""
    def __init__(self):
        self.data = []

    def get_data(self, input_file):
        """get data from text file"""
        with open(fn) as f:
            data = f.readlines()

        self.data_file = data
        self.data = [i.strip() for i in self.data_file]
        self.data = [float(i) for i in self.data]

    def count_increases(self):
        """count the number of increases"""
        self.increases = 0
        data = self.data
        for i in range(1,len(data)):
            if data[i] > data[i-1]:
                self.increases += 1
        return self.increases
    
    def sliding_window_count_increases(self, window_size=3):
        """count number of increases from one sliding window to the next"""
        self.window_increases = 0
        data = self.data
        for i in range(0, len(data)-(window_size-1)):
            win1 = sum(data[i:i+window_size])
            win2 = sum(data[i+1:i+window_size+1])
            if win1<win2:
                self.window_increases += 1
        return self.window_increases

windowed_increases = Aoc_day2()
windowed_increases.get_data(fn)
print(windowed_increases.sliding_window_count_increases())
