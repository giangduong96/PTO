def normal():
    table = {"Nick": "A", "Ada": "B", "Mike": "B", "Leo": "C", "Sandy": "D"}
    result = {}
    for name, score in table.items():
        if score not in result:
            result[score] = [name]
        else:
            result[score].append(name)

    print(result)


def setdefault():
    table = {"Nick": "A", "Ada": "B", "Mike": "B", "Leo": "C", "Sandy": "D"}
    result = {}
    for name, score in table.items():
        g = result.setdefault(score, [])
        g.append(name)

    print(result)


def defaultdict():
    table = {"Nick": "A", "Ada": "B", "Mike": "B", "Leo": "C", "Sandy": "D"}
    from collections import defaultdict

    result = defaultdict(list)
    for name, score in table.items():
        result[score].append(name)  # all keys have a default already

    print(type(result))
    print(result)


normal()
setdefault()
defaultdict()
