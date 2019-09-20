import time
from binary_search_tree import BinarySearchTree

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

start_time = time.time()
duplicates = []


# ORIGINAL SOLUTION ~~ Runtime 3.9709 seconds ~~ complexity of n^2

print('\n Original Solution')

for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)


end_time2 = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time2 - start_time} seconds")


# MY SOLUTION #1 ~~ runtime 0.0689 seconds ~~ complexity of log[n] ~~ uses BST
print("MVP Solution")
start_time2 = time.time()

bst = BinarySearchTree(names_1[0])
bstduplicates = []
for name in names_1:
    bst.insert(name)

for name in names_2:
    if bst.contains(name):
        bstduplicates.append(name)

end_time = time.time()
print (f"{len(bstduplicates)} duplicates:\n\n{', '.join(bstduplicates)}\n\n")
print (f"runtime: {end_time - start_time2} seconds")

# STRETCH SOLUTION #2 ~~ 0.02628 seconds runtime ~~ complexity nlog(n)
print('\n Stretch solution #2')
start_time4 = time.time()
names_1.sort()
names_2.sort()

def binarySearch(names, item):
    first_item = 0
    last_item = len(names)-1
    item_found = False

    while(first_item <= last_item and not item_found):
        middle_item = (first_item + last_item)//2
        if names[middle_item] == item:
            item_found = True
        else:
            if item < names[middle_item]:
                last_item = middle_item - 1
            else:
                first_item = middle_item + 1

    return item_found
    
stretchdupes = []
for name in names_1:
    found = binarySearch(names_2, name)
    if found is True:
        stretchdupes.append(name)


end_time4 = time.time()
print (f"{len(stretchdupes)} duplicates:\n\n{', '.join(stretchdupes)}\n\n")
print (f"runtime: {end_time4 - start_time4} seconds")


# STRETCH SOLUTION ~~ runtime of 0.001487 seconds ~~ Sets might not be valid? I'm leaving this because it's neat.
print("Stretch solution #1")
start_time3 = time.time()
names_1 = set(names_1)
names_2 = set(names_2)

names_1.intersection_update(names_2)

end_time3 = time.time()

print (f"{len(names_1)} duplicates:\n\n{', '.join(names_1)}\n\n")
print (f"runtime: {end_time3 - start_time3} seconds")





# # My TEST ~~ to make sure my solutions were returning the same duplicates because they were in different orders.

# numdupes = 0

# for name1 in bstduplicates:
#     for name2 in names_1:
#         if name1 == name2:
#             numdupes += 1

# print(numdupes)



