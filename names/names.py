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

## MY SOLUTION #1 ~~ runtime 0.0689 seconds ~~ complexity of log[n] ~~ uses BST
print("Solution #1")

bst = BinarySearchTree(names_1[0])
bstduplicates = []
for name in names_1:
    bst.insert(name)

for name in names_2:
    if bst.contains(name):
        bstduplicates.append(name)

end_time = time.time()
print (f"{len(bstduplicates)} duplicates:\n\n{', '.join(bstduplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

start_time2 = time.time()
print('\n Original Solution')

# # ORIGINAL SOLUTION ~~ Runtime 3.9709 seconds ~~ complexity of n^2
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# end_time2 = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time2 - start_time2} seconds")

# # STRETCH SOLUTION ~~ sets aren't valid so I'll try again. I'm leaving this because it's neat.
# start_time3 = time.time()
# set_1 = set(names_1)
# set_2 = set(names_2)

# set_1.intersection_update(set_2)

# end_time3 = time.time()

# print (f"{len(set_1)} duplicates:\n\n{', '.join(set_1)}\n\n")
# print (f"runtime: {end_time3 - start_time3} seconds")



# My TEST ~~ to make sure my BST had the same duplicates as the original solution

# numdupes = 0

# for name1 in bstduplicates:
#     for name2 in set_1:
#         if name1 == name2:
#             numdupes += 1

# print(numdupes)



