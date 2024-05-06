clusterarray = []

#Kind of emulate low level memory behaviour
class memcluster:
    def __init__(self, cluster = [], maxlen = 8) -> None:
        self.cluster = cluster
        self.maxlen = maxlen
        clusterarray.append(self)
    def write(self, clusterpos, content) -> str:
        if clusterpos >= self.maxlen or clusterpos < 0:
            return "Adress is not allocated"
        
        self.cluster.insert(clusterpos, content)
        return "success"