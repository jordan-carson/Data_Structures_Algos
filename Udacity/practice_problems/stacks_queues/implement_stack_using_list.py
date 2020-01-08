class Stack:
    def __init__(self):
        self.arr = [0] * 10
        self.next_index = None
        self.num_elements = len(self.arr)

    def push(self, data):
        if self.next_index == len(self.arr):
            print("Out of space! Increasing array capacity ...")
            self._handle_stack_capacity_full()
        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

    def _handle_stack_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(old_arr))]
        for idx, val in enumerate(old_arr):
            self.arr[idx] = val

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0