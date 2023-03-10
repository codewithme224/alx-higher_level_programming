#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        result = add(a, b)
        for i in range(2, 4):
            result = add(result, i)
        return (result)
    else:
        return(sub(a, b))
