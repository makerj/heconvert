def swapkv(dictionary):
    return dict([(v, k) for (k, v) in dictionary.items()])


class Namespace(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
