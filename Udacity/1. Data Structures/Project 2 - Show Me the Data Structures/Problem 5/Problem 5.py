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
        self.tail = None
        self.blocks = list()
        self.num_blocks = 0

    def __len__(self):
        return max(len(self.blocks), self.num_blocks)

    def __repr__(self):
        if self.num_blocks == 0:
            print('*'.center(75, '*'))
            print(
                'Blochain Empty!')
            print('*'.center(75, '*'))
        output = ''
        for idx, block in enumerate(self.blocks):
            output += f'Block {idx}'.center(70, '*') + '\n'
            output += str(block)
        return output

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
                          previous_hash=None) # t

        if self.current_block is None:
            self.current_block, self.tail = new_block, new_block
            # self.tail = new_block
            self.num_blocks += 1
            self.blocks.append(new_block)
            return
        else:
            self.tail = new_block
            new_block.next = self.current_block
            new_block.previous_hash = self.current_block.hash
            self.num_blocks += 1
            self.blocks.append(new_block)

    def to_list(self):
        # new_list = list()
        # current_node = self.current_block
        # while current_node:
        #     new_list.append(current_node)
        return self.blocks


if __name__ == '__main__':
    chain1 = Blockchain()
    chain1.add_block('This is a block')
    # print(chain)
    chain1.add_block('This is another block')
    # print(chain)
    chain1.add_block('Third block First Chain')
    print(chain1)

    chain2 = Blockchain()
    chain2.add_block('This is a block')
    # print(chain)
    chain2.add_block('This is another block')
    # print(chain)
    chain2.add_block('Third block Second Chain')
    print(chain2)

    chain3 = Blockchain()
    print(chain3)
    # chain3.add_block()
    # print(chain)
    chain3.add_block('')
    # print(chain)
    chain3.add_block('Third block, is this the last chain?')
    print(chain3)

    chain4 = Blockchain()
    print(chain4) # Empty Blockchain
    chain4.add_block('yellow data')
    print(chain4)


