def is_prime(func):
    def wrapper(*numbers):
        number = func(*numbers)
        if number < 2:
            print('Составное')
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                print('Составное')
            else:
                print('Простое')
            break
        return number
    return wrapper

@is_prime
def sum_three(*numbers):
    sum_numbers = sum(numbers)
    return sum_numbers


result = sum_three(2, 3, 6)
print(result)