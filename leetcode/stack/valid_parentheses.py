def is_valid(s: str) -> bool:  # when you need to define what a function is expected to return
    dict_of_items = {")": "(", "]": "[", "}": "{"}  # to store equivalent opening values
    result_list = []  # Using a list as a stack
    for char in s:
        if char in "([{":  # use this way for checking, keep adding to the list
            result_list.append(char)
        else:
            if len(result_list) == 0:  # if extra closing bracket is there, it will be detected.
                return False
            char_opening_value = result_list.pop()  # removes the last element and returns it.
            # NOTE: last ele removed should be char_opening_value,
            # thus a pair will be formed, and it will be a valid syntax.
            if char_opening_value != dict_of_items[char]:  # If a proper pair is not formed.
                return False
    return len(result_list) == 0  # only if all openings and closing are sorted,
    # thus a list is empty then only return true


print(is_valid("[]{()}"))   # True
print(is_valid("[{]}"))  # False

# NOTE : [{]} - this is invalid, as '{' should close first before closing '['. Thus using stack is optimum is

# Explanation: If the current character is a closing bracket (i.e., ')', '}', ']'), check if the stack is empty.
# If it is empty, return false, because the closing bracket does not have a corresponding opening bracket. Otherwise,
# pop the top element from the stack and check if it matches the current closing bracket. If it does not match,
# return false, because the brackets are not valid.

# Time complexity: O(n)
# The space complexity of the solution is O(n), where n is the length of the input string. This is because the
# worst-case scenario is when all opening brackets are present in the string and the stack will have to store them all.

# Hints :
empty_list = []
print(not empty_list)  # not list returns True if a list is empty
