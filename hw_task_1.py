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
        self.list_filled_event = threading.Event()
        self.total_sum = None
        self.average = None

    def fill_list(self):
        for _ in range(25):
            self.random_list.append(random.randint(1,1000))
        print(f"List filled with numbers: {self.random_list}")
        self.list_filled_event.set()

    def sum_list(self):
        self.list_filled_event.wait()
        self.total_sum = sum(self.random_list)
        print(f"Sum of numbers: {self.total_sum}")

    def average_list(self):
        self.list_filled_event.wait()
        self.average = sum(self.random_list) / len(self.random_list)
        print(f"Average of numbers: {self.average}")


def main():
    result = RandomNumbers()

    fill_thread = threading.Thread(target=result.fill_list())
    sum_thread = threading.Thread(target=result.sum_list())
    average_thread = threading.Thread(target=result.average_list())

    fill_thread.start()
    sum_thread.start()
    average_thread.start()

    fill_thread.join()
    sum_thread.join()
    average_thread.join()
    #result.fill_list()
    #result.sum_list()
    #result.average_list()


if __name__ == "__main__":
    main()
