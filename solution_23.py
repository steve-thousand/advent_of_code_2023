DIRECTIONS = ['>', 'v', '<', '^']

def max_graph_path(graph, goal, visited=set(), at=(0, 1), distance=0):
    if at == goal:
        return distance
    distances = [-1]
    for adj in graph[at]:
        if adj[0] not in visited:
            new_visited = set(visited)
            new_visited.add(adj[0])
            distances.append(max_graph_path(graph, goal, new_visited, adj[0], distance + adj[1]))
    return max(distances)

def find_edges(maze, start, climb_slopes=False):
    goal, vertices = (len(maze) - 1, len(maze[0]) - 2), []
    queue = [(start, 0, (start[0], start[1]))]
    while len(queue) > 0:
        item = queue.pop(0)
        node, distance, start, next_nodes = item[0], item[1], item[2], []
        for direction in range(0, 4):
            if len(node) > 2 and direction == (node[2] + 2) % 4:
                continue
            new_y = node[0] + (1 if direction == 1 else -1 if direction == 3 else 0)
            new_x = node[1] + (1 if direction == 0 else -1 if direction == 2 else 0)
            if new_y < 0 or new_y >= len(maze) or new_x < 0 or new_x >= len(maze[0]) or maze[new_y][new_x] == '#':
                continue
            if maze[new_y][new_x] == '.' or climb_slopes or maze[new_y][new_x] == DIRECTIONS[direction]:
                next_node = (new_y, new_x, direction)
                if (new_y, new_x) not in vertices or (start, distance + 1) not in vertices[(new_y, new_x)]:
                    next_nodes.append(next_node)
        if node != start and (len(next_nodes) > 1):
            vertices.append(((node[0], node[1]), distance))
            continue
        for next_node in next_nodes:
            if (next_node[0], next_node[1]) == goal and (next_node, distance) not in vertices:
                vertices.append(((next_node[0], next_node[1]), distance + 1))
            queue.append((next_node, distance + 1, start))
    return vertices

def build_graph(maze, climb_slopes=False):
    start = (0, 1)
    queue = [start]
    graph = {}
    while len(queue) > 0:
        vertex = queue.pop()
        edges = find_edges(maze, vertex, climb_slopes)
        graph[vertex] = edges
        for edge in edges:
            if edge[0] not in graph:
                queue.append(edge[0])
    return graph

def solve(puzzle_input):
    maze = [[x for x in y] for y in puzzle_input.strip().splitlines()]
    goal = (len(maze) - 1, len(maze[0]) - 2)
    graph = build_graph(maze)
    print(max_graph_path(graph, goal))
    graph = build_graph(maze, True)
    print(max_graph_path(graph, goal))

