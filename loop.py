
# Task
# The provided code stub reads an integer, n, from STDIN. For all non-negative integers ¿ < n, print ¿2.
# Example
# n = 3
# The list of non-negative integers that are less than ʼn = 3 is [0, 1, 2]. Print the square of each number on a separate line.
# Θ
# 1
# 4
# Input Format
# The first and only line contains the integer, n.
# Constraints
# 1 ≤ n ≤ 20





if __name__ == '__main__':
    n = int(input())
    for i in range(n):
         print(i**2)