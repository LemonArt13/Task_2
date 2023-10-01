num = input("Введіть ціле число ")

if num.isdigit():
    num_str = str(num)

    for digit in num_str:
        k = int(digit)
        print("#"*k)
else:
    print("Введено не ціле число")