from math import inf


def dfs(adjacency_list: list, node_number: int):
    parents = [None] * len(adjacency_list)
    colors = [0] * len(adjacency_list)
    time_in = [inf] * len(adjacency_list)
    time_out = [inf] * len(adjacency_list)
    stack = [node_number]

    time = 0
    time_in[node_number] = time

    while len(stack) > 0:
        current_node = stack[-1]
        if colors[current_node] == 1:
            stack.pop()
            time_out[current_node] = min(time_out[current_node], time)
        else:
            time_in[current_node] = time
            for adj_node in adjacency_list[current_node]:
                if colors[adj_node] == 0:
                    stack.append(adj_node)
                    parents[adj_node] = current_node
            colors[current_node] = 1

        time += 1


if __name__ == "__main__":
    print("")
