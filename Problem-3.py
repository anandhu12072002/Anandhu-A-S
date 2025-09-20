def odd_print(n):
    num = 1
    for i in range(n):
        print(num, end=" ")
        num += 2

def even_print(n):
    num = 1
    for i in range(n-1):
        print(num, end = " ")
        num += 2

n = int(input("Enter a number : "))
if (n%2) != 0:
    odd_print(n)
else:
    even_print(n)