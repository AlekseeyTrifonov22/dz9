def factorial(n):
  if n < 0:
    raise ValueError("Факториал не определен для отрицательных чисел.")
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)
number = int(input("Введите неотрицательное целое число: "))
print(f"Факториал от {number} равен {factorial(number)}.")
