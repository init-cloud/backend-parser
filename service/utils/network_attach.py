class Attach():
    def __init__(self, target: list, parent: dict) -> None:
        self.target = target
        self.parent = parent
        self.set_parent()

    def set_parent(self) -> None:
        for t in self.target:
            self.parent[t.target] = t.source

    def find(self, x):
        if self.parent[x] != x:
            return self.find(self.parent[x])
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            self.parent[b] = a
        else:
            self.parent[a] = b