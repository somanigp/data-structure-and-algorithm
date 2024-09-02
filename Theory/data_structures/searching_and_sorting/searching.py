import os
from typing import Any, Union
# Linear Search : Brute force. Search one by one till you reach the item.


# Order of growth : O(n). No sorting required.
def linear_search(arr: list, value: Any) -> Union[int, None]:
    """Returns index of value if found """
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return None


#  Order of growth: O(log(n)). When input multiples, no of iterations for getting o/p only gets added. Sorted arr needed
def binary_search_through_iteration(arr: list[int], value: int) -> Union[int, None]:
    """The array passed should be sorted."""
    # We are search with respect to mid = (high + low)/2. high and low are index of the sub-list considered.
    # Note : while only low <= high then only remaining list is valid. if low>high means remaining list is invalid now,
    # thus item not found.
    low = 0  # initial low is 0th index - first index of list
    high = len(arr) - 1  # last index of the list

    # As long as sub-list is valid, the while loop continues.
    while low <= high:
        # mid is point of perspective, basically we compare with mid.
        mid = (high + low) // 2  # Floor division : gives quotient

        # As we keep narrowing down till one item remains to compare, if the value does exist eventually it will be
        # equal to mid(point of perspective).
        if value == arr[mid]:
            return mid
        elif value < arr[mid]:
            # If the value is less than mid, then the element is on the left side of list, thus high will be mid-1,
            # as we have already checked mid and it doesn't need to be included.
            high = mid - 1
        elif value > arr[mid]:
            # If the value is greater than mid, then the element is on the right side of list, thus low will be mid+1,
            # as we have already checked mid and it doesn't need to be included.
            low = mid + 1

    # If while searching list is invalid, meaning low > high, and we have searched all list then value not found.
    raise ValueError("Value not Found.")


# We are passing low and high as we don't want to redefine in the function as it will erase the prev values.
def binary_search_through_recursion(arr: list[int], value: int, low: int, high: int) -> Union[int, None]:

    if low <= high:
        mid = (low + high) // 2  # point of perspective

        if value == arr[mid]:
            # NOTE: ** Anything at any point of recursion that is returned, will be in return of all the higher
            # functions. Ex : return (return (return mid) ). It will be like this and thus mid or None will be returned.
            return mid
        elif value < arr[mid]:
            # If the value is less than mid, then the element is on the left side of list, thus high will be mid-1,
            # as we have already checked mid and it doesn't need to be included.
            # high = mid - 1. Call function with altered value of high
            return binary_search_through_recursion(arr, value, low, mid - 1)
        elif value > arr[mid]:
            # If the value is greater than mid, then the element is on the right side of list, thus low will be mid+1,
            # as we have already checked mid and it doesn't need to be included.
            # low = mid + 1
            return binary_search_through_recursion(arr, value, mid + 1, high)
    else:
        # returning value not found as soon as list is invalid : low > high
        return None


arr1 = [1, 2, 4, 5, 6, 7]
print(linear_search(arr1, 4))
print(binary_search_through_iteration(arr1, 1))
print(binary_search_through_recursion(arr1, 7, 0, (len(arr1) - 1)))


# Amortized Cost:
# If we included sorting + searching, then :
# linear search of non sorted arr is : O(n)
# binary search with sorting is : O(nlog(n)) + O(log(n))
# And thus for one search : linear search of non-sorted arr 'is better' binary search with sorting of non-sorted arr

# But in the case we need to search a lot, say K times, and k is a very big number then:
# binary search with sorting is : (1)*O(nlog(n)) + (K)*O(log(n)). Here we need to sort only once and thus it becomes,
# negligible time when we are searching a lot. thus
# binary search with sorting is : (K)*O(log(n))
# linear search of non sorted arr is : (K)*O(n)
# And thus for large no. of searched : binary search 'is better' linear search
