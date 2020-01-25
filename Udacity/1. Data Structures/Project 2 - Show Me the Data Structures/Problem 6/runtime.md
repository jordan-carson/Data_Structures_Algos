# Problem 6
### Union & Intersection


For the union I create a method within the LinkedList class to allow for an easily
implementation of performing this taks. I first loop through all items in the first
unsorted list, adding them to a set if its not already within it. Then I loop through
the second list and add all of the items that are not already within it. These are two separate
lists. I finally loop through the final set with the union elements and append them to our
LinkedList.
Time Complexity = T(n) = n + n + n
or **O(n)**
Space Completity is O(n) as we are creating a new linked list


The intersection loops through all the items in the first
list and appends the items to a new LinkedList if that item
is contained in the second LikedList. In this solutiomn we loop through
all the items of the first list and add them to a set. We then loop through all
the items into the second list and if an item exists in the first set, we append it to
a new linked list.

The time complexity is O(n + n) or O(n), and the space complexity is O(n) as we
are only creating one new list type structure. 
