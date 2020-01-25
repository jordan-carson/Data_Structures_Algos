# Problem 2
### Find Files

Given we do not know how many files and directories we are going to be searching for, 
recursion is a fantastic way of solving the problem.

I decided to use the os (operating system) library which comes as part
of the Python Standard Library, as it has some easy to use file functions. 

### Our Explanation
We loop through all the specified path, we then determine
if the child paths are directories or files. If they are directories, we continue our recursion, otherwise we test
to determine if the files match our suffix. If it does, we add it to our list. 


### Complexities 
The time complexity is O(n), where n is the number of files in the parent directory, and subsequent directories, files etc.
Separately, the space complexity is O(n), as we create a variable to hold the files that match the suffix. 

The call stack in this example would make the first call to the path directory, then 
would call the child_path subdir1, and process would repeat to the numbers of subdirectories within a path.

Thus the space complexity, is based on the number of files and directories in the path variable.
In the worst-case this would be O(n).

__Note:__ We can mitigate the recursion limit by setting

```python
import sys
sys.setrecursionlimit(100)
``` 