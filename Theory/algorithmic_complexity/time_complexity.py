
# Measured time will change depending on the server.
import time
# time.sleep(1) # Adds delay
start = time.time()  # Return the current time in seconds since the Epoch. Returns float
for i in range(1, 100000):
    # print(i)
    continue

print(time.time() - start)  # Current time - Start Time

# Operation Involved: if and while can show different time taken even after same logic behind them.

# Counting Operations: x=5, x+1, x+=1 (2 Ops here), etc are all operations, thus calculating no of operations.
# This still gives the issue of operations involved above.

# Order of Growth: evaluate algo, evaluate scalability and evaluate in terms of input size.
# Best case, worst case and average case. Focus on Worst case.


def int_to_str(x: int) -> str:  # O(log(n)) -> as input increase 10x and no. of loop increases by 1
    digits = '0123456789'
    result = ''
    while x > 0:
        result = digits[x % 10] + result
        x = x // 10  # Gives back the quotient. 9 // 10 = 0, 90 // 10 = 9
    return result

# For 1000->4 loops, 100-> 3 loops, 10 -> 2 loops, etc. Thus log(n)
# Generally for division it could be log. Also, when input multiplies and output adds -> log


n = 100
for i in range(int(n/2), n):  # This is O(n/2)
    j = 2  # for(j=2;j<n;j=j*2)
    while j < n:  # 36 to 39 is log(n). If n = 10 , loop is for j=2,4,8
                                        #  n = 100, loop is for j = 2,4,8,16,32,64 , Thus add by 3
                                        # n = 1000, loop is for j = 2,4,8,16,32,64,124,256,512 , Thus add by 3
                                        # Thua when input multiplies and output adds -> log
        print('Hi')
        j *= 2
# Thus O(n/2)*O(log(n)) is O(nlog(n))


# n! -> Factorial of n
def factorial(k):  # For k=5, 5 function calls are made, for k=10, 10 function calls are made thus its O(n) -> Linear
    """Factorial."""
    if k == 1:
        return 1
    else:
        return k * factorial(k-1)


# 1.7^n is the order of growth
# This is assuming it starts from 1 1 2 3 5 ...
def fib(num):  # less than O(2^n) -> Imperfect exponential. It is opposite of log as input adds then operations multiply
    if num == 1 or num == 0:
        return 1
    else:
        return fib(num-1) + fib(num-2)

# input : 1 -> function calls : 1
# input : 2 -> function calls : 2
# input : 3 -> function calls : 4
# input : 5 -> function calls : 14
# input : 6 -> function calls : 32

# Aritmatic Operation : Constant time O(1)

