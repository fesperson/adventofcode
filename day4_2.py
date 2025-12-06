import numpy as np
from scipy.signal import convolve2d

with open("day_4_input.txt", "r") as file:
    content = file.read()
    arr = content.split("\n")
    for i in range(len(arr)):
        arr[i] = list(arr[i])
    arr = np.array(arr)
arr[arr == "@"] = 1
arr[arr == "."] = 0
arr = arr.astype("i")
window = np.ones((3,3))

total_removed = 0
more_to_remove = True
while more_to_remove:
    print(arr)
    convolve = convolve2d(arr, window, mode='same', boundary='fill', fillvalue=0)

    final = (arr * convolve)
    to_remove = (final > 0) & (final <= 4)
    print(to_remove)
    count_to_remove = np.count_nonzero(to_remove)
    print("Will remove", count_to_remove)
    total_removed += count_to_remove
    if count_to_remove == 0:
        more_to_remove = False
    arr = np.logical_not(to_remove) * arr

print(total_removed)