import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

## MY SOLUTION ~~ runtime 0.0689 seconds ~~ complexity of log[n]
bst = BinarySearchTree(names_1[0])
bstduplicates = []
for name in names_1:
    bst.insert(name)

for name in names_2:
    if bst.contains(name):
        bstduplicates.append(name)

## ORIGINAL SOLUTION ~~ Runtime 3.9709 seconds ~~ complexity of n^2
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# My TEST ~~ to make sure my BST had the same duplicates as the original solution

# numdupes = 0

# for name1 in bstduplicates:
#     for name2 in duplicates:
#         if name1 == name2:
#             numdupes += 1

# print(numdupes)

end_time = time.time()
print (f"{len(bstduplicates)} duplicates:\n\n{', '.join(bstduplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

