from math import inf


"""
на вход:
    - списки смежности: u -> [v1, v2, ...]
    - начальная вершина s

инициализация:
    - s.destination = 0 (остальные вершины в беск)
    - s.color = black (остальные вершины тоже в white)
    - s.parent = None
    - queue.append(s)

цикл: пока очередь не пустая:
    - достаем из очереди элемент u
    - для всех смежных вершин v:
        - кладем их в очередь (вершина должна попадать в очередь ровно 1 раз)
        - v.color = black
        - v.parent = u
        - v.destination = u.destination + 1

"""


def bfs(adjacency_list: list, node_number: int):

    distances = [inf] * len(adjacency_list)
    distances[node_number] = 0
    colors = [0] * len(adjacency_list)
    colors[node_number] = 1
    parents = [None] * len(adjacency_list)
    queue = [node_number]

    while len(queue) > 0:
        current_node = queue.pop(0)

        for adjacency_node in adjacency_list[current_node]:
            if colors[adjacency_node] == 0:
                colors[adjacency_node] = 1
                queue.append(adjacency_node)
                parents[adjacency_node] = current_node
                distances[adjacency_node] = distances[current_node] + 1

    return distances, parents


if __name__ == "__main__":

    test_adjacency_list = [
        [1],
        [0, 2],
        [1, 3],
        [2, 4, 5],
        [3, 5, 6],
        [3, 4, 6, 7],
        [4, 5, 7],
        [5, 6]
    ]

    print(bfs(test_adjacency_list, 2))
