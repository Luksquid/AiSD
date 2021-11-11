# 1
# def numbers(n: int) -> int:
#     print(n)
#     if(n==0):
#         return 1
#     return numbers(n-1)
#
# numbers(10)

# 2
# def fib(n: int):
#     if(n==1 or n==0):
#         return 1
#     return fib(n-1) + fib(n-2)
# for i in range(10):
#     print(fib(i))

# 3
# def power(number: int, n: int) -> int:
#     if(n==1):
#         return number
#     return power(number, n-1) * number
# print(power(2,3))

# 4
# def reverse(txt: str) -> str:
#     return txt[::-1]

# 5
# def factorial(n: int) -> int:
#     if(n==1):
#         return 1
#     return factorial(n-1) + n
# print(factorial(4))

# 6
# def prime(n: int, p: int) -> bool:
#     if(n<p):
#         return n;
#     for i in range(1, n-1):
#         if(n % prime(n-i, p)==0):
#             return False
#     return True
# print(prime(6, 6))

# 7
def n_sums(n: int) -> list[int]:
    lista = []
    temp2 = 0
    while (len(str(temp2)) < n):
        temp = str(n)
        par = 0
        npar = 0
        for i in range(len(temp)):
            if (i % 2 == 0):
                par = par + int(temp[i])
            else:
                npar = npar + int(temp[i])
        if (par == npar):
            lista.append(str(n))
        temp2 = temp2 + 1

