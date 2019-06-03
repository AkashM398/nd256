from heapq import heappush, heappop
from helpers import load_map

map_40 = load_map("map-40.pickle")

def shortest_path(M, start, goal):
    print("shortest path called")
    frontier = list()
    path_taken = dict()
    total_path_cost = dict()

    heappush(frontier, (0, start))
    path_taken[start] = None
    total_path_cost[start] = 0

    while bool(frontier):
        node = heappop(frontier)
        current_node = node[1]

        if current_node == goal:
            break
        for neighbour_node in M.roads[current_node]:
            cost = total_path_cost[current_node] + manhattan_distance(
                M.intersections[current_node], M.intersections[neighbour_node]
            )
            if (neighbour_node not in total_path_cost) or (
                cost < total_path_cost[neighbour_node]
            ):
                total_path_cost[neighbour_node] = cost
                priority = cost + manhattan_distance(
                    M.intersections[goal], M.intersections[neighbour_node]
                )
                heappush(frontier, (priority, neighbour_node))
                path_taken[neighbour_node] = current_node

    return get_path_taken(path_taken, start, goal)


def manhattan_distance(node_1_loc: list, node_2_loc: list = [0, 0]):
    return abs(node_1_loc[0] - node_2_loc[0]) + abs(node_1_loc[1] - node_2_loc[1])


def get_path_taken(path_map: dict, start, end):
    current = end
    path = list()
    while current != start:
        path.append(current)
        current = path_map[current]
    path.append(start)
    path.reverse()
    return path


print(shortest_path(map_40, 8, 24))  # [8, 14, 16, 37, 12, 17, 10, 24]
print(shortest_path(map_40, 5, 5))  # [5]
print(shortest_path(map_40, 5, 34))  # [5, 16, 37, 12, 34]
