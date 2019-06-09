from heapq import heappush, heappop


class GraphEdges(object):
    def __init__(self, node, path_cost):
        self.node = node
        self.path_cost = path_cost


class GraphNode(object):
    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def add_neighbour(self, node, path_cost):
        self.neighbours.append(GraphEdges(node, path_cost))


node_a = GraphNode("A")
node_b = GraphNode("B")
node_a.add_neighbour(node_b, 10)

map_intersections = {
    0: [0.7798606835438107, 0.6922727646627362],
    1: [0.7647837074641568, 0.3252670836724646],
    2: [0.7155217893995438, 0.20026498027300055],
    3: [0.7076566826610747, 0.3278339270610988],
    4: [0.8325506249953353, 0.02310946309985762],
    5: [0.49016747075266875, 0.5464878695400415],
    6: [0.8820353070895344, 0.6791919587749445],
    7: [0.46247219371675075, 0.6258061621642713],
    8: [0.11622158839385677, 0.11236327488812581],
    9: [0.1285377678230034, 0.3285840695698353],
}

map_roads = [
    [7, 6, 5],
    [4, 3, 2],
    [4, 3, 1],
    [5, 4, 1, 2],
    [1, 2, 3],
    [7, 0, 3],
    [0],
    [0, 5],
    [9],
    [8],
]


def manhattan_distance(node_1_loc: list, node_2_loc: list = [0, 0]):
    return abs(node_1_loc[0] - node_2_loc[0]) + abs(node_1_loc[1] - node_2_loc[1])


def get_path_taken(path_map: dict, start, end):
    current = end
    path = list()
    while current != start:
        current_mapped_value = path_map[current]
        path.append(current)
        current = path_map[current]
    path.append(start)
    path.reverse()
    return path


def shortest_distance(map, start_node, goal_node):
    frontier = list()
    path_taken = dict()
    total_path_cost = dict()

    start_node_cost = manhattan_distance(map_intersections[start_node])

    heappush(frontier, (start_node_cost, start_node))
    path_taken[start_node] = None
    total_path_cost[start_node] = 0

    while bool(frontier):
        node = heappop(frontier)
        current_node = node[1]

        if current_node == goal_node:
            break

        for neighbour_node in map_roads[current_node]:
            cost = total_path_cost[start_node] + manhattan_distance(
                map_intersections[current_node], map_intersections[neighbour_node]
            )
            if (
                neighbour_node not in total_path_cost
                or cost < total_path_cost[neighbour_node]
            ):
                total_path_cost[neighbour_node] = cost
                priority = cost + manhattan_distance(
                    map_intersections[goal_node], map_intersections[neighbour_node]
                )
                heappush(frontier, (priority, neighbour_node))
                path_taken[neighbour_node] = current_node

    return get_path_taken(path_taken, start_node, goal_node)


print(shortest_distance(None, 1, 5))
print(get_path_taken(None, 8, 24))
