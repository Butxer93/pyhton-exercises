num_list = range(1, 11)
cubed_nums = []

for num in num_list:
  cubed_nums.append(num ** 3)
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

cubed_nums = [num ** 3 for num in num_list]

print(cubed_nums)
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

even_numbers = []

for num in num_list:
  if num % 2 == 0:
    even_numbers.append(num)
# [2, 4, 6, 8, 10]

even_numbers = [num for num in num_list if num % 2 == 0]

print(even_numbers)
# [2, 4, 6, 8, 10]