fn = "data_day1_sonar_sweep.txt"

with open(fn) as f:
    data = f.readlines()

class Aoc_day1:
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
    
sonar = Aoc_day1()
sonar.get_data(fn)
print(sonar.count_increases())
