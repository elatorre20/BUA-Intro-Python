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

