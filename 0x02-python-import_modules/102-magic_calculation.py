#!/usr/bin/python3
def magic_calculation(a, b):
    if a < b:
        add = __import__('magic_calculation_102', globals(), locals(), ['add'], 0).add
        sub = __import__('magic_calculation_102', globals(), locals(), ['sub'], 0).sub

        c = add(a, b)

        for i in range(4, 7):
            c = add(c, i)

        return c
    else:
        return __import__('magic_calculation_102', globals(), locals(), ['sub'], 0).sub(a, b)
