def update_dictionary(d, key, value):
    if (key not in d) and (2 * key not in d):
        d[2*key] = [value]
    elif key in d:
        temp_list = d.get(key)
        temp_list.append(value)
        d[key] = temp_list
    elif 2*key in d:
        temp_list = d.get(2*key)
        temp_list.append(value)
        d[2*key] = temp_list


d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
