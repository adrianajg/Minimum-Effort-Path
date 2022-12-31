import heapq


def min_effort_path(heights):
    """Given a 2D array of heights, write a function to return
    the path with minimum effort.

    A route's effort is the maximum absolute difference in heights
    between two consecutive cells of the route.

    Parameters
    ----------
    heights : list[list[]] (2D array)
        2D array containing the heights of the available paths

    Returns
    -------
    int
        minimum effort required to navigate the path from (0, 0) to heights[rows - 1][columns - 1]
    """
    pass

def create_min_heights_dict(heights: list) -> dict:
    S = 0
    if len(heights) == 0:
        return {"previous": [], "heights": []}
    g = create_graph(heights)
    pq = initialize_priority_queue(0)
    result = initialize_result_dict(g, S)
    visited = []
    recursive_helper(g, pq, result, visited)
    return result

def create_graph(heights: list) -> list:
    num_nodes = len(heights) * len(heights[0])
    g = create_empty_graph(num_nodes)
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            node_num = i*len(heights[0]) + j
            row = g[node_num]
            given_i_j_adjust_node_num_height_diffs(i, j, heights, row)
    return g


def given_i_j_adjust_node_num_height_diffs(i, j, heights, row):
    '''
    example_input: i = 0, j = 1, 
        heights = [
            [4, 2],
            [3, 8]
        ]
        row = [0, 0, 0, 0]
    example_output: [2, 0, 0, 6]
    '''
    left_adj_coor = None
    right_adj_coor = None
    top_adj_coor = None
    bottom_adj_coor = None
    
    left_adj_node_num = None
    right_adj_node_num = None
    top_adj_node_num = None
    bottom_adj_node_num = None

    if j > 0:
        left_adj_j = j - 1
        left_adj_coor = (i, left_adj_j)
        left_adj_node_num = i*len(heights) + left_adj_j
    if j < len(heights[0]) - 1:
        right_adj_j = j + 1
        right_adj_coor = (i, right_adj_j)
        right_adj_node_num = i*len(heights) + right_adj_j
    if i > 0:
        top_adj_i = i - 1
        top_adj_coor = (top_adj_i, j)
        top_adj_node_num = top_adj_i*len(heights) + j
    if i < len(heights) - 1:
        bottom_adj_i = i + 1
        bottom_adj_coor = (bottom_adj_i, j)
        bottom_adj_node_num = bottom_adj_i*len(heights) + j

    this_node_height = heights[i][j]
    if left_adj_node_num != None:
        left_height = heights[left_adj_coor[0]][left_adj_coor[1]]
        left_diff = abs(this_node_height-left_height)
        row[left_adj_node_num] = left_diff
    if right_adj_node_num != None:
        right_height = heights[right_adj_coor[0]][right_adj_coor[1]]
        right_diff = abs(this_node_height-right_height)
        row[right_adj_node_num] = right_diff
    if top_adj_node_num != None:
        top_height = heights[top_adj_coor[0]][top_adj_coor[1]]
        top_diff = abs(this_node_height-top_height)
        row[top_adj_node_num] = top_diff
    if bottom_adj_node_num != None:
        bottom_height = heights[bottom_adj_coor[0]][bottom_adj_coor[1]]
        bottom_diff = abs(this_node_height-bottom_height)
        row[bottom_adj_node_num] = bottom_diff

def create_empty_graph(num_nodes):
    a_row = [float('inf')] * num_nodes
    g = []
    for i in range(num_nodes):
        g.append(a_row[:])
    return g


def recursive_helper(g: list, pq: list, result: dict, visited: list) -> None:
    if not pq:
        return None
    min_heights = result["min_heights"]
    previous = result["previous"]

    current_height, current = heapq.heappop(pq)
    visited.append(current)
    for neighbor, neighbor_distance in enumerate(g[current]):
        if neighbor_distance != float('inf') and neighbor not in visited:
        # if neighbor not in visited:    
            # new_distance = current_distance + neighbor_distance
            if neighbor_distance < min_heights[neighbor]:
                min_heights[neighbor] = neighbor_distance
                previous[neighbor] = current
                heapq.heappush(pq, (neighbor_distance, neighbor))

    recursive_helper(g, pq, result, visited)


def initialize_result_dict(g: list, s: int) -> dict:
    """
    returns a dict with keys 'previous' and 'distances
    """
    result = {}
    previous = [None] * len(g)
    min_heights = [float("inf")] * len(g)
    # min_heights[s] = 0
    return {"previous": previous, "min_heights": min_heights}


def initialize_priority_queue(s: int) -> list:
    pq = []
    heapq.heappush(pq, (float('inf'), s))
    return pq
