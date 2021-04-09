
def is_divides(number, divider=7):
    if number%divider == 0:
        return True
    else:
        return False


def fig_sum(number):
    result = 0
    base = 10
    digit = 0
    while number//(base ** digit) != 0:
        result += (number % (base ** (digit + 1))) // (base ** digit)
        digit += 1
    return result


# Задание а)


odd_cubes = []
for num in range(1, 1000, 2):
    odd_cubes.append(num ** 3)
print(odd_cubes)
cubes_sum = 0
for num in odd_cubes:
    if is_divides(fig_sum(num)):
        cubes_sum += num
print(cubes_sum)

# Задание b)

odd_cubes_mod = []
for num in odd_cubes:
    num += 17
    odd_cubes_mod.append(num)
cubes_sum = 0
print(odd_cubes_mod)
for num in odd_cubes_mod:
    if is_divides(fig_sum(num)):
        cubes_sum += num
print(cubes_sum)

# Задание c)
cubes_sum = 0
for i in range(len(odd_cubes)):
    odd_cubes[i] += 17
    if is_divides(fig_sum(odd_cubes[i])):
        cubes_sum += odd_cubes[i]
print(odd_cubes)
print(cubes_sum)