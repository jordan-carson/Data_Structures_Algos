import hashlib
import datetime
import os
import time
from typing import Union, AnyStr

class Block:

    def __init__(self, timestamp, #: Union[time.struct_time, datetime.datetime, datetime.date, AnyStr],
                        data, previous_hash,
                 **kwargs):

        #  Instance Attributes
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self._calculate_hash()
        self.debug = kwargs.get('debug', False)
        # os.makedirs(os.path.join(os.pardir, self.__class__.__name__), exist_ok=True)
        # self.__str__()
        self.next = None

    def _calculate_hash(self):
        """
        Function to calculate a sha256 hash, and update the hash with the data contained within our object,
            data, timestamp, and previous hash.
        :return:
        """
        sha = hashlib.sha256()
        # sha.update(self.data.encode('utf-8'))
        sha.update(str(self.data).encode('utf-8'))
        sha.update(self.timestamp.isoformat().encode('utf-8')) # converts data type to string
        if self.previous_hash: sha.update(str(self.previous_hash).encode('utf-8')) # make sure its a string
        # if self.previous_hash: sha.update(self.previous_hash.encode('utf-8'))
        return sha.hexdigest()

    def __str__(self):
        return (
            f'Data:\n\t {self.data}\n'
            f'Timestamp:\n\t {self.timestamp.isoformat()}\n'
            f'Hash:\n\t {self.hash}\n'
            f'Previous Hash:\n\t {self.previous_hash}\n'
        )


class Blockchain:
    """
    A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information
    of how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash
    of the previous block, a timestamp, and transactional data.
    """
    def __init__(self):
        self.current_block = None
        self.blocks = list()
        self.num_blocks = 0

    def __len__(self):
        return max(len(self.blocks), self.num_blocks)

    def __repr__(self):
        output = ''
        for idx, block in enumerate(self.blocks):
            output += f'Block {idx}'.center(70, '*') + '\n'
            output += str(block)
        return output

    def __iter__(self):
        current_block = self.current_block
        while current_block:
            yield current_block
            current_block = current_block.next

    def add_block(self, data):
        """
        Function / Method to add a new 'Block' object into our 'Blockchain'.
        This method will first create a new 'Block' object then it will add the block into our LinkedList.

        Remember to set the previous_hash

        Args:
            Data
        """
        new_block = Block(timestamp=datetime.datetime.utcnow(),
                          data=data,
                          previous_hash=None) # this is handled below

        if self.current_block is None:
            self.current_block = new_block
            self.num_blocks += 1
            self.blocks.append(new_block)
            return

        node = self.current_block
        while node.next:
            node = node.next

        # must change the set the previous hash of the new black equal to the current_blocks
        new_block.previous_hash = node.hash
        node.next = new_block
        self.num_blocks += 1
        self.blocks.append(new_block)

    def to_list(self):
        # new_list = list()
        # current_node = self.current_block
        # while current_node:
        #     new_list.append(current_node)
        #     current_node = current_node.next
        return self.blocks

    def search(self, hash):
        for block in self:
            if block.hash == hash:
                return block
        # return "Block Not Found"
        return -1


if __name__ == '__main__':
    chain = Blockchain()
    chain.add_block('This is a block')
    chain.add_block('This is another block')
    chain.add_block('This block is more important')

    print(chain)

    # print a list of block objects
    print(chain.blocks)

    # test the number of blocks is what we expect
    assert len(chain.blocks) == chain.num_blocks

    print(chain.search('bb46fc71124bb28472c09606096e9777eb72ac7786b4963dbd0548eb9dd0164e'))
