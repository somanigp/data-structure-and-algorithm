# How to detect if an arr is sorted or not:
def is_sorted_arr(arr: list[int]):  # O(n) to check if sorted.
    is_sorted: bool = True
    for i in range(len(arr)):
        if i+1 == len(arr):  # Break at the last element as arr[i + 1] is invalid then.
            return is_sorted
        if arr[i] > arr[i + 1]:  # For <= it's ok
            is_sorted = False
    return is_sorted


print(is_sorted_arr([1, 2, 2, 6, 10]))
