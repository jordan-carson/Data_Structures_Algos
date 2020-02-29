import collections

Item = collections.namedtuple('Item', ['weight', 'value'])


def max_value(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack.
    """
    memory = [0] * (knapsack_max_weight + 1)
    for item in items: # do not forget to loop through the items!
        for capacity in reversed(range(knapsack_max_weight +1)):
            if item.weight <= capacity:
                memory[capacity] = max(memory[capacity], memory[capacity - item.weight] + item.value)
#             print(capacity)
#     print(memory)
    return memory[-1]


tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
for test in tests:
    assert test['correct_output'] == max_value(**test['input'])


