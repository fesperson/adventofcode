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
print(arr)
# padded = np.pad(arr, pad_width=1, mode='constant')
# print(padded)
 
window = np.ones((3,3))
convolve = convolve2d(arr, window, mode='same', boundary='fill', fillvalue=0)
print(convolve)
print(convolve.shape)
print(arr.shape)

final = (arr * convolve)
print(np.count_nonzero((final > 0) & (final <= 4)))


