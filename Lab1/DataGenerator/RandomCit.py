import csv
import random


def randomIndex(given_list):
    print(len(given_list))
    return random.randint(1,(len(given_list)-1))


def randomNum():
    return random.randint(1,5)

