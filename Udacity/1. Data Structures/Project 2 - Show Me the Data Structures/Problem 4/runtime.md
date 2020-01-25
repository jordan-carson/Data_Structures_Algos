# Problem 4
### Users / Groups

We are using recursion to solve this problem, because we are unsure how many 
groups we will have to search through. 

Here the time complexity is O(n), as we are looping through only one group.groups to find all subgroups. 

Here given we are using a recursive solution, our call stack space
increases based on the number of times out function is called. So the space would be

The call stack would first call our main program is_user_in_group(user, group), then 
call the program based on the number of subgroups within the group.


On each recursive call the groups are added on the call stack, 
which is O(n) where n is the number of groups below the group to be explored


The class returns group.groups and group.users which are two lists encapsulated
within the class. The space consumed is based on the number of users and number of groups.
