def tower_of_Hanoi(num_disks):
    """
    :param: num_disks - number of disks
    """
    _tower_of_hanoi(num_disks, 'S', 'A', 'D')


def _tower_of_hanoi(num_disks, source, auxiliary, destination):
    final = []
    if num_disks == 0: return

    if num_disks == 1:
        # final.append([source, destination])
        print(f'Move disk 1 from {source} to {destination}')
        return

    _tower_of_hanoi(num_disks - 1, source, destination, auxiliary)
    # final.append([source, destination])
    print(f'Move disk {num_disks} from {source} to {destination}')
    _tower_of_hanoi(num_disks - 1, auxiliary, source, destination)


if __name__ == '__main__':

    print(tower_of_Hanoi(3))