import csv
import random
from CreateAuthorList import createAuthorList

my_list = createAuthorList
print(my_list)
print(len(my_list))

def randomIndex(given_list):
    return random.randint(1,(len(given_list)-1))


def randomNum():
    return random.randint(1,5)

