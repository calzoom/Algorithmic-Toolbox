# Uses python3
# Max time used: 0.02/5.00, max memory used: 8585216/536870912

# There are two ways of running this program:
# 1. Run
#     python3 APlusB.py
# then enter two numbers and press ctrl-d/ctrl-z
# 2. Save two numbers to a file -- say, dataset.txt.
# Then run
#     python3 APlusB.py < dataset.txt

import sys

input = sys.stdin.read()
tokens = input.split()

a = tokens[0]
b = tokens[1]

c = int(a) + int(b)
print()
print(c)
