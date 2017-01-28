import collections
import heapq
from queue import PriorityQueue


###
# Queue class.
# Implements a list in which elements are added to the tail and popped from the head.
#
# Members:
#   list: deque() collection.
# Methods:
#   __init__:           Instantiate empty deque.
#   __str__ => String:  Return a string as [ A B C ... Z ].
#   empty   => Boolean: Return True if empty.
#   put     => <T>:     Append an element to the queue tail.
#   pop     => <T>:     Remove and return element from head.
###
class Queue:
    ###
    # Constructor.
    ###
    def __init__(self):
        self.list = collections.deque()

    ###
    # Stringify.
    #   => (String): [ A B C ... Z ].
    ###
    def __str__(self):
        list = []
        string = "[ "
        for item in self.list:
            list.append(str(item))
        string += ( ", ".join(list) + " ]" )
        return string                                                               # ==>

    ###
    # Check if empty.
    #   => (Boolean): True if empty.
    ###
    def empty(self):
        return len(self.list) == 0                                                  # ==>

    ###
    # Append an element.
    #   - item => (any): Element to add at tail.
    ###
    def put(self, item):
        self.list.append(item)

    ###
    # Pop an element.
    #   => (any): Remove and return head element | None.
    ###
    def pop(self):
        if( not(self.empty()) ):
            return self.list.popleft()                                              # ==>
        return None                                                                 # ==>


###
# Stack class.
# Implements a list in which elements are addedand removed from the head.
#
# Members:
#   list: [] list.
# Methods:
#   __init__:           Instantiate empty stack.
#   __str__ => String:  Return a string as [ A B C ... Z ].
#   empty   => Boolean: Return True if empty.
#   put     => <T>:     Append an element to the stack head.
#   pop     => <T>:     Remove and return element from head.
###
class Stack:
    ###
    # Constructor.
    ###
    def __init__(self):
        self.list = []

    ###
    # Stringify.
    #   => (String): [ A B C ... Z ].
    ###
    def __str__(self):
        list = []
        string = "[ "
        for item in self.list:
            list.append(str(item) + " ")
        string += ( ", ".join(list) + " ]" )
        return string                                                               # ==>

    ###
    # Check if empty.
    #   => (Boolean): True if empty.
    ###
    def empty(self):
        return len(self.list) == 0                                                  # ==>

    ###
    # Append an element.
    #   - item => (any): Element to add at tail.
    ###
    def put(self, item):
        self.list.insert(0, item)

    ###
    # Pop an element.
    #   => (any): Remove and return head element | None.
    ###
    def pop(self):
        size = len(self.list)
        if( size > 0 ):
            return self.list.pop(0)                                                 # ==>
        return None                                                                 # ==>


###
# Heap class.
# Implements a list of touples, (cost, node) that stays sorted when elements are added.
# The pist will always pop the element with minimum cost.
#
# Members:
#   list: array.
# Methods:
#   __init__:           Instantiate empty min heap.
#   __str__ => String:  Return a string as [ A(x) B(x) C(x) ... Z(x) ], where x is the cost.
#   empty   => Boolean: Return True if empty.
#   put     => <T>:     Add an element.
#   pop     => <T>:     Remove and return min or max element.
###
class Heap:
    ###
    # Constructor.
    ###
    def __init__(self):
        self.list = []
        heapq.heapify(self.list)

    ###
    # Stringify.
    #   => (String): [ A(x) B(x) C(x) ... Z(x) ] where x is the cost.
    ###
    def __str__(self):
        list = []
        string = "[ "
        for cost, item in self.list:
            list.append(str(item) + "(" + str(cost) + ")")
        string += ( ", ".join(list) + " ]" )
        return string                                                               # ==>

    ###
    # Check if empty.
    #   => (Boolean): True if empty.
    ###
    def empty(self):
        return len(self.list) == 0                                                  # ==>

    ###
    # Add an element.
    #   - item => (any): Node.
    #   - cost => (Int): Weight.
    ###
    def put(self, item, cost=0):
        heapq.heappush(self.list, (cost, item))

    ###
    # Pop an element.
    #   => (Int, any): Remove and return the (cost, node) touple with minimum cost | None.
    ###
    def pop(self):
        if( not(self.empty()) ):
            return heapq.heappop(self.list)                                         # ==>
        return None                                                                 # ==>


