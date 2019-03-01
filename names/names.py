import time

start_time = time.time()

names = {}
duplicates = []
with open('names_1.txt', 'r') as f:
    for line in f.readlines():
        names[line] = 1

with open('names_2.txt', 'r') as f:
    for line in f.readlines():
        if names.get(line) is not None:
            duplicates.append(line.strip())


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
