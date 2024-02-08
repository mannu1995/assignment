class Dict2:
    def __init__(self):
        self.keys = []
        self.values = []

    def __getitem__(self, key):
        if key not in self.keys:
            raise KeyError(f"Key '{key}' does not exist")
        return self.values[self.keys.index(key)]

    def __setitem__(self, key, value):
        if key in self.keys:
            self.values[self.keys.index(key)] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def __iter__(self):
        return iter(self.keys)
