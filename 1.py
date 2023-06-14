import math


def zavdania2(kid, apple):
    each = apple // kid
    left = apple - kid * each
    print("Left: " + str(left) + "  Each: " + str(each))


def zavdania3(wake, hours, minutes):
    time = hours * 60 + minutes + wake
    H = int(time / 60)
    M = time - H * 60
    print("Hours: " + str(H) + " Minutes: " + str(M))


def zavdania4(a, b, c):
    all = a + b + c
    part = all / 2
    if part % 2 != 0:
        part = int(part) + 1
    else:
        part = int(part)
    print("Answer: " + str(part))


def zavdania5():
    k1 = int(input("1 : "))
    k2 = int(input("2 : "))
    k3 = int(input("3 : "))
    max = (k1 + k2 + abs(k1 - k2)) / 2
    max = (max + k3 + abs(max- k3)) / 2
    min = (k1 + k2 - abs(k1 - k2)) / 2
    min = (min + k3 - abs(min - k3)) / 2
    mid = (k1 + k2 + k3) - max - min
    print(str(int(max)) + "\t" + str(int(min)) + "\t" + str(int(mid)))


def zavdania6(a, b, l, N):
    result = (N * a) + 2 * (b * (N - int(N / 4) - 1)) + l
    print("Result: " + str(result) + "sm")