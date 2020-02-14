# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24, 13), (21, 55), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3)]


def bubble_sort_2(l):
    for i in range(len(l)):
        for j in range(1, len(l)):
            this_hour, this_min = l[j]
            prev_hour, prev_min = l[j - 1]
            if this_hour < prev_hour or (prev_hour == this_hour and prev_min > this_min):
                continue
            l[j], l[j - 1] = (prev_hour, prev_min), (this_hour, this_min)
    return l


bubble_sort_2(sleep_times)
print("Pass" if (sleep_times == [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)]) else "Fail")

