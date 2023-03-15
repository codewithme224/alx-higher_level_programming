#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum = 0
    sum_weight = 0
    for tup in my_list:
        sum += tup[0] * tup[1]
        sum_weight += tup[1]
    return (sum / sum_weight)
