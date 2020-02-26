# Problem 5

This problem required us to create a Trie Data structure, using a defaultdict to store
the children. 

Time Complexity:
All methods, such as Find, Insert, Suffixes, does_word_exist() are all Linear time algorithms
as each character needs to be iterated over to find, insert or create the suffixes. 

Space Complexity:
Find and Suffix Methods happen in O(1) as no memory is allocated,
while Insert requires O(n) as we have to insert all of the characters from the input string/list.