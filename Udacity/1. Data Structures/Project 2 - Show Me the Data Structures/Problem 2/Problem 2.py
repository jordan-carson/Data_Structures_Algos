import os


def find_files(suffix, path):
    # If its not a directory return
    if os.path.isfile(path) and path.endswith(suffix):
        return path

    if not os.path.isdir(path) or not path:
        raise ValueError('Not a valid path')
        # return []
    output = list()
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            # extend the list to search down the child path
            output.extend(find_files(suffix, child_path))
        elif os.path.isfile(child_path) and child_path.endswith(suffix): # and os.path.join(path, child).endswith(suffix):
            # if its a file and the file matches our suffix add it to our list
            output.append(child_path)
    return output


if __name__ == '__main__':
    print('Test 1')
    print(find_files('.c', r'D:\DeepLearning\data_structures_algos\Project 2\Problem 2\testdir'))

    print('Test 2')
    print(find_files('.py', r'D:\DeepLearning\data_structures_algos\Project 2\Problem 2\testdir'))

    print('Test 3')
    print(find_files('.h', r'D:\DeepLearning\data_structures_algos\Project 2\Problem 2\testdir'))

    print('Test 4 - Edge case')
    print(find_files('', r'D:\DeepLearning\data_structures_algos\Project 2\Problem 2\testdir'))

    print('Test 5 - Edge case')
    print(find_files('', ''))