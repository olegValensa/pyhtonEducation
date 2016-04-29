temp_array = []

with open('dataset_24465_4.txt') as f_in:
    print(type(f_in))
    for line in f_in:
        temp_array.append(line.rstrip())

for i in reversed(temp_array):
    with open('output.txt', 'a') as f_w:
        f_w.write(i + '\n')
