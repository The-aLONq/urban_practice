def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        result = function(int_list)
        results[function.__name__] = result

    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
