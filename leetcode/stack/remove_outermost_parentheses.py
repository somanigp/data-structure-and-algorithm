def remove_outer_parentheses(s: str) -> str:
    res, opened = [], 0
    # don't add outer parenthesis and you can track that by 'opened'
    for c in s:
        if c == '(' and opened > 0:
            res.append(c)
        if c == ')' and opened > 1:  # as bcuz of outermost '(', opened is 1
            res.append(c)
        opened += 1 if c == '(' else -1

    return "".join(res)


print(remove_outer_parentheses(s="(()())(())(()(()))"))