solve('''
#.###########################################################################################################################################
#.#.....###...#...#.....#.....................#.....................#...#.....#...#.....#...###.........#.........#.......#...#####...#.....#
#.#.###.###.#.#.#.#.###.#.###################.#.###################.#.#.#.###.#.#.#.###.#.#.###.#######.#.#######.#.#####.#.#.#####.#.#.###.#
#...#...#...#.#.#.#...#.#...............#.....#.........#...........#.#.#...#...#.#.#...#.#.###.#.......#...#.....#.....#.#.#.###...#.#.#...#
#####.###.###.#.#.###.#.###############.#.#############.#.###########.#.###.#####.#.#.###.#.###.#.#########.#.#########.#.#.#.###.###.#.#.###
#.....###.#...#.#...#.#.###...#.....###.#.###...###...#.#.#...#####...#...#.....#.#.#...#.#...#.#...#...#...#...#...#...#...#...#...#...#...#
#.#######.#.###.###.#.#.###.#.#.###.###.#.###.#.###.#.#.#.#.#.#####.#####.#####.#.#.###.#.###.#.###.#.#.#.#####.#.#.#.#########.###.#######.#
#.#...###.#.###.#...#.#...#.#.#...#.....#.....#.#...#.#.#.#.#.>.>.#.#.....#...#.#.#.#...#...#.#.#...#.#.#.....#.#.#.#.........#.###...#.....#
#.#.#.###.#.###.#.###.###.#.#.###.#############.#.###.#.#.#.###v#.#.#.#####.#.#.#.#.#.#####.#.#.#.###.#.#####.#.#.#.#########.#.#####.#.#####
#.#.#...#.#.#...#...#.#...#.#.#...#...........#.#...#...#...###.#...#...#...#...#.#.#...#...#...#...#.#.#...#.#...#.###...###.#.#...#.#.#...#
#.#.###.#.#.#.#####.#.#.###.#.#.###.#########.#.###.###########.#######.#.#######.#.###.#.#########.#.#.#.#.#.#####.###.#.###.#.#.#.#.#.#.#.#
#...###...#.#...#...#.#...#.#.#.....#.....#...#.....#...........###.....#.....#...#.#...#...#.......#.#.#.#.#.....#.#...#...#.#.#.#.#.#.#.#.#
###########.###.#.###.###.#.#.#######.###.#.#########.#############.#########.#.###.#.#####.#.#######.#.#.#.#####.#.#.#####.#.#.#.#.#.#.#.#.#
#...........#...#.#...#...#.#.......#...#.#.........#.............#...#...#...#...#.#.>.>.#.#.###...#.#.#.#...###.#.#...#...#.#.#.#.#.#...#.#
#.###########.###.#.###.###.#######.###.#.#########.#############.###.#.#.#.#####.#.###v#.#.#.###.#.#.#.#.###.###.#.###.#.###.#.#.#.#.#####.#
#.......#...#...#.#...#.###...#.....#...#.#.......#.#.............###...#.#.###...#.#...#...#...#.#.#.#.#...#.#...#.....#.#...#.#.#...###...#
#######.#.#v###.#.###.#.#####.#.#####.###.#.#####.#.#.###################.#.###.###.#.#########.#.#.#.#.###.#.#.#########.#.###.#.#######.###
#.....#...#.>.#.#...#.#.#...#.#.>.>.#...#...#...#...#...............#.....#...#.....#.#.........#.#.#.#.###.#.#.........#...###...#.....#...#
#.###.#####v#.#.###.#.#.#.#.#.###v#.###.#####.#.###################.#.#######.#######.#.#########.#.#.#.###.#.#########.###########.###.###.#
#...#...#...#...#...#.#.#.#...###.#.#...#...#.#.....###...#.........#.#...#...#.......#.#...#...#.#.#.#.#...#.>.>.....#.#.........#...#...#.#
###.###.#.#######.###.#.#.#######.#.#.###.#.#.#####.###.#.#.#########.#.#.#.###.#######.#.#.#.#.#.#.#.#.#.#####v#####.#.#.#######.###.###.#.#
###...#.#.......#.#...#.#.#.......#.#.###.#.#...#...#...#.#.......###.#.#.#.###.......#...#.#.#.#.#.#.#.#.#...#.....#...#.......#.....#...#.#
#####.#.#######.#.#.###.#.#.#######.#.###.#.###.#.###.###.#######.###.#.#.#.#########.#####.#.#.#.#.#.#.#.#.#.#####.###########.#######.###.#
###...#.....#...#.#.#...#.#...#...#...#...#...#.#...#...#.#.....#...#.#.#.#.#.....###.....#.#.#.#.#...#...#.#.#...#.....#.......#.....#.....#
###.#######.#.###.#.#.###.###.#.#.#####.#####.#.###.###.#.#.###.###.#.#.#.#.#.###.#######.#.#.#.#.#########.#.#.#.#####.#.#######.###.#######
#...#...###...###...#...#...#...#...###.....#.#.#...#...#...###.....#...#...#...#.........#.#.#...#...#.....#...#.#.....#.........#...#...###
#.###.#.###############.###.#######.#######.#.#.#.###.#########################.###########.#.#####.#.#.#########.#.###############.###.#.###
#...#.#...............#.#...###...#...#.....#...#...#.....#####.......#...#...#...........#...#...#.#.#.........#...#.....###...###.....#...#
###.#.###############.#.#.#####.#.###.#.###########.#####.#####.#####.#.#.#.#.###########.#####.#.#.#.#########.#####.###.###.#.###########.#
#...#.#.............#.#.#.#...#.#.#...#.#.........#.#...#...###.#.....#.#.#.#.#...........#...#.#...#.#...#...#.....#.#...#...#.............#
#.###.#v###########.#.#.#.#.#.#.#.#.###.#.#######.#.#.#.###.###.#.#####.#.#.#.#.###########.#.#.#####.#.#.#.#.#####.#.#.###.#################
#.....#.>.#...#...#.#.#.#.#.#...#...#...#.#.....#...#.#.....#...#.#...#.#.#.#.#.........###.#.#.....#...#.#.#.#...#.#.#...#...#.............#
#######v#.#.#.#.#.#.#.#.#.#.#########.###.#.###.#####.#######.###.#.#.#.#.#.#.#########.###.#.#####v#####.#.#.#.#.#.#.###.###.#.###########.#
#...#...#.#.#...#.#...#.#.#...#.....#...#.#.#...#...#...#...#...#.#.#.#.#.#.#.#...#.....#...#.....>.>...#...#...#...#.#...#...#.#...........#
#.#.#.###.#.#####.#####.#.###.#.###.###.#.#.#.###.#.###v#.#.###.#.#.#.#.#.#.#.#.#.#.#####.#########v###.#############.#.###.###.#.###########
#.#.#...#...#.....#...#...###...###.....#...#...#.#...>.>.#...#.#.#.#.#.#.#.#.#.#.#...#...#.......#...#...#.....#...#.#...#.....#.........###
#.#.###.#####.#####.#.#########################.#.#####v#####.#.#.#.#.#.#.#.#.#.#.###v#.###.#####.###.###.#.###.#.#.#.###.###############.###
#.#.....#.....###...#...###.....#.....###.......#.....#...#...#.#.#.#.#.#.#.#.#.#.#.>.>.###.....#.....#...#.#...#.#.#.#...#...#...###...#...#
#.#######.#######.#####.###.###.#.###.###.###########.###.#.###.#.#.#.#.#.#.#.#.#.#.#v#########.#######.###.#.###.#.#.#.###.#.#.#.###.#.###.#
#.......#.....#...#.....#...#...#...#...#...#...#...#...#.#.....#...#...#.#.#.#.#...#.........#.#.....#...#.#...#.#.#.#.###.#.#.#.#...#.....#
#######.#####.#.###.#####.###.#####.###.###.#.#.#.#.###.#.###############.#.#.#.#############.#.#.###.###.#.###.#.#.#.#.###.#.#.#.#.#########
#.......#.....#.#...#...#...#.#...#...#.#...#.#.#.#.#...#.#...#...#...###.#.#.#.#.......#...#.#...#...###...#...#.#.#.#...#.#.#.#.#...#...###
#.#######.#####.#.###.#.###.#.#.#.###.#.#v###.#.#.#.#.###.#.#.#.#.#.#.###.#.#.#.#.#####.#.#.#.#####.#########.###.#.#.###.#.#.#.#.###v#.#.###
#.#.....#...#...#...#.#.....#.#.#.#...#.>.>...#.#.#.#...#...#...#...#...#...#.#.#.....#...#...#.....#.......#.#...#...###.#.#.#.#...>.#.#.###
#.#.###.###.#.#####.#.#######.#.#.#.#####v#####.#.#.###.###############.#####.#.#####.#########.#####.#####.#.#.#########.#.#.#.#####v#.#.###
#...#...###.#...###.#...#.....#.#...#####.....#.#.#...#.#.....#...#.....#...#...#####.....#...#.....#.#.....#.#.#...#...#.#.#...#...#...#...#
#####.#####.###.###.###.#.#####.#############.#.#.###.#.#.###.#.#.#.#####.#.#############.#.#.#####.#.#.#####.#.#.#.#.#.#.#.#####.#.#######.#
#.....#...#.....#...#...#.#...#.#.....###...#.#...###...#...#...#...#...#.#.###...........#.#...###.#.#.#...#...#.#.#.#.#...###...#.......#.#
#.#####.#.#######.###.###.#.#.#.#.###.###.#.#.#############.#########.#.#.#.###.###########.###.###.#.#.#.#.#####.#.#.#.#######.#########.#.#
#.#...#.#...#...#.....###...#.#.#...#.....#...#.........#...#...#...#.#.#.#...#...........#...#.....#.#...#.#...#.#.#.#.#.....#.........#...#
#.#.#.#.###.#.#.#############.#.###.###########.#######.#.###.#.#.#.#.#.#.###.###########.###.#######.#####.#.#.#.#.#.#.#.###.#########.#####
#.#.#.#.###...#.....#...#...#.#.###...#...###...#.....#.#.....#...#...#.#.#...#.........#...#.#.......#...#.#.#.#.#.#.#.#.#...#...#...#...###
#.#.#.#.###########.#.#.#.#.#.#.#####.#.#.###.###.###.#.###############.#.#.###.#######.###.#.#.#######.#.#.#.#.#.#.#.#.#.#.###.#.#.#.###v###
#...#...#.........#...#...#.#.#...###...#...#...#...#...###...#.........#.#...#.......#.....#...#.....#.#...#.#.#.#.#.#.#.#...#.#.#.#...>.###
#########.#######.#########.#.###.#########.###.###.#######.#.#.#########.###.#######.###########.###.#.#####.#.#.#.#.#.#.###.#.#.#.#####v###
###.......#...###...........#.....#.....#...#...#...#...###.#.#.....#...#.#...#...###.#...#...###...#.#.#...#.#.#.#.#.#...###...#...#...#...#
###.#######.#.#####################.###.#.###.###.###.#.###.#.#####v#.#.#.#.###.#.###v#.#.#.#.#####.#.#v#.#.#.#.#.#.#.###############.#.###.#
#...#.......#.#...............#...#...#...###...#...#.#.#...#.#...>.>.#...#.#...#.#.>.>.#.#.#.#...#.#.>.>.#...#...#.#.....#.........#.#...#.#
#.###.#######.#.#############.#.#.###.#########.###.#.#.#.###.#.###v#######.#.###.#.#v###.#.#.#.#.#.###v###########.#####.#.#######.#.###.#.#
#.....#...#...#.#...#.........#.#.###.....#...#...#...#.#...#...###.......#.#.###...#.#...#.#.#.#.#.###.......#...#...#...#.......#.#...#...#
#######.#.#.###.#.#.#.#########.#.#######.#.#.###.#####.###.#############.#.#.#######.#.###.#.#.#.#.#########.#.#.###.#.#########.#.###.#####
#.......#.#...#.#.#...#...#...#.#.###.....#.#.#...###...#...#.............#...#.......#.....#...#.#.#.........#.#...#.#.#.........#.....#...#
#.#######.###v#.#.#####.#.#.#.#.#.###.#####.#.#.#####.###.###.#################.#################.#.#.#########.###.#.#.#.###############.#.#
#.......#.###.>.#.#...#.#.#.#...#...#.....#.#...#...#.....###.................#.................#...#...........#...#...#...#.............#.#
#######.#.###v###.#.#.#.#.#.#######.#####.#.#####.#.#########################.#################.#################.#########.#.#############.#
###...#.#.#...###.#.#.#.#.#...#.....#...#.#.......#...#...#...#...#...#...#...#...........#...#.#.....#...........###.....#...#...#...#...#.#
###.#.#.#.#.#####.#.#.#.#.###.#.#####.#.#v###########.#.#.#.#.#.#.#.#.#.#.#.###.#########.#.#.#.#.###.#.#############.###.#####.#.#.#.#.#.#.#
#...#...#.#.....#.#.#.#.#...#.#.#...#.#.>.>...#...#...#.#...#...#.#.#.#.#.#...#...#...###...#.#.#.#...#.....#...#...#.#...#.....#...#...#.#.#
#.#######.#####.#.#.#.#.###.#.#.#.#.#.###v###.#.#.#.###.#########.#.#.#.#.###.###.#.#.#######.#.#.#.#######.#.#.#.#.#.#.###.#############.#.#
#.......#.......#...#.#...#.#.#.#.#...#...###...#.#.###.........#...#...#.#...###...#.......#...#.#.###...#.#.#.#.#.#.#...#.............#.#.#
#######.#############.###.#.#.#.#.#####.#########.#.###########.#########.#.###############.#####.#.###.#.#.#.#.#.#.#.###.#############.#.#.#
#.......#...........#.#...#...#...#...#...###...#...#...........#.....#...#...#.............###...#...#.#.#.#.#...#...#...#...#.........#...#
#.#######.#########.#.#.###########.#.###.###.#.#####.###########.###.#.#####.#.###############.#####.#.#.#.#.#########.###.#.#.#############
#.#...#...#.....#...#...###.......#.#.#...#...#.#...#.........#...#...#...#...#.......#.......#...#...#.#.#...#.......#...#.#...#...###.....#
#.#.#.#.###.###.#.#########.#####.#.#.#.###.###.#.#.#########.#.###.#####.#.#########.#.#####.###.#.###.#.#####.#####.###.#.#####.#.###.###.#
#...#...###...#...#...#...#.....#.#.#.#...#...#.#.#.###.......#.#...#####...###...###...#.....#...#...#.#...#...#...#.#...#.......#.....#...#
#############.#####.#.#.#.#####.#.#.#.###v###.#.#.#.###v#######.#.#############.#.#######.#####.#####.#.###.#.###.#.#.#.#################.###
#...........#...#...#...#...#...#...#...>.>.#.#.#.#.#.>.>.......#.#######...#...#.#.......#...#...#...#.#...#...#.#.#...#...#.............###
#.#########.###.#.#########.#.###########v#.#.#.#.#.#.#v#########.#######.#.#.###.#.#######.#.###.#.###.#.#####v#.#.#####.#.#.###############
#.........#.....#.......###.#.#...........#.#.#...#.#.#.........#...###...#.#...#.#.....#...#.....#...#.#.....>.>.#.....#.#.#...............#
#########.#############.###.#.#.###########.#.#####.#.#########.###.###.###.###.#.#####.#.###########.#.#######v#######.#.#.###############.#
#.........#.....###...#...#...#...........#.#.....#.#.#.........###...#.#...#...#.###...#...........#.#...#.....###.....#.#.................#
#.#########.###.###.#.###.###############.#.#####.#.#.#.#############.#.#.###.###.###.#############.#.###.#.#######.#####.###################
#...#.......#...#...#.#...#.......#...#...#...#...#...#...........#...#.#...#...#...#.#...#.....#...#.....#.......#.....#...............#...#
###.#.#######.###.###.#.###.#####.#.#.#.#####.#.#################.#.###.###.###.###.#.#.#.#.###.#.###############.#####.###############.#.#.#
#...#.#.......###...#.#...#.....#...#...#####...#.................#...#.###...#.#...#.#.#.#...#.#.#...###...#...#.#.....###...#.........#.#.#
#.###.#.###########.#.###.#####.#################.###################.#.#####.#.#.###v#.#.###.#.#.#.#.###.#.#.#.#.#.#######.#.#v#########.#.#
#.....#.......###...#.....#...#.............#...#...........#.........#.#.....#.#...>.>.#.....#...#.#.....#...#...#.....#...#.>.#.........#.#
#############v###.#########.#.#############.#.#.###########.#.#########.#.#####.#####v#############.###################.#.#####v#.#########.#
#...###...###.>.#.....#.....#.........#.....#.#...###...#...#.....#...#.#...#...#...#.###.....#...#.................#...#.#.....#.#.........#
#.#.###.#.###v#.#####.#.#############.#.#####.###.###.#.#.#######.#.#.#.###.#.###.#.#.###.###.#.#.#################.#.###.#.#####.#.#########
#.#.#...#...#.#.#.....#.#...........#.#.....#...#.....#...#.....#.#.#.#.###...#...#.#.....#...#.#.#####...#...#...#.#...#.#.#...#.#.........#
#.#.#.#####.#.#.#.#####.#.#########.#.#####.###.###########.###.#.#.#.#.#######.###.#######.###.#.#####.#.#.#.#.#.#.###.#.#.#.#.#.#########.#
#.#.#.....#...#.#...###...#...#.....#...#...#...#...#.....#.#...#...#...###...#...#...#.....###.#.#.....#...#...#...###.#.#.#.#.#.###.......#
#.#.#####.#####.###.#######.#.#.#######.#.###.###.#.#.###.#.#.#############.#.###.###.#.#######.#.#.###################.#.#.#.#.#.###.#######
#.#.#####.....#...#.#.......#.#.......#.#...#.#...#.#.#...#.#.#...###...###.#...#...#.#...#.....#.#...........#...#.....#.#.#.#.#.#...###...#
#.#.#########.###.#.#.#######.#######.#.###.#.#.###.#.#.###.#.#.#.###.#.###.###.###.#.###.#.#####.###########.#.#.#.#####.#.#.#.#.#.#####.#.#
#.#...........###...#.......#.#...#...#.....#...###.#.#.....#.#.#.#...#...#.#...#...#.....#...#...#...........#.#.#.......#...#...#.......#.#
#.#########################.#.#.#.#.###############.#.#######.#.#.#.#####.#.#.###.###########.#.###.###########.#.#########################.#
#...#.......#...###...#.....#...#...#...#...#.....#...###.....#.#.#...#...#.#.#...#.....#...#.#...#.#...........#.......#.................#.#
###.#.#####.#.#.###.#.#.#############.#.#.#.#.###.#######.#####.#.###.#.###.#.#v###.###.#.#.#.###.#.#.#################.#.###############.#.#
###...###...#.#.###.#.#...#...###.....#...#.#...#.#...#...#####.#.#...#...#.#.>.>.#...#.#.#.#.#...#...#.........#...#...#...............#.#.#
#########v###.#.###.#.###.#.#.###.#########.###.#.#.#.#.#######.#.#.#####.#.###v#.###.#.#.#.#.#.#######v#######.#.#.#.#################.#.#.#
#.......#.>.#.#...#.#...#...#.....#.......#.#...#.#.#.#...###...#...#...#...#...#.....#...#.#.#.......>.>.#...#...#...###.....#.....#...#...#
#.#####.#v#.#.###.#.###.###########.#####.#.#.###.#.#.###.###.#######.#.#####.#############.#.#########v#.#.#.###########.###.#.###.#.#######
#.#...#...#.#.#...#.#...#...#.......#...#...#.#...#.#.###...#.........#.....#.............#.#.....#.....#...#...#...#...#...#.#...#.#.......#
#.#.#.#####.#.#.###.#.###.#.#.#######.#.#####.#.###.#.#####.###############.#############.#.#####.#.###########.#.#.#.#.###.#.###.#.#######.#
#.#.#.....#...#...#.#...#.#.#.#...#...#...#...#...#.#...#...#...#.....#.....#.............#.#.....#.....#.......#.#.#.#.#...#...#.#.#.......#
#.#.#####.#######.#.###.#.#.#.#.#.#.#####.#.#####.#.###.#.###.#.#.###.#.#####.#############.#.#########.#.#######.#.#.#.#.#####.#.#.#.#######
#...#...#.....#...#.###.#.#.#.#.#.#...#...#...#...#.#...#.###.#...###.#.#.....#...........#.#...#.......#.###.....#.#.#.#.....#.#.#.#.......#
#####.#.#####.#.###.###.#.#.#v#.#.###.#.#####.#.###.#.###v###.#######.#.#.#####.#########.#.###.#.#######.###.#####.#.#.#####.#.#.#.#######.#
#.....#.......#...#...#...#.>.>.#.....#.#...#.#.#...#.#.>.>...###...#...#.......#...#...#.#.#...#...#...#...#.....#.#.#.#...#.#.#.#.#.......#
#.###############.###.#######v#########.#.#.#.#.#.###.#.#v#######.#.#############.#.#.#.#.#.#.#####.#.#.###.#####.#.#.#.#.#.#.#.#.#.#v#######
#.......#.......#.....###...#.#...#...#.#.#...#.#...#...#.#...#...#.......#.......#.#.#...#.#.#...#...#...#.....#.#.#.#.#.#.#.#...#.>.#.....#
#######.#.#####.#########.#.#.#.#.#.#.#.#.#####.###.#####.#.#.#.#########.#.#######.#.#####.#.#.#.#######.#####.#.#.#.#.#.#.#.#######v#.###.#
#...###...#...#.....#.....#...#.#...#.#.#...#...#...#.....#.#...#.........#...#...#...###...#...#...#...#...###.#.#.#.#.#.#.#.#.....#...#...#
#.#.#######.#.#####.#.#########.#####.#.###.#.###.###.#####.#####.###########.#.#.#######.#########.#.#.###.###.#.#.#.#.#.#.#.#.###.#####.###
#.#.........#.......#.......#...#.....#.....#...#...#.......#...#...........#.#.#.....#...#.........#.#.###...#...#...#...#...#.#...#.....###
#.#########################.#.###.#############.###.#########.#.###########.#.#.#####.#.###.#########.#.#####.#################.#.###.#######
#...#...#...........#.....#.#.###.............#.....#.....#...#.............#...#.....#...#...#.......#.......###.....#.........#.....###...#
###.#.#.#.#########.#.###.#.#.###############.#######.###.#.#####################.#######.###.#.#################.###.#.#################.#.#
#...#.#...#.........#.#...#...#...#...........###...#...#.#...........#...###...#.......#...#.#...........#...#...#...#.............#...#.#.#
#.###.#####.#########.#.#######.#.#.#############.#.###.#.###########.#.#.###.#.#######.###.#.###########.#.#.#.###.###############.#.#.#.#.#
#...#.#.....#.....#...#.#...#...#.#.......###...#.#.#...#.#...........#.#...#.#.........###.#.#...........#.#...#...#...#.........#...#...#.#
###.#.#.#####.###.#.###.#.#.#.###.#######.###.#.#.#.#.###.#.###########.###.#.#############.#.#.###########.#####.###.#.#.#######.#########.#
###.#.#.....#...#.#.#...#.#.#...#.###...#...#.#.#.#.#.#...#.............#...#.....#.......#...#.........#...#.....###.#.#.......#...........#
###.#.#####.###.#.#.#.###.#.###.#.###.#.###v#.#.#.#.#.#.#################.#######.#.#####.#############.#.###.#######.#.#######.#############
###...#...#.#...#.#.#...#.#...#.#...#.#...>.>.#.#.#.#.#...###...#.........#...###...#.....#.....#.....#...###...#...#.#.#...#...#...........#
#######.#.#.#.###.#.###.#.###.#.###.#.#########.#.#.#.###.###.#.#.#########.#.#######.#####.###.#.###.#########.#.#.#.#.#.#.#.###.#########.#
#.......#...#.###...###.#.#...#...#.#...#.......#.#.#.#...#...#...#...#...#.#.###.....#...#...#.#.#...#...#####.#.#.#.#...#.#...#...#.......#
#.###########.#########.#.#.#####.#.###.#.#######.#.#.#.###.#######.#.#.#.#.#.###v#####.#.###.#.#.#.###.#.#####v#.#.#.#####.###.###.#.#######
#.#.....#...#.........#...#.#.....#...#.#.#...#...#.#.#...#...#.....#...#.#.#...>.>.#...#.#...#...#.#...#...#.>.>.#.#.#.....###.#...#.#...###
#.#.###.#.#.#########.#####.#.#######.#.#.#.#.#.###.#.###.###.#.#########.#.#######.#.###.#.#######.#.#####.#.#####.#.#.#######v#.###.#.#.###
#...###...#.#.....#...#.....#...#####...#.#.#.#...#...###...#...#.........#...###...#...#.#...###...#...#...#.#####...#...#...>.#...#.#.#...#
###########.#.###.#.###.#######.#########.#.#.###.#########.#####.###########.###.#####.#.###.###.#####.#.###.###########.#.###v###.#.#.###.#
###.........#...#.#.###.#.....#...#.......#.#...#.#.........#...#.#...#.....#...#.....#.#...#...#.#.....#...#...###.......#.#...###.#...#...#
###.###########.#.#.###.#.###.###.#.#######.###.#.#.#########.#.#v#.#.#.###.###.#####.#.###.###.#.#.#######.###.###.#######.#.#####.#####.###
#...#.....#...#.#.#.#...#...#...#.#...#...#.#...#.#.#...#...#.#.>.>.#.#.###...#.....#.#.###.#...#.#.......#.#...#...#.....#.#.....#.#.....###
#.###.###.#.#.#.#.#.#.#####.###.#.###.#.#.#.#.###.#.#.#.#.#.#.#######.#.#####.#####.#.#.###.#.###.#######.#.#.###.###.###.#.#####.#.#.#######
#.....###...#...#...#.......###...###...#...#.....#...#...#...#######...#####.......#...###...###.........#...###.....###...#####...#.......#
###########################################################################################################################################.#
''')