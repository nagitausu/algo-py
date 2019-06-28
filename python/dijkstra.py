import heapq
INF = 10**9

class Dijkstra:
    def __init__(self, adj):
        self.adj = adj
        self.num = len(adj)
        self.dist = [INF] * self.num
        self.prev = [INF] * self.num
        self.q = []

    def reset(self):
        self.dist = [INF] * self.num
        self.prev = [INF] * self.num
        self.q = []

    def calc(self, start, goal=None):
        self.dist[start] = 0
        heapq.heappush(self.q, (0, start))
        while len(self.q) != 0:
            prov_cost, src = heapq.heappop(self.q)
            if self.dist[src] < prov_cost:
                continue
            for dest in range(self.num):
                cost = self.adj[src][dest]
                if cost != INF and self.dist[dest] > self.dist[src] + cost:
                    self.dist[dest] = self.dist[src] + cost
                    heapq.heappush(self.q, (self.dist[dest], dest))
                    self.prev[dest] = src
        if goal is not None:
            return self.get_path(goal)
        else:
            return self.dist

    def get_path(self, goal):
        path = [goal]
        dest = goal

        while self.prev[dest] != INF:
            path.append(self.prev[dest])
            dest = self.prev[dest]
        return list(reversed(path))


if __name__ == "__main__":
    adj = [[INF,2,3], [2,INF,5], [3,5,INF]]
    dijk = Dijkstra(adj)
    print(dijk.calc(1))
    dijk.reset()
    print(dijk.calc(2))
