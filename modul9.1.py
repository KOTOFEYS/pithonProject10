def apply_all_func(int_list, *functions):
    result = {}
    for i in functions:
        if i == max:
            result[max.__name__] = max(int_list)
        elif i == min:
            result[min.__name__] = min(int_list)
            return result
        elif i == len:
            result[len.__name__] = len(int_list)
        elif i == sum:
            result[sum.__name__] = sum(int_list)
        elif i == sorted:
            result[sorted.__name__] = sorted(int_list)
            return result

print(apply_all_func([6, 20, 15, 9], max, min), end = ' ')
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))