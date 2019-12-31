
def find_busiest_period(data):
    """
    Aggregate number of visitors at each time stamp,
    return the largest

    O(n) time
    O(n) space

    Every time we update the timestamp aggregate # visitors, we compare versus the max

    [ [1487799425, 14, 1],
     [1487799425, 4,  0],
     [1487799425, 2,  0],
     [1487800378, 10, 1],
     [1487801478, 18, 0],
     [1487801478, 18, 1],
     [1487901013, 1,  0],
     [1487901211, 7,  1],
     [1487901211, 7,  0] ]

    :param data:
    :return:
    """
    # initial conditions
    max_timestamp = data[0][0]
    max_visitors = 0

    timestamp_map = {}

    # AGGREGATION STEP
    # iterate thru data to access each point individually
    for datum in data:
        timestamp, visitors, entry = datum
        entry = -1 if entry == 0 else 1  # use entry to signify sign
        # update the timestamp map, which is the aggregation
        timestamp_map[timestamp] = timestamp_map.get(timestamp, 0) + entry * visitors
        if timestamp_map[timestamp] > max_visitors:
            max_timestamp = timestamp
            max_visitors = visitors

    return max_timestamp
