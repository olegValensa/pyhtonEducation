import os
import os.path

directories = []

os.chdir('module2\main')

for current_dir, dirs, files in os.walk('.'):
    print(current_dir, dirs, files)
    for file in files:
        ext = file.split('.')[1]
        if ext == 'py':
            directories.append(current_dir[2:])
            break

for x in directories:
    print(x)

