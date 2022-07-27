

def initiate_costs_table(graph, start):
    """
    Initiates the first values for the graph's points connected to start.

    Synchronical with initiate_parents_table.
    """
    costs = {i: float('inf') for i in graph.keys()}
    for v, k in graph[start].items():
        if costs[v] == float('inf'):
            costs[v] = k
    return costs


def initiate_parents_table(graph, start):
    """
    Initiates the first parents for the graph's points connected to start.

    Synchronical with initiate_costs_table.
    """
    parents = {i: None for i in graph.keys()}
    for k, v in graph[start].items():
        if parents[k] is None:
            parents[k] = start
    return parents


def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra_algorithm(graph, start, finish):
    costs = initiate_costs_table(graph, start)
    parents = initiate_parents_table(graph, start)
    processed = []

    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        # Go through all the node's neighbours and discover those which can have less cost if goes via this node.
        for neighbour, neighbour_cost in graph[node].items():
            new_cost = costs[node] + neighbour_cost
            if new_cost < costs[neighbour]:
                costs[neighbour] = new_cost
                parents[neighbour] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    return costs, parents, processed


graph = {
    'start': {'a': 6, 'b': 2},
    'a': {'finish': 1},
    'b': {'a': 3, 'finish': 1},
    'finish': {'b': 1},
}

costs, parents, processed = dijkstra_algorithm(graph, 'b', 'a')

print(costs)
print(parents)
print(processed)
