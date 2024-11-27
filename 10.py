def sum_digits(n):
  sum = 0
  while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
  return sum
n = 123
sum_of_digits = sum_digits(n)
print(f"Сумма цифр из {n} равно: {sum_of_digits}")
