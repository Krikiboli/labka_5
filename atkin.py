import multiprocessing as mp
import os
import sys
import timeit
from math import sqrt
from colorama import Fore, Back, Style
from colorama import init

init(autoreset=True)

def atkin(limit: int, proc: int) -> None:
    print(f"•Выполняется 'Решето Аткина' {proc} ")
    count_list = [False] * (limit + 1)
    for x in range(proc, int(sqrt(limit)) + 1, 3):
        for y in range(1, int(sqrt(limit)) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and n % 5 != 0 and (n % 12 == 1 or n % 12 == 5):
                count_list[n] = not count_list[n]
            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 5 != 0 and n % 12 == 7:
                count_list[n] = not count_list[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 5 != 0 and n % 12 == 11:
                count_list[n] = not count_list[n]
    if proc == 1:
        with open('one.txt', "w", encoding='utf-7') as file:
            for x in count_list:
                string = str(x) + '\n'
                file.write(string)
    elif proc == 2:
        with open('two.txt', "w", encoding='utf-7') as file:
            for x in count_list:
                string = str(x) + '\n'
                file.write(string)
    else:
        with open('three.txt', "w", encoding='utf-7') as file:
            for x in count_list:
                string = str(x) + '\n'
                file.write(string)


def write_in_file() -> None:
    with open('one.txt', 'r', encoding='utf-8') as one:
        first_read = one.read()
        list_1 = first_read.split("\n")
    with open('two.txt', 'r', encoding='utf-8') as two:
        first_read = two.read()
        list_2 = first_read.split("\n")
    with open('three.txt', 'r', encoding='utf-8') as three:
        first_read = three.read()
        list_3 = first_read.split("\n")

    os.remove('one.txt')
    os.remove('two.txt')
    os.remove('three.txt')
    dirty_list = [False] * len(list_1)
    for i in range(0, len(list_1)):
        if list_1[i] == "False":
            a = False
        else:
            a = True
        if list_2[i] == "False":
            b = False
        else:
            b = True
        if list_3[i] == "False":
            c = False
        else:
            c = True
        dirty_list[i] = (a + b + c) % 2
    nums = [False] * len(dirty_list)
    for index, x in enumerate(dirty_list):
        if x == 1:
            nums[index] = index
    for x in range(5, int(sqrt(len(dirty_list)))):
        if nums[x]:
            for y in range(x ** 2, limit + 1, x ** 2):
                nums[y] = False

    nums.pop()
    result = list()
    for index, elem in enumerate(nums):
        if elem is not False:
            result.append(elem)
    with open("result.txt", "w", encoding='utf-8') as file:
        file.write("2\n3\n5\n")
        for i in result:
            str0 = '' + str(i) + "\n"
            file.write(str0)


def start(limit: int) -> None:
    with mp.Pool(processes=3) as pool:
        pool.starmap(atkin, iterable=[[limit, 1], [limit, 2], [limit, 3]])
        pool.close()


if __name__ == '__main__':
    try:
        if int(sys.argv[1]) < 0:
            raise Exception
        if int(sys.argv[1]) == 0:
            raise Exception
    except Exception:
        print(Fore.RED + '•Неправильный аргумент')
    else:
        limit = int(sys.argv[1])
        start_time = timeit.default_timer()
        start(limit)
        write_in_file()
        print(Fore.GREEN + f'•Вычисление длилось: {timeit.default_timer() - start_time} секунд\n')
        print(Fore.GREEN + '•Скрипт завершен\n•Результат в папке с относительным путем')