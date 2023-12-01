#!/usr/bin/python3
from sys import argv

num_args = len(argv) - 1
plural_suffix = 's' if num_args != 1 else ''

print("{:d} argument{:s}{}".format(
    num_args, plural_suffix, ':' if num_args > 0 else '.'))

for i, arg in enumerate(argv[1:], start=1):
    print("{:d}: {}".format(i, arg))
