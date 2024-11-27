def sum_even_numbers(n):
  sum = 0
  for i in range(2, n + 1, 2):
    sum += i
  return sum
n = int(input("Введите число N: "))
sum_even = sum_even_numbers(n)
print(f"Вывод: {sum_even}")
