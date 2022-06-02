

class Meta:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def get_type(self):
        return type(self.value)


class MetaObject:
    def __init__(self):
        super().__init__()
        self.data_set = []

    def get_list(self):
        return self.data_set

    def get_dict(self):
        return {data.key: data.value for data in self.data_set}

    def append(self, item: Meta):
        self.data_set.append(item)
