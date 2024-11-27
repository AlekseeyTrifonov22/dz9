def count_digits(n):
  if n == 0:
    return 1
  count = 0
  while n > 0:
    count += 1
    n //= 10
  return count
number = 56789
num_digits = count_digits(number)
print(f"Количество цифр в {number} равно: {num_digits}")
