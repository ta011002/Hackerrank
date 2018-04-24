"""
Problem : Find the Running Median
Explain : https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem
Input : single integer, n, denoting the number of integers in the data stream.
        i of the n subsequent lines contains an integer, a_i, to be added to your list.
Output : After each new integer is added to the list, print the list's updated median
         on a new line as a single double-precision number scaled to 1 decimal place (i.e., 12.3 format).
"""

def running_median(a):
    if len(a) % 2 == 0:
        print((a[int(len(a)/2)-1] + a[int(len(a)/2)])/2)
    elif len(a) % 2 == 1:
        print(float(a[int(len(a)/2)]))

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    insort(a, a_t)
    running_median(a)