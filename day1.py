class Advent1:
    def get_text_from_url(self, url: str) -> list:
        import urllib.request
        response = urllib.request.urlopen(url)
        return response.read().decode('utf-8').splitlines()

    def count_number_increases(self, list_of_numbers):
        count = 0
        for i in range(len(list_of_numbers) - 1):
            if list_of_numbers[i] < list_of_numbers[i + 1]:
                count += 1
        return count



url = 'https://adventofcode.com/2018/day/1/input'
data = Advent1()

data.get_text_from_url(url)

##%

