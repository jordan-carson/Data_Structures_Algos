# Graphs

Can be thought of as a collection of objects where each object is called a node or vertex,
and the links between them is an edge. Both edges and nodes can contain data.

Graphs can have a **direction**, where A points to B, this would be called a **Directed Graph**.

Graphs can also have **cycles**, while Trees cannot. Trees can be thought of as a special type
of graph. A cycle happens in a graph when you can start at one node and follow edges all the way
back to that node. This is called a cyclic graph, and can have infinite loops!

We often need to make sure that the graph your taking in as input is **acyclic**, means it has no cycles. 
One type of graph that shows up often is a DAG, or a directed, acyclic graph. 

Graphs can also have **connectivity**. A disconnected graph has some vertex that cannot be reached
by the other vertices. It could also have two so-called connected components, which are
connected graphs on their own but have no connection between them. Thus, a connected graph
has no disconnected vertices. There's also a metric used to describe a graph as a whole called
connectivity, which measures the minimum number of elements that need to be removed for a graph to 
become disconnected. We can sometimes use connectivity to determine which graph is stronger.

We can create Vertex and Edge objects, give them each properties like name, strength, id, number, 
using object-oriented programming. We can build graphs using lists, dictionaries, adjacency matrices.

Graphs are fantastic for modelling connections between elements, and are very easy to traverse
based on connections. We have two primary methods for traversing a graph, **depth-first search**,
where we follow one path as far as it'll go, and a **breadth-first search**, where we look at all
the nodes adjacent to one before moving on to the next level.

### Depth-First Search

DFS on graphs operates under the same principles as DFS on trees. Unlike a tree, there's no 
root in a graph, so you can begin with any node. First mark the node you selected as visited (seen),
then we pick an edge, follow it, mark that node as visited and add it to the stack. We keep repeating these
steps, when you see a node that has been visited just go back to the previous node and try another edge. 
If you run out of edges with new nodes, you pop the current node from the stack and go back to the one
before it, which is just the next one on the stack. We continue this approach until you've popped everything off the,
stack or you find the node you were originally looking for. We can solve this using recursion, instead of using
a stack. This time complexity implementation is O(|E| + |V|), the number of edges plus
the number of vertices. We actually visit every edge twice, once to explore it
and once traveling back through it. The V is added to account for the time taken
to look up a vertex. 

### Breath-First Search

BFS is quite similar, but here you search every edge of one node before continuing on with the graph.
We first start at a node, we mark that off as visited, and add it to our queue. 
Recall the difference between a queue and a stack. For a queue, we'll remove the first
element we put in it, but for a stack we remove the most recently added element. 
We go back to the first node and visit everything adjacent to it, marking each as
seen and adding them to a queue. When we've run out of edges we can just dequeue a node
from the queue and use that as our starting place. We look at every node adjacent to that
one, and adding each one to the stack until we've exhausted our options. It's important
to note that when we dequeue, 