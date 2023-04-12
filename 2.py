class ConsistentHashing(object):
    def __init__(self, nodes=None):
        self.ring = dict()
        self.keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)
    def add_node(self, node):
        key = self.GEN_KEY(node)
        self.ring[key] = node
        self.keys.append(key)
    def remove_node(self, node):
        key = self.GEN_KEY(node)
        del self.ring[key]
        self.keys.remove(key)
    def get_node(self, string_key):
        pos = self.get_node_pos(string_key)
        if pos == -1:
            return None
        return self.ring[self.keys[pos]]
    def get_node_pos(self, string_key):
        if not self.ring:
            return -1
        key = self.GEN_KEY(string_key)
        nodes = self.keys
        for i in range(1, len(nodes)):
            node = nodes[i]
            if key <= node:
                return  i
        return -1