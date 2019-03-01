import time


# class BinarySearchTree:
#     def __init__(self, value=None):
#         self.value = value
#         self.left = None
#         self.right = None

#     def insert(self, value):
#         if self.value == None:
#             self.value = value
#         else:
#             target = 'left' if value <= self.value else 'right'
#             target_val = getattr(self, target)
#             if target_val is None:
#                 setattr(self, target, BinarySearchTree(value))
#             else:
#                 target_val.insert(value)

#     def contains(self, target):
#         if self.value == target:
#             return True
#         if target < self.value:
#             return self.left and self.left.contains(target)
#         else:
#             return self.right and self.right.contains(target)

#     def get_max(self):
#         if self.right is None:
#             return self.value
#         else:
#             return self.right.get_max()


start_time = time.time()

# binary tree version
# names = BinarySearchTree()
# duplicates = []
# with open('names_1.txt', 'r') as f:
#     for line in f.readlines():
#         names.insert(line.strip())

# with open('names_2.txt', 'r') as f:
#     for line in f.readlines():
#         line = line.strip()
#         if names.contains(line):
#             duplicates.append(line)

# dictionary version
# names = {}
# duplicates = []
# with open('names_1.txt', 'r') as f:
#     for line in f.readlines():
#         names[(line.strip())] = 1

# with open('names_2.txt', 'r') as f:
#     for line in f.readlines():
#         line = line.strip()
#         if names.get(line) is not None:
#             duplicates.append(line)


# arrays only
names = []
duplicates = []
with open('names_1.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        start = 0
        end = len(names) - 1
        while start < end:
            mid = (start + end) // 2
            if names[mid] >= line:
                end = mid - 1
            else:
                start = mid + 1
                mid = (mid + end) // 2
        if not names:
            names.append(line)
        if names[start] > line:
            names.insert(start, line)
        else:
            names.insert(start + 1, line)

s = sorted(names)
for i in range(len(names)):
    if names[i] != s[i]:
        print(f'{names[i]} not equal to {s[i]}')
        break

print('sorted okay')

with open('names_2.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        start = 0
        end = len(names) - 1

        while start < end:
            mid = (start + end) // 2
            if names[mid] == line:
                duplicates.append(line)
                break
            if names[mid] >= line:
                end = mid - 1
            else:
                start = mid + 1
                mid = (mid + end) // 2

        else:
            if names[start] == line:
                duplicates.append(line)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
