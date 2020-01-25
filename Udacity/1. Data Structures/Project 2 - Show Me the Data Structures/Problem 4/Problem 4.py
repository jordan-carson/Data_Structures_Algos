

class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups, self.users = list(), list()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


if __name__ == '__main__':
    print('Test Case 1')
    parent = Group('parent')
    child = Group('child')
    sub_child = Group('subchild')

    sub_child_user = 'sub_child_user'
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

        # return [is_user_in_group(user, subgroup) for subgroup in group.groups][0]
    def is_user_in_group(user, group):
        if not user:
            print('No user to look for!')
            return False
        if not isinstance(group, Group):
            print('Invalid group!')
            return False
        if user in group.users:
            return True
        if len(group.groups) == 0:
            return False
        for sub_group in group.groups:
            return is_user_in_group(user, sub_group)


    print('Pass' if not (is_user_in_group(parent, child) == True) else 'Fail')
    print('Pass' if is_user_in_group('sub_child_user', sub_child) else 'Fail') # --> True
    print('Test Case 2')
    grand_parent = Group('grand_parent')
    parent = Group('parent')
    child = Group('child')

    sub_child_user = 'sub_child_user'
    grand_parent.add_user('Joseph')
    grand_parent.add_user('Greg')

    parent.add_user('Mike')
    parent.add_user('Jeff')

    grand_parent.add_group(parent)
    parent.add_group(child)

    print('Pass' if not is_user_in_group(grand_parent, child) else 'Fail')

    print('Test Case 3')

    parent = Group('parent')
    cousin = Group('cousin')
    child = Group('child')

    sub_child_user = 'sub_child_user'
    child.add_user(sub_child_user)
    cousin.add_user('Greg')

    parent.add_user('Mike')
    parent.add_user('Jeff')

    parent.add_group(child)
    child.add_group(parent)

    print('Pass' if is_user_in_group('Mike', parent) else 'Fail')
    print('Pass' if is_user_in_group('Jeff', parent) else 'Fail')
    print('Pass' if is_user_in_group('Jeff', child) else 'Fail')
    print('Pass' if is_user_in_group('Greg', cousin) else 'Fail')