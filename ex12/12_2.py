from collections import defaultdict


class Graph:
    def __init__(self):

        self.edges = defaultdict(list)
        self.paths_counter = 0

    def add_edge(self, a, b):

        self.edges[b].append(a)
        self.edges[a].append(b)

    def make_paths(self, start, end):

        current_path = []
        visited_edges = []
        double_visited = False

        self.make_path(start, end, visited_edges, current_path, double_visited)

    def make_path(self, local_start, end, visited_edges, current_path, double_visited):

        # if it's not big cave add to visited
        if not local_start.isupper():
            visited_edges.append(local_start)

        current_path.append(local_start)

        if local_start == end:
            self.paths_counter += 1

        else:
            # if current node is not end node go through nodes edges
            for next_start in self.edges[local_start]:

                condition_1 = (next_start not in visited_edges) \
                              or (next_start in visited_edges and double_visited == False) \
                              and next_start != 'start'

                # if next vertices isnt last visited 
                if condition_1 and current_path[-1] != next_start:

                    if next_start in visited_edges:
                        double_visited = True
                    self.make_path(next_start, end, visited_edges, current_path, double_visited)

                    if next_start in visited_edges:
                        double_visited = False

        current_path.pop()
        if local_start in visited_edges:
            visited_edges.remove(local_start)


with open('12_input.txt') as reader:
    graph = Graph()

    for line in reader:
        line = line.replace('\n', '')
        line = line.split('-')
        graph.add_edge(*line)

graph.make_paths('start', 'end')
print(graph.paths_counter)