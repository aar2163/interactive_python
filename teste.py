from time import time


a = [1,2,3]
delta = 1
delta = (delta) % 3

print a[delta:] + a[:delta]
