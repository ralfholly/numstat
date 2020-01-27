#!/usr/bin/env python3

import math

def main():
    inp_values = []
    while True:
        try:
            num = input()
            try:
                num = float(num)
            except ValueError:
                continue
            inp_values.append(num)
        except EOFError:
            break

    if inp_values:
        max_num = max_of(inp_values)
        min_num = min_of(inp_values)
        sum_num = sum_of(inp_values)
        avg_num = sum_num / len(inp_values)
        median_num = median_of(inp_values)
        stddev_num = standard_deviation(sum_of_squared_deltas_of(inp_values, avg_num), len(inp_values))
        sep = ', '
        print_value('count:', '%d', sep, len(inp_values))
        print_value('min:', '%g', sep, min_num)
        print_value('max:', '%g', sep, max_num)
        print_value('sum:', '%g', sep, sum_num)
        print_value('median:', '%g', sep, median_num)
        print_value('average:', '%g', sep, avg_num)
        print_value('stddev:', '%g', sep, stddev_num)
        print()
    else:
        print("No valid input found.")

def max_of(values):
    return max(values)

def min_of(values):
    return min(values)

def sum_of(values):
    return sum(values)

def sum_of_squared_deltas_of(values, average):
    squared_sum = dist = 0
    for value in values:
        dist = value - average
        squared_sum += dist * dist
    return squared_sum

def median_of(values):
    sorted_values = sorted(values)
    if len(sorted_values) % 2 == 0:
        mid = len(sorted_values) // 2
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2.0
    return sorted_values[mid]

def variance(squared_deltas_sum, count):
    return squared_deltas_sum / count

def standard_deviation(squared_deltas_sum, count):
    if count >= 1 and squared_deltas_sum >= 0:
        return math.sqrt(squared_deltas_sum / (count - 1))
    return 0

def print_value(title, fmt_spec, separator, value):
    print((title + fmt_spec + separator) % + value, end='')

####

if __name__ == '__main__':
    main()
