import os.path


DATA_ROOT = os.path.join(os.path.dirname(__file__), 'data')


def data_path(fname=None):
    if fname is not None:
        return os.path.join(DATA_ROOT, fname)
    return DATA_ROOT


def parse_pairwise(raw):
    comparisons = list()
    max_item = -1
    for line in raw.splitlines():
        line = line.strip()
        if line.startswith('#') or line == '':
            # Line is empty or is a comment, skip it.
            continue
        pair = (a, b) = tuple(map(int, line.split(" > ")))
        comparisons.append(pair)
        if max(pair) > max_item:
            max_item = max(pair)
    num_items = max_item + 1
    return num_items, tuple(comparisons)
