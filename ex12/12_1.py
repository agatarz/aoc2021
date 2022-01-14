from collections import defaultdict


class Graph:
    def __init__(self):

        self.edges = defaultdict(list)
        self.paths_counter = 0

    def add_edge(self, a, b):

        if any(map(str.isupper, [a, b])) or any([a not in ['start', 'end'], b not in ['start', 'end']]):
            self.edges[b].append(a)

        self.edges[a].append(b)

    def make_paths(self, start, end):

        current_path = []
        visited_edges = []

        self.make_path(start, end, visited_edges, current_path)

    def make_path(self, local_start, end, visited_edges, current_path):

        # if it's not big cave add to visited
        if not local_start.isupper():
            visited_edges.append(local_start)

        current_path.append(local_start)

        if local_start == end:
            self.paths_counter += 1
            # print(current_path)

        else:
            # if current node is not end node go through nodes edges
            for next_start in self.edges[local_start]:

                # if next vertices isnt last visited 
                if next_start not in visited_edges and current_path[-1] != next_start:
                    self.make_path(next_start, end, visited_edges, current_path)

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
print('Solution:', graph.paths_counter)
