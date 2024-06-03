"""
The app starts three threads when launched.
The first thread fills a list with random numbers.
Two other threads are waiting.
When the list is filled, both threads start.
The first thread finds the sum of the list elements,
the second thread finds the average in that list.
The received list, sum, and average are displayed on the screen.
"""

import threading
import random


class RandomNumbers:
    def __init__(self):
        self.random_list = []

    def fill_list(self):
        for _ in range(10):
            self.random_list.append(random.randint(1,100))
        print(f"List filled with numbers: {self.random_list}")

    def sum_list(self):
        total_sum = sum(self.random_list)
        print(f"Sum of numbers: {total_sum}")

    def average_list(self):
        average = sum(self.random_list) / len(self.random_list)
        print(f"Average of numbers: {average}")




if __name__ == "__main__":
    pass
