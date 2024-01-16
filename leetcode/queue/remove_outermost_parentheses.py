from collections import deque


def remove_outer_parentheses(s: str) -> str:
    queue = deque([])  # Creating a Queue
    i = 0  # pos to track outer parenthesis
    result_string = ""
    for char in s:
        if char == "(":
            queue.append(char)
            i += 1
        else:
            if i == 1:  # when there is a ")" for pos 1 meaning outer parenthesis is closing
                queue.popleft()
                result_string += "".join(queue)  # as queue only can popleft thus cant pop the second outer parenthesis
                # as such, we add items inside the first outer parenthesis inside the result_string
                # and clear the queue and start again
                queue.clear()
            else:
                queue.append(char)
            i -= 1
    return result_string


print(remove_outer_parentheses(s="(()())(())(()(()))"))
