import pprint

# Define how we will structure the graph
class Graph:
    def __init__(self, nodes):
        self.network = dict()

        for node in nodes:
            self.network[node] = []
    
    def add_node(self, node):
        self.network[label] = []
    
    def add_edge(self, node_one, node_two):
        self.network[node_one].append(node_two)
        self.network[node_two].append(node_one)
    
    def get_edges(self, node):
        return self.network[node]

    def print_network(self):
        pprint.pp(self.network)


# Build the graph
graph = Graph(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R'])
graph.add_edge('A', 'B')
graph.add_edge('A', 'R')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('C', 'E')
graph.add_edge('E', 'F')
graph.add_edge('E', 'G')
graph.add_edge('G', 'H')
graph.add_edge('G', 'I')
graph.add_edge('I', 'J')
graph.add_edge('J', 'K')
graph.add_edge('J', 'M')
graph.add_edge('K', 'L')
graph.add_edge('L', 'M')
graph.add_edge('C', 'N')
graph.add_edge('N', 'O')
graph.add_edge('O', 'P')
graph.add_edge('P', 'Q')
graph.add_edge('Q', 'R')

# Check out the internals
graph.print_network()



def depth_first(graph, start, end):
    stack = [start]
    history = dict()
    visited = set()

    while len(stack) > 0:
        # Get the next node to search through
        node = stack.pop(0)

        # If we have already visited here, skip this
        # loop
        if node in visited:
            continue
        
        # Check if we have found our goal
        if node == end:
            return history

        # Add the node to our list of visited
        visited.add(node)

        # Now add all the edges together
        for child in graph.get_edges(node):
            if child not in visited:
                stack.insert(0, child)
                history[child] = node
    
    # If we got here, there isn't a path between
    # the two nodes
    return None

def history_to_path(history, start, end):
    path = []
    current = end

    while current != start:
        path.insert(0, current)
        current = history[current]
    path.insert(0, current)
    print(path)

print('\nDepth First: Q -> A')
history = depth_first(graph, 'Q', 'A')
history_to_path(history, 'Q', 'A')

print('\nDepth First: M -> A')
history = depth_first(graph, 'M', 'A')
history_to_path(history, 'M', 'A')


def breadth_first(graph, start, end):
    stack = [start]
    history = dict()
    visited = set()

    while len(stack) > 0:
        # Get the next node to search through
        node = stack.pop(0)

        # If we have already visited here, skip this
        # loop
        if node in visited:
            continue
        
        # Check if we have found our goal
        if node == end:
            return history

        # Add the node to our list of visited
        visited.add(node)

        # Now add all the edges together
        for child in graph.get_edges(node):
            if child not in visited:
                stack.append(child)
                history[child] = node
    
    # If we got here, there isn't a path between
    # the two nodes
    return None


print('\nBreadth First: Q -> A')
history = depth_first(graph, 'Q', 'A')
history_to_path(history, 'Q', 'A')

print('\nBreadth First: M -> A')
history = breadth_first(graph, 'M', 'A')
history_to_path(history, 'M', 'A')
