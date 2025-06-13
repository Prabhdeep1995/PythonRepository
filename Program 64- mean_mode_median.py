# mean mode median

import statistics

def mean_median_mode(list1):
    return statistics.mean(list1),statistics.mode(list1),statistics.median(list1)


# assigning in different different variables
a,b,c = mean_median_mode([2, 4, 3, 5, 6, 7])
print(f"Mean is {a}, Median is {b}, Mode is {c}")