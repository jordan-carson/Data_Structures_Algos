from collections import defaultdict

# RouteTrie.handler is similar to Trie.is_word


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root_node = RouteTrieNode(handler)

    def insert(self, parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root_node
        for part in parts:
            current_node.insert(part)
            current_node = current_node.children[part]
        current_node.handler = handler

    def find(self, parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root_node
        for part in parts:
            if part in current_node.children:
                current_node = current_node.children[part]
            else:
                return None
        return current_node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = defaultdict(RouteTrieNode)

    def insert(self, node):
        # Insert the node as before
        self.children[node] = RouteTrieNode()


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler, not_found_handler=None):
        self.route_trie = RouteTrie(handler=handler)
        self.not_found_handler = not_found_handler
    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!

    def add_handler(self, path, handler):
        parts = self.split_path(path)
        self.route_trie.insert(parts, handler)
        # DONE: Add a handler for a path
        # DONE: You will need to split the path and pass the pass parts
        # DONE: as a list to the RouteTrie

    def lookup(self, path):
        # first split the path
        parts = self.split_path(path)
        handler = self.route_trie.find(parts)
        return handler if handler is not None else self.not_found_handler
        # DONE: lookup path (by parts) and return the associated handler
        # DONE: you can return None if it's not found or
        # DONE: return the "not found" handler if you added one -> add this to our init
        # DONE: bonus points if a path works with and without a trailing slash
        # DONE: e.g. /about and /about/ both return the /about handler

    def split_path(self, path: str):
        if path.startswith('/') and path.endswith('/'):
            path = path.strip("/")
        if path:
            return path.split('/')
        else:
            return list()
# you need to split the path into parts for
# both the add_handler and loopup functions,
# so it should be placed in a function here

if __name__ == '__main__':
    # Here are some test cases and expected outputs you can use to test your implementation

    # create the router and add a route
    router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about")) # should print 'about handler'
    print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


