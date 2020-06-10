from graph import Graph


def earliest_ancestor(ancestors, starting_node):

    # create graph
    g = Graph()

    # ancestors will contain tuples
    # index 0 is parent index 1 is child
    # create vertex for each child and neighbors will be parents
    for i in range(len(ancestors)):
        g.add_vertex(ancestors[i][1])

    for i in range(len(ancestors)):
        g.add_edge(ancestors[i][1], ancestors[i][0])

    # get levels of each node from starting_node
    level = g.get_levels(starting_node)

    # loop through level dictionary and key with most value is the farthes node
    node_list = []
    # use this to check if nodes are on same level
    farthest = 0

    # get node with most value(farthest)
    for key in level:

        if level[key] > farthest:
            farthest = level[key]

    # check each value of key in level
    # if level[key] matches the farthest, append to node_list
    for key in level:
        if level[key] == farthest and level[key] != 0:
            node_list.append(key)

    # if node list contains more more than one node, compare and grab the lowest value
    if len(node_list) >= 1:
        return node_list[0]
    else:
        return -1
