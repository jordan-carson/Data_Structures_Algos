

def compute_depth(n):
    multiple = 1
    depth = 0
    depth_reached = False
    depth_set = set()
    while n:
        value = n * multiple
        for val in str(value):
            if val not in depth_set:
                depth_set.add(int(val))
        multiple += 1
        depth += 1
        if len(depth_set) == 10:
            break
    return depth


def compute_depth_theirs(n):
    i = 0
    digits = set()
    while len(digits) < 10:
        i += 1
        digits.update(str(n * i))
    return i

print(compute_depth(42)) # should equal 9