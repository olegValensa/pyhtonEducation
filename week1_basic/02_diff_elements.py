objects = [1, 2, "dfg", [0, 2], 1]

diff_objects = set()
for obj in objects:
    diff_objects.add(id(obj))
print(len(diff_objects))