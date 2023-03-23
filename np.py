"""Main module."""
import numpy as np

if __name__ == '__main__':
    """Start of the program."""
    # 1
    arr = np.array([range(i, i+33) for i in range(2, 100, 33)])
    print(arr)

    print()

    # 2
    arr = np.zeros((8, 8), dtype=int)
    arr[::2, ::2] = 1
    arr[1::2, 1::2] = 1
    print(arr)

    print()

    # 3
    arr = np.zeros((8, 8), dtype=int)
    for i in range(8):
        arr[i, 0:0+i] = 1
    print(arr)

    print()

    # 4
    arr1, arr2 = np.split(np.arange(0, 16).reshape((4, 4)), 2, axis=1)
    print(arr1)
    print(arr2)

    print()

    # 5
    m = 50
    n = 15
    arr = np.array([np.random.randint(-1000, 1000) for _ in range(m*n)]).reshape((m, n))
    arr = arr.reshape(m*n)
    ml = sorted(arr.tolist())
    print(ml)
    k = int(input("Enter value to find: "))
    left, right = 0, m*n - 1
    while left + 1 < right:
        mid = left + ((right - left) // 2)
        vl = ml[mid]
        if vl < k:
            left = mid
        else:
            right = mid
    if abs(k - ml[left]) > abs(ml[right] - k):
        print(ml[right])
    else:
        print(ml[left])
