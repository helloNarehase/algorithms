"""
visualization binary serch
"""
import time
import numpy as np

def visual_bs(x, target, low=0, high=None):
    if high is None:
        high = len(x) - 1
    blue = "\033[44m"
    red = "\033[43m"
    ye = "\033[42m"

    while low <= high:
        mid = (low + high) // 2
        print("\033[2J\033[1H")


        for idx, value in enumerate(x):
            if idx == low:
                print(blue + f"{value:03d}\033[0m", end=" ")
            elif idx == high:
                print(red + f"{value:03d}\033[0m", end=" ")
            elif idx == mid:
                print(ye + f"{value:03d}\033[0m", end=" ")
            else:
                print(f"{value:03d}", end=" ")
        print()
        time.sleep(1)

        if x[mid] < target:
            low = mid + 1
        elif x[mid] > target:
            high = mid - 1
        else:
            print(f"Target {target} found at index {mid}")
            return mid

    print(f"Target {target} not found in the list.")
    return -1

l = np.random.randint(0, 100, (30))
l.sort(-1)
visual_bs(l, l[np.random.randint(0, 30)])
