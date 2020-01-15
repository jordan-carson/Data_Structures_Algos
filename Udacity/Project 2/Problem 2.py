# Your work here
import os


def find_files(suffix, path):
    if not os.path.isdir(path): raise ValueError('Not a valid path')

    output = list()

    for child in os.listdir(path):
        child_path = os.path.join(path, child)

        if os.path.isfile(child_path) and child_path.endswith(suffix):
            output.append(child_path)

        if os.path.isdir(child_path):
            output.extend(find_files(suffix, child_path))  # recursive
    return output


if __name__ == '__main__':
    print(find_files('.py', os.pardir))