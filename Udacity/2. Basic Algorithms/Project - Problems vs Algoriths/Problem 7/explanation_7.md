# Problem 7

This problem is very similar to 5, where instead of a Trie.is_word we have a Router.handler.
The handler acts the same as before, we traverse the entire string and store the handler at the end. 
I also, created some methods to clean and split our list, based on the requirements of the problem.

Time Complexity:
Find, Insert, Lookup, and Add_Handler methods are all O(n), as we need to iterate over each part
of the path to get the results for these methods.

Space Complexity:
The add_handler method requires us to create a new RouteTrieNode for each part of the path (parts, handler).
This method is O(n).

Insert method is the same as the add_handler method, as the add_handler calls the insert method.

The rest of the methods do not require any additional memory, thus the remaining methods happen in constant time
O(1).

