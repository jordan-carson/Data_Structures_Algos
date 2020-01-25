
# Problem 4
### Blockchain


This was fun and interesting to see an actual use-case 
for LinkedList (especially in practice).

My answer contains a Block (or a Node class), and a Blockchain, which is
an implementation of a LinkedList. 

The add_block() method first created a new Block object (aka our Node), we then test
to see if our current block is empty, if it is we set both the head and tail to the new block.
Otherwise, we set the tail to the new_block and point it next to the head, also changing the
new_blocks previous hash from none to the current_nodes hash.

We are doign this in constant time as we are including a tail so we do not need
to traverse the time complexity is O(1).


The space complexity occupied by the block list in worst-case will be O(n),
where n is the number of blocks. 
