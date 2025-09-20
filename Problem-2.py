def generate_series(n):
    num = 1
    for i in range(n):
        print(num, end = " ")
        num += 2

num = int(input("Enter a number : "))
generate_series(num)