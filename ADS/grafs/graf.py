from collections import defaultdict, deque, namedtuple
from itertools import chain
import operator


class Graf(object):
    def __init__(self):
        self.adjacency_list = defaultdict(lambda: defaultdict(list))

    def add_edge(self, node_from, node_to, edge_val):
        self.adjacency_list[node_from][node_to].append(edge_val)

    def add_node(self, node):
        self.adjacency_list[node]

    def remove_edge(self, node_from, node_to, edge_val=None) -> bool:
        try:
            if not node_from in self.adjacency_list.keys():
                raise KeyError(f"{node_from} does not exist")
            if not node_to in self.adjacency_list[node_from].keys():
                raise KeyError(f"{node_to} is not a neighbour of {node_from}")
            if edge_val:
                self.adjacency_list[node_from][node_to].remove(edge_val)
                if len(self.adjacency_list[node_from][node_to]) == 0:
                    self.adjacency_list[node_from].pop(node_to)
                return True
            else:
                self.adjacency_list[node_from].pop(node_to)
                return True
        except (ValueError, KeyError):
            return False

    @property
    def nodes(self):
        return set(x for x in self.adjacency_list.keys()) | set(
            chain.from_iterable(
                self.adjacency_list[x].keys() for x in self.adjacency_list.keys()
            )
        )

    def dfs(self, node, func: callable, visited=defaultdict(lambda: False)):
        if node not in self.nodes:
            raise KeyError(f"{node} does not exist")
        visited[node] = True
        func(node)
        for neighbour in self.adjacency_list[node]:
            if not visited[neighbour]:
                self.dfs(neighbour, func, visited=visited)

    def __dfs_iterative(self, node, func: callable):
        if node not in self.nodes:
            raise KeyError(f"{node} does not exist")

        visited = defaultdict(lambda: False)
        stack = deque()

        stack.append(node)
        visited[node] = True

        while len(stack):
            node = stack.pop()
            func(node)
            for neighbour in self.adjacency_list[node]:
                if not visited[neighbour]:
                    stack.append(neighbour)
                    visited[neighbour] = True

    def bfs(self, node, func: callable):
        if node not in self.nodes:
            raise KeyError(f"{node} does not exist")

        visited = defaultdict(lambda: False)
        queue = deque()

        queue.appendleft(node)
        visited[node] = True

        while len(queue):
            node = queue.pop()
            func(node)
            for neighbour in self.adjacency_list[node]:
                if not visited[neighbour]:
                    queue.appendleft(neighbour)
                    visited[neighbour] = True

    def path(self, node_from, node_to) -> list:
        if node_from not in self.nodes:
            raise KeyError(f"{node_from} does not exist")
        if node_to not in self.nodes:
            raise KeyError(f"{node_to} does not exist")

        visited = defaultdict(lambda: False)
        queue = deque()

        queue.appendleft(node_from)
        visited[node_from] = True

        found = False
        path = deque()

        while len(queue):
            node = queue.pop()
            path.append(node)
            if node is node_to:
                found = True
                return (found, list(path))
            if all(visited[neighbour] for neighbour in self.adjacency_list[node]):
                path.pop()
            else:
                for neighbour in self.adjacency_list[node]:
                    if not visited[neighbour]:
                        queue.appendleft(neighbour)
                        visited[neighbour] = True

        return (found, None)

    def dijkstra(self, node_start, node_finish):
        q = self.nodes

        d = {}
        d[node_start] = 0

        p = defaultdict(lambda: None)
        while q:
            min_d = min((x for x in d.items() if x[0] in q), key=operator.itemgetter(1))
            node = min_d[0]
            dist = min_d[1]
            q.remove(node)
            for neighbour in self.adjacency_list[node]:
                if neighbour in q:
                    if (
                        not d.get(neighbour, None)
                        or min(self.adjacency_list[node][neighbour]) + dist
                        < d[neighbour]
                    ):

                        d[neighbour] = min(self.adjacency_list[node][neighbour]) + dist
                        p[neighbour] = node

        if not d.get(node_finish, None):
            return None
        path = [node_finish]
        node = node_finish
        while node is not node_start:
            node = p[node]
            path.append(node)

        path.reverse()
        return path, d[node_finish]


if __name__ == "__main__":
    g = Graf()
    g.add_edge("A", "B", 1)
    g.add_edge("B", "C", 2)
    g.add_edge("C", "A", 3)
    g.add_edge("A", "C", 4)
    g.add_node("D")
    g.add_edge("B", "D", 8)
    g.add_edge("D", "A", 9)
    print(g.adjacency_list)
    print(g.remove_edge("B", "A"))
    print(g.remove_edge("B", "A", 3))
    print(g.remove_edge("A", "C"))
    print(g.adjacency_list)
    print(g.nodes)
    g.dfs("A", print)
    g._Graf__dfs_iterative("A", print)
    g.bfs("A", print)
    print(g.path("D", "B"))
    print(g.dijkstra("A", "D"))
