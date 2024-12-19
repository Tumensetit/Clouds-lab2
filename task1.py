import math
import flask

def numerical_integration(lower, upper, n):
    totalArea = 0
    width = (upper - lower) / n

    for i in range(n):
        x = lower + i * width
        height = abs(math.sin(x))
        totalArea += height * width

    return totalArea

def main():
    lower = 0
    upper = math.pi
    nValues = [10, 100, 100, 1000, 10000, 100000, 1000000]

    for n in nValues:
        result = numerical_integration(lower, upper, n)
        print(n, result)


if __name__ == "__main__":
    main()