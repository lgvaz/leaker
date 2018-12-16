import gc


def count_type(obj):
    return sum([type(obj) == type(o) for o in gc.get_objects()])