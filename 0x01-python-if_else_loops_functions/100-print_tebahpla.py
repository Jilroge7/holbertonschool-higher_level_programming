#!/usr/bin/python3
# Print the alphabet backwards.

for chars in range(122, 96, -1):
    print("{:c}".format(chars), end='')
