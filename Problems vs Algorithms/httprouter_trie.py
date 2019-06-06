from collections import defaultdict

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler="not found handler"):
        # Initialize the node with children as before, plus a handler
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, route_path, route_handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for path in route_path:
            current_node = current_node.children[path]
        current_node.handler = route_handler

    def find(self, route_path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for path in route_path:
            if path not in current_node.children:
                return "not found handler"
            current_node = current_node.children[path]

        return current_node.handler

# The Router class will wrap the Trie and handler
class Router:
    def __init__(self, route_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self._routetrie = RouteTrie(route_handler)

    def add_handler(self, route, route_handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        route_path = self.split_path(route)
        self._routetrie.insert(route_path, route_handler)

    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if route == "/":
            return self._routetrie.root.handler
        route_path = self.split_path(route)
        return self._routetrie.find(route_path)

    def split_path(self, route):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        if route.startswith("/") and route.endswith("/"):
            route_paths = route[1:-1].split("/")
        else:
            route_paths = route[1:].split("/")

        return route_paths

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/hello/lang/en", "hello")
router.add_handler("/hello/lang/es", "no hablo ingles")
# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/hello/lang/en/"))
print(router.lookup("/hello/lang/es"))