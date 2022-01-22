def drugi(data):
    return sorted(data)[-2]

print(drugi([0, 1, 2, 3]))
assert(drugi([0, 1, 2, 3]))==2
assert(drugi([2, 2, 2, 2]))==2
assert(drugi(['a', 'b', 'c']))=="b"
assert(drugi([1000, 10, 100, 1, 10000]))==1000

from sklearn.ensemble import RandomForestClassifier