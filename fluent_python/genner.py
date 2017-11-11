# encoding=utf-8
import random


def my_gen():
    start = 'Welcome'
    while True:
        rc = yield start
        start = rc * random.randint(1, 10)

