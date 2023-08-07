set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
symmetric_difference_set = set1.symmetric_difference(set2)

# print(union_set,intersection_set,difference_set,symmetric_difference_set)

arr = [1,2,4,5,1]

newSet = set(arr)

print("Not Unique" if len(newSet)!=len(arr) else "Unique")
