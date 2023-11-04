import multiprocessing

import selenium_logic

if __name__ == '__main__':
    num_instances = 3  # Укажите количество требуемых экземпляров Selenium

    processes = []

    for i in range(num_instances):
        process = multiprocessing.Process(target=selenium_logic, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("Все экземпляры приложения Selenium завершили выполнение.")
