
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[0][u] = u if p == -1 else p
                tin[u] = timer
                timer += 1

                stack.append((u, p, 1))
                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        for j in range(1, LOG):
            for u in range(n):
                parent[j][u] = parent[j - 1][parent[j - 1][u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for j in range(LOG):
                if diff & (1 << j):
                    u = parent[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]

            return parent[0][u]

        class Fenwick:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 2)

            def update(self, i, value):
                i += 1
                while i <= self.n:
                    self.bit[i] ^= value
                    i += i & -i

            def range_update(self, left, right, value):
                self.update(left, value)
                if right + 1 < self.n:
                    self.update(right + 1, value)

            def point_query(self, i):
                result = 0
                i += 1
                while i > 0:
                    result ^= self.bit[i]
                    i -= i & -i
                return result

        fenwick = Fenwick(n)
        chars = list(s)

        for u in range(n):
            fenwick.range_update(
                tin[u], tout[u] - 1,
                1 << (ord(chars[u]) - ord('a'))
            )

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                if chars[u] != c:
                    old_mask = 1 << (ord(chars[u]) - ord('a'))
                    new_mask = 1 << (ord(c) - ord('a'))

                    fenwick.range_update(
                        tin[u], tout[u] - 1, old_mask ^ new_mask
                    )
                    chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])
                w = lca(u, v)

                mask_u = fenwick.point_query(tin[u])
                mask_v = fenwick.point_query(tin[v])
                mask_w = 1 << (ord(chars[w]) - ord('a'))

                mask = mask_u ^ mask_v ^ mask_w
                answer.append(mask == 0 or (mask & (mask - 1)) == 0)

        return answer
