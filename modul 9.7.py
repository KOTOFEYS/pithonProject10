def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        number_of_divisors = 0
        for i in range(2,result):
            if (result % i == 0):
                number_of_divisors += 1
        if number_of_divisors <=0:
            print('простое')
        else:
            print('составное')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)
