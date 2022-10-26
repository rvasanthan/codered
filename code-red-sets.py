# Set is an unordered collection of unique items.
#2 Below are the properties of Set
# 1) UnOrdered
# 2) Unique
# 3) UnIndexed
# 4) Mutable - they can grow and Shrink

#How to create Sets
demo_set = {'red', 'blue', 'green', 'yellow'};
print(demo_set);

#You can have a mix of any types
demo_set = {'red', (2,2), 5753725, True, None};
print(demo_set);

#List is mutable but it doesn't contain any mutable objects
#demo_set = {[1,2], [3,4], [4,6]}
#print(demo_set);

#Set Constructors
demo_set = set('abc'); #--> Only for Iterable types this is possible
print(demo_set);

# Set Constructor
#demo_set = set(123);
#print(demo_set);

demo_set = set(range(1,10))
print(demo_set);

#Convert a list into a set
demo_set = set([1,2,3]);
print(demo_set);

#Convert a list with duplicates into a set
demo_set = set([1,2,3,4,5,5,6]);
print(demo_set);

#How to know if set is mutable
demo_set = set(range(1,10));
print(demo_set);
print(hex(id(demo_set)));

demo_set1 = set(range(1,10));
print(demo_set1);
print(hex(id(demo_set1)));

demo_set1.add(11);
print(hex(id(demo_set1)));

#update a list to a Set
demo_set = set((1,2,3));
demo_set.update([4,5,6]);
print(demo_set);

#find the size of the set
print(len(demo_set));

demo_set.remove(6);
print(demo_set);

#what is we remove the item from a set and the item is not available. 
#demo_set.remove(6);

#how to avoid this scenario
demo_set.discard(6);
print(demo_set);

demo_set.discard(5);
print(demo_set);

#Remove a random one.
demo_set.pop();
print(demo_set);

#What if we want to remove all the items from the set
demo_set.clear();
print(demo_set);

#iterate through Set
demo_set = set([1,2,3]);
for i in demo_set:
    print(i);
    
# how to check if an item exists in Set
print(3 in demo_set);

#Set Operators
set1 = set([1,2,3]);
set2 = set([3,4,5]);
set1.union(set2);
#What happens to union.. 
print(set1);
set3 = set1.union(set2);
print(set3);

set4 = set1.intersection(set2);
print(set4);

set5 = set1.difference(set2);
print(set5);
set6 = set2.difference(set1);
print(set6);

set7 = set1.symmetric_difference(set2);
print(set7);

#Removes the items from this set that are not present in other sets
set1.intersection_update(set2);
print(set1);

#Removes the items from this set that are also included in another set
set1 = set((1,2,3));
set1.difference_update(set2);
print(set1);

#Modify this set with the symmetric difference of this set and other set
set1 = set((1,2,3));
set1.symmetric_difference_update(set2);
print(set1);

#isDisjoint -
set1 = set([3,2,1]);
set2 = set([6,4,5]);
print(set1.isdisjoint(set2));

#isSubset-
set1 = set([1,2,3]);
set2 = set([2,3]);
print(set2.issubset(set1));

#isSuperset-
set1 = set([1,2,3]);
set2 = set([2,3]);
print(set1.issuperset(set2));

