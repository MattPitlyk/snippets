from time import sleep
import os


def clear(): os.system('cls' if os.name == 'nt' else 'clear')


for i in range(10):
    clear()
    print("Hello World!")
    print(i)
    sleep(1)
