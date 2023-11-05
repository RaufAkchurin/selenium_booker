import multiprocessing

import selenium_logic

if __name__ == '__main__':
    num_instances = 10

    processes = []

    for i in range(num_instances):
        process = multiprocessing.Process(target=selenium_logic.central)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("Все экземпляры приложения Selenium завершили выполнение.")
