def reverse_digits(number):
  reversed_number = 0
  while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
  return reversed_number
number = int(input("Введите число: "))
reversed_number = reverse_digits(number)
print(f"Обратное число равно: {reversed_number}")
