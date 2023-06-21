

"""
Author: Lucien No
Date Modified: June 18th, 2023.
Description: This file (theamth.py) holds the custom made trig/log functions that are used in the math

 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
** Function 1 **
MySin- This function uses taylor series approximation for the term x, n being nubmer of terms, in order to pinpoint the mathematically
correct resuult.
* Variables * 
n = number of terms
x = input value
Input: MySin(3)
Output: 0.14112000785871492

 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

** Function 2 **
MyCos- This function also uses taylor series approximation for the term x, with n being the number of terms in order to pinpoint the mathematically
correct result.
* Variables *
n = number of terms
x = input value
Input = MyCos(3)
Output: -0.9899924980061545

 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

** Function 3 **
MyTan- This function uses the MyCos and MySin functions in order to calculate tan correctly via (Sin/Cos)
* Variables * 
x = input value
MySin = see function 1
MyCos = see function 2
Input = MyTan(3)
Output = -0.1425465426686876

 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

** Function 4 **
MyLog10- This function uses binary searches in order to get the exact value instead of taylor series approxmation as iti's far more accurate with this
specific function.
* Variables *
x = Input value
low = 0 (lowest value in binary)
high = 1 (highest value in binary)
mid = the middle value of low,high

 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""


def MySin(x):
    result = 0
    for n in range(10):

        numerator = (-1) ** n * x ** (2 * n + 1)
        denominator = 1

        for i in range(1, 2 * n + 2):
            denominator *= i

        result += numerator / denominator
        print(result)

    return result

def MyCos(x):
    result = 0

    for n in range(10):
        numerator = (-1) ** n * x ** (2 * n)
        denominator = 1

        for i in range(1, 2 * n + 1):
            denominator *= i

        result += numerator / denominator

    return result


def MyTan(x):
    return MySin(x) / MyCos(x)


def MyLog10(x):
    if x <= 0:
        raise ValueError("Invalid input for logarithm")

    if x == 1:
        return 0

    low, high = 0, 1
    precision = 1e-9

    while high - low > precision:
        mid = (low + high) / 2
        
        if 10 ** mid > x:
            high = mid

        else:
            low = mid

    return low
