# Shortest Path Problem

Finding the shortest path in a graph. In a graph each edge can have a weight, these are called **weighted edges**,
where the edges in a graph have some numerical value associated with them. 

The shortest path is the one where the sum of the edges is as small as possible. If we had an unweighted graph,
the shortest path would just be the one with the fewest number of edges. 

The nature of the solution to this problem changes a lot depending on the type of graph. For example, 
the solution to the shortest path for an unweighted graph is actually just a **breath-first search (BFS)**,
with a BFS you start at one node and visit the closest nodes first, slowly moving out to more distant nodes
until you find the one that you were looking for. Remember with no weights, the shortest path is the 
one with the least number of edges. 

## Dijkstra's Algorithm

One solution to the shortest path problem for weighted undirected graphs is called **Dijkstra's Algorithm**.

The distance value we start with is infinity, which is a placeholder value that will update
whenever we discover a node and have an actual distance to store. The node we're starting with 
will have a distance of zero. A common implementation of dijkstra's uses a min priority queue, where the element
with a minimum priority, or minimum distance in our case, can be removed efficiently. 

We store all of our nodes in the priority queue and use `extract min` to take out the minimum element the only one with 
a distance of zero. 

From our starting node we have several options. We will follow each edge and update the node on the other
side a distance value, which is just the weight of the edge. Next we are faced with a choice, 
which node should we visit? We'll always pick the node with the smallest distance value, which 
means we run `extract_min` on the queue. 

Because we always pick the node with the lowest distance, dijkstra's algorithms is often called a
**greedy algorithm**. The philosophy for these algorithms are pick whatever option looks best at the moment, 
hence the name greedy. 

We repeat the process visiting all adjacent nodes that are still in the queue and updating
their distance values if we can decrease it at all. We keep going, extracting the minimum from 
our queue and exploring adjacent elements, until the node we're looking for has been extracted from the
queue or everything else has a distance of infinity, which means the path we're looking for doesn't exist.

The basic runtime of dijkstra's is the number of vertices squared. 
O(|V|^2)

Since in the worst case, we visit every node in the graph once or twice and every time we visit we need to search
through the queue to find the minimum element. 

There are a lot of optimizations for dijkstra's, if the priority queue is implemented really efficiently, 
the runtime looks more like O(|E| + |V| log (|V|)).
