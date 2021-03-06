# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence that do not exceed the nth term, find the sum of the even-valued terms.
# fiboEvenSum(10) should return 44.
# fiboEvenSum(18) should return 3382.
# fiboEvenSum(23) should return 60696.
# fiboEvenSum(43) should return 350704366.

even_values = []


def list_sum(list_sum):
    even_sum = 0
    for i in range(len(even_values)):
        # print(even_values[i])
        even_sum = even_sum + even_values[i]

    print(even_sum)


def fibonacciSeries(n, memo):
    if n == 0 or n == 1:
        memo[n] = n

    if memo[n] is None:
        memo[n] = fibonacciSeries(n - 1, memo) + fibonacciSeries(n - 2, memo)
        # print(memo[n], end=",")
        if memo[n] % 2 == 0:
            # print(memo[n], end=",")
            even_values.append(memo[n])

    return memo[n]


n = 43
memo = [None] * (n + 1)
print("sum of even fibonacci numbers: ", end="")
fibonacciSeries(n, memo)
list_sum(even_values)