###
# Graph class.
# Implements a weighted graph structured as a map of maps, where each outer element
# represents a vertex and each inner element represents a {vertex: cost} element.
# Vertices are by definition strings, to handle nodes, these should be instantiated
# externally and the graph vertices should represent the node keys.
#
# Members:
#   edges: Map of vertex neighbours {vertex: {vertex: cost, ... vertex: cost} }.
# Methods:
#   __init__:           Instantiate empty graph.
#   __str__ => String:  Return one line per vertex as "vertex: [ vertex(cost) ... ]".
#   empty   => Boolean: Return True if empty.
#   put     => <T>:     Add an element.
#   pop     => <T>:     Remove and return min or max element.
###
class Graph:
    ###
    # Constructor.
    ###
    def __init__(self):
        self.edges = {}

    ###
    # Stringify.
    #   => (String): One line per vertex as "vertex: [ vertex(cost) ... ]".
    ###
    def __str__(self):
        string = ""
        for node in self.edges:
            string += (str(node) + "(" + str(len(self.edges[node])) + "): [ " )
            list = []
            for neighbour, cost in self.edges[node].items():
                list.append( str(neighbour) + "(" + str(cost) + ")" )
            string += ", ".join(list)
            string += " ]\n"
        return string                                                               # ==>

    ###
    # Add a vertex.
    # If the vertex already exists, the method will do nothing.
    #   - node => (any): Vertex node, will be converted to string (any).
    # => (String): The vertex node converted to a string.
    ###
    def addNode(self, node):
        key = str(node)
        if( not(key in self.edges) ):
            self.edges[key] = {}
        return key                                                                  # ==>

    ###
    # Get vertex neighbours.
    # This method will will return the edges of the provided node, if the node is not found,
    # the method will return None.
    #   - node => (any): Target node, will be converted to string.
    #   => (dictionary): Edges | None.
    ###
    def getEdges(self, node):
        return self.edges.get(str(node))                                            # ==>

    ###
    # Return a path object from the provided path list.
    # This method will return a Path object populated from the provided path list.
    # If any vertex or edge is not resolved, the method will return None.
    #   - path => (list): Pas as a list of vertex keys.
    #   => (Path): Path with total and individual costs | None.
    ###
    def makePath(self, path):
        p = Path()
        if (len(path) > 0):
            start = path.pop(0)
            p.path[start] = 0
            while( len(path) > 0 ):
                dest = path.pop(0)
                edges = self.getEdges(start)
                if( not(edges is None) ):
                    cost = edges.get(dest)
                    if( not(cost is None) ):
                        p.cost += cost
                        p.path[dest] = cost
                        start = dest
                    else:
                        return None                                                 # ==>
                else:
                    return None                                                     # ==>
        return p                                                                    # ==>

    ###
    # Create a directed graph edge.
    # This method will add and connect the provided nodes with a directed edge, from the
    # start vertex to the end vertex with a weight of cost.
    # If the edge already exists, the method will replace it.
    #   - start => (any): Relationship source, will be converted to string.
    #   - end => (any):   Relationship destination, will be converted to string.
    #   - cost => (Int):  Relationship weight.
    ###
    def connectNodes(self, start, end, cost=0):
        self.edges[self.addNode(start)][self.addNode(end)] = cost

    ###
    # Create a bidirectional graph edge.
    # This method will add and connect the provided nodes in both directions, it will create
    # two directed edges, one from start to end and one from end to start, both with the
    # same provided cost.
    # If the edges already exists, the method will replace them.
    #   - start => (any): Relationship source, will be converted to string.
    #   - end => (any):   Relationship destination, will be converted to string.
    #   - cost => (Int):  Relationship weight.
    ###
    def relateNodes(self, start, end, cost=0):
        start = self.addNode(start)
        end = self.addNode(end)
        self.edges[start][end] = cost
        self.edges[end][start] = cost

    ###
    # Return least nodes path between two vertices.
    # This method will traverse the graph fron the start node until it finds the goal node
    # returning the path with the least nodes.
    # If any of the start and goal nodes are not in the graph, the method will return None.
    #   - start => (any): Start node, will be converted to string.
    #   - goal => (any):  Goal node, will be converted to string.
    #   => (Path): Shortest path | None.
    ###
    def leastNodes(self, start, goal):
        try:
            return self.makePath( next( self.bfs(start, goal) ) )                   # ==>
        except StopIteration:
            return None                                                             # ==>

    ###
    # Return least cost path between two vertices.
    # This method will traverse the graph fron the start node until it finds the goal node
    # returning the path with the least cumulative cost.
    # If any of the start and goal nodes are not in the graph, the method will return None.
    #   - start => (any): Start node, will be converted to string.
    #   - goal => (any):  Goal node, will be converted to string.
    #   => (Path): Shortest path | None.
    ###
    def leastCost(self, start, goal):
        try:
            return  self.makePath(self.ucs(start, goal))                          # ==>
        except StopIteration:
            return None                                                             # ==>

    ###
    # Traverse graph in Breath-First search.
    # This method will traverse the graph fron the start node until it finds the goal node.
    # The method will return all paths that lead to the goal from the start.
    # If any of the start and goal nodes are not in the graph, the method will return None.
    #   - start => (any): Start node, will be converted to string.
    #   - goal => (any):  Goal node, will be converted to string.
    #   => (list): List of paths | None.
    ###
    def bfs(self, start, goal):
        start = str(start)
        goal = str(goal)
        queue = [(start, [start])]
        while queue:
            (node, path) = queue.pop(0)
            for key, cost in self.edges[node].items():
                if (not (key in set(path))):
                    if (key == goal):
                        yield path + [key]                                          # ==>
                    else:
                        queue.append((key, path + [key]))

    ###
    # Traverse graph in Depth-First search.
    # This method will traverse the graph fron the start node until it finds the goal node.
    # The method will return all paths that lead to the goal from the start.
    # If any of the start and goal nodes are not in the graph, the method will return None.
    #   - start => (String): Start node, will be converted to string.
    #   - goal => (String):  Goal node, will be converted to string.
    #   - level => (Int):    Maximum depth level (zero-based); use -1 for all levels, or
    #                        None to set with nummber of nodes in graph.
    #   - path => (list):    Current path, used when recursing.
    #   => (list): List of paths | None.
    ###
    def dfs(self, start, goal, level=-1, path=None):
        if( path is None ):
            path = [start]
            if( level is None ):
                level = len(self.edges)
        if( start == goal ):
            yield path                                                              # ==>
        if( level != 0 ):
            for key, cost in self.edges[start].items():
                if (not (key in path)):
                    yield from self.dfs( key, goal, level - 1, path + [key] )

    ###
    # Traverse graph in Uniform-Cost search.
    # This method will traverse the graph fron the start node until it finds the goal node.
    # The method will return the path with the least cost between start and goal.
    # If any of the start and goal nodes are not in the graph, the method will return None.
    #   - start => (any): Start node, will be converted to string.
    #   - goal => (any):  Goal node, will be converted to string.
    #   => (list): Least cost path | None.
    ###
    def ucs(self, start, goal):
        start = str(start)
        goal = str(goal)
        visited = set()
        queue = PriorityQueue()
        queue.put( (0, start, [start]) )
        while queue:
            total, node, path = queue.get()
            if node not in visited:
                visited.add(node)
                if node == goal:
                    return path                                                     # ==>
                for vertex, cost in self.edges[node].items():
                    if vertex not in visited:
                        queue.put( (total + cost, vertex, path + [vertex]) )


###
# Path class.
# Implements an object that holds graph paths with individual and total weights.
# The object is instantiated with a graph and path.
#
# Members:
#   path: Map of edges representing path {vertex: cost, ... vertex: cost}.
#   cost: Total path cost (Int).
# Methods:
#   __init__:           Instantiate empty graph.
#   __str__ => String:  Return one line per vertex as "vertex: [ vertex(cost) ... ]".
#   empty   => Boolean: Return True if empty.
#   put     => <T>:     Add an element.
#   pop     => <T>:     Remove and return min or max element.
###
class Path:
    ###
    # Constructor.
    ###
    def __init__(self):
        self.path = collections.OrderedDict()
        self.cost = 0

    ###
    # Stringify.
    #   => (String): (total) [ node(cost) ... node(cost) ].
    ###
    def __str__(self):
        list = []
        string = "(" + str(self.cost) + ") [ "
        for node, cost in self.path.items():
            list.append(str(node) + "(" + str(cost) + ")")
        string += ", ".join(list)
        string += " ]"
        return string                                                               # ==>
