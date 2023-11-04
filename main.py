import multiprocessing
from multiprocessing import Pool
from selenium import webdriver

from selenium_logic import slots_booker


if __name__ == '__main__':
    processes = [multiprocessing.Process(target=slots_booker) for _ in range(3)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
