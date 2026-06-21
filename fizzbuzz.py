number = 50

fizz_list = []
buzz_list = []
fizzbuzz_list = []

# loop through the number
for num in range(1, number + 1):
    divisible_by_3 = num % 3 == 0
    divisible_by_5 = num % 5 == 0

    if divisible_by_3 and divisible_by_5:
        print("fizzbuzz")
        fizzbuzz_list.append(num)
    elif divisible_by_3:
        print("fizz")
    elif divisible_by_5:
        print("buzz")
    else:
        print(num)

    if divisible_by_3:
        fizz_list.append(num)
    if divisible_by_5:
        buzz_list.append(num)

print(f"There are {len(fizz_list)} numbers divisible by 3 and they are: {fizz_list}")
print(f"There are {len(buzz_list)} numbers divisible by 5 and they are: {buzz_list}")
print(
    f"There are {len(fizzbuzz_list)} numbers divisible by 3 abd 5 and they are: {fizzbuzz_list}"
)
