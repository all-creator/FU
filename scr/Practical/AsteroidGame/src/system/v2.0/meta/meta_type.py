from meta import MetaObject, Meta


class Resource:
    def __init__(self, path):
        self.path = path
        self.meta = MetaObject()

    def add_meta(self, key, value):
        self.meta.append(Meta(key, value))


class Music(Resource):
    def __init__(self, path):
        super().__init__(path)


class Image(Resource):
    def __init__(self, path):
        super().__init__(path)


class Custom(Resource):
    def __init__(self, path):
        super().__init__(path)


class Data(Resource):
    def __init__(self, path):
        super().__init__(path)
