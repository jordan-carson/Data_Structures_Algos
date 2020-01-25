# Problem 3
### Huffman Coding Tree

This was by far the most difficult problem in this project.
We create several functions to help us get to the results. 
The time complexity for the huffman_encoding() algorithm:

#### Time Complexity Calculations
- HuffmanCoding()._create_frequencies() 
    - O(n)
- HuffmanCoding()._sort_frequencies() 
    - O(n)
- HuffmanCoding().create_merged_trie() 
    - O(n * log n)
    - We pop twice for every call
    - We also call sort_frequencies within the while loop, which causes this to n * log n
- HuffmanCoding().create_encoding_dict() 
    - O(n)

1. T(n) = (n + n + n) * (log n)
2. T(n) = (3n) * (n * log n) 
3. T(n) = n * n * log n
4. T(n) = O(n * n log(n))

### Space Complexities
- HuffmanCoding()._create_frequencies() 
    - We create a dict which is as large as the number of keys (each string) in the data
    - O(n)
- HuffmanCoding()._sort_frequencies() 
    - O(n), sorting a list
- HuffmanCoding().create_merged_trie() 
    - We create a frequencies list, and remove and append
    - O(n)
- HuffmanCoding().create_encoding_dict() 
    - Here we are recursively creating a dictionary, going through both the left and
    - right parts of the tree. Thus the space complexity will be O(n).


The huffman_decoding() function has a time complexity of O(n) and a space complexity of O(1).
We are looping through each character of the encoded_text variable.

The huffman_encoding() function has a time complexity of O(n * n log n) + O(n) + O(n),
which reduces to O(nn log n).
