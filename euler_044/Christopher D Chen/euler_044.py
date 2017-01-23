#!/usr/bin/env python3
"""Pentagon numbers
Problem 44

Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

"""


def quadratic(a, b, c) -> float:
    sq = (b**2 - 4 * a * c)**(1 / 2)
    denom = 2 * a
    return max(((-b + sq) / denom, (-b - sq) / denom))


def pn(n) -> float:
    """nth pentagonal number"""
    return n * (3 * n - 1) / 2


def np(p) -> float:
    """n, given pentagonal number.
        If p is not a true pentagonal number
    then output will be a fraction."""
    return quadratic(3 / 2, -1 / 2, -p)


def test(a, b) -> bool:
    return np(a + b) % 1 == 0 and np(abs(a-b)) % 1 == 0
# print([nt(i) for i in [1, 3, 6, 10]])
# print([np(i) for i in [1, 5, 12, 22]])
# print([nh(i) for i in [1, 6, 15, 28]])


def main():
    a = 1
    while True:
        for b in range(a, 0, -1):
            pa, pb = pn(a), pn(b)
            if test(pa, pb):
                # print(a,b,abs(a-b))
                print(abs(int(pa - pb)))
                quit()
        a += 1
if __name__ == '__main__':
    main()