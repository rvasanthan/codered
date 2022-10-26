#Empty Dictionary
empty_dict = {};
print(empty_dict);

# New Dictionary - You can use any types in the same dictionaries as values.
new_dict = {"name": "John", "Location" : "Weehawken", "Age" : 25,  "perm" : True};
print(new_dict);

#what if I change the Keys? Keys can also be any type
new_dict = {True: "John", "Location" : "Weehawken", "Age" : 25,  "perm" : True};
print(new_dict);

# Properties of Dictionaries
# 1) Dictionaries are Ordered
new_dict = {"name": "John", "Age" : 25, "Location" : "Weehawken",  "perm" : True};
print(new_dict);

# 2) The Keys must be unique.
new_dict = {"name": "John", "Location" : "Weehawken", "Age" : 25,  "perm" : True, "name" : "Doe"}
print(new_dict);

# 3) The keys must be immutable
tup = (1,2,3,4);
print(tup);
print(hex(id(tup)));
#tup[0] = 5; --> Immutable
#print(tup);
#print(hex(id(tup)));
tup2 = (1,2,3,4)
print(tup2);
print(hex(id(tup2)));

# mutable
list1 = [1,2,3,4];
print(list1);
print(hex(id(list1)));

list2 = [1,2,3,4];
print(list2);
print(hex(id(list2)));

list2[0] = 5
print(list2);
print(hex(id(list2)));

#Mutable and Immutable in Dictionaries
my_mut_dict = {(2,2) : "John", (3,3) : "Doe"};
print(my_mut_dict);

#You can't use any mutable objects as a key
#my_immute_dict = {[2,2] : "John", [3:3] : "Doe"};
#print(my_immute_dict);

#inserting an item into a dictionary
dict_insert_demo = {"name": "John", "Age" : 25, "Location" : "Weehawken",  "perm" : True};
print(dict_insert_demo);
dict_insert_demo["zip"] = "08823";
print(dict_insert_demo);

#Accessing the item from a dictionary
print(dict_insert_demo["name"]);

#Inserting a duplicate
dict_insert_demo = dict_insert_demo = {"name": "John", "Age" : 25, "Location" : "Weehawken",  "perm" : True, "name" : "Jane"};
print(dict_insert_demo);

#Creating dict() using constructor
dict_using_constructor = dict({"firstname":"John", "lastname": "Doe"});
print(dict_using_constructor);

#Which means we have type / object dict in python
print(type(dict_using_constructor));

#Removing an item from dictionary
remove_demo_dict = {"name": "John", "Age" : 25, "Location" : "Weehawken",  "perm" : True};
print(remove_demo_dict);
remove_demo_dict.pop("perm");
print(remove_demo_dict);

# Removing the last added item from the dictionary
remove_demo_dict = {"name": "John", "Age" : 25,  "perm" : True, "Location" : "Weehawken"};
print(remove_demo_dict);
remove_demo_dict.popitem();
print(remove_demo_dict);
# What will happen in Python 3.6 if I use popitem()? -- food for thoughts

# Remove all the items from a dictionary
clear_all_demo = {"name": "John", "Age" : 25,  "perm" : True, "Location" : "Weehawken"};
print(clear_all_demo);
clear_all_demo.clear();
print(clear_all_demo);


# what if I access an empty dictionary? --> throw an error
#print(clear_all_demo["name"]);

#Find the length of dictionaries
new_dict = {"name": "John", "Age" : 25,  "perm" : True, "Location" : "Weehawken"};
print(len(new_dict))
new_dict.popitem();
print(len(new_dict));

# Get all the Keys from a dictionary
new_dict = {"name": "John", "Age" : 25,  "perm" : True, "Location" : "Weehawken"};
print(new_dict.keys());

#Get all the Values from a dictionary
print(list(new_dict.values()));

#Iterating through the list of Keys or Values
for i in range(0, len(new_dict.keys())):
    print(new_dict[list(new_dict.keys())[i]])

#Check if the the key or value exists in a dictionary
new_dict = {"name": "John", "Age" : 25,  "perm" : True, "Location" : "Weehawken"};
print("name" in new_dict);  #--> By default searched the new_dict.keys() iterable
print("John" in new_dict.values())
# The "in" operator in python will be slower when it is used with List. Because it uses a search algorithm which is goint to get slower
# as the size of list getting bigger.
# With respect to dictioary, this uses the hashtable algorithm which have consistent retrieval time regardless of the size of the Dictionary

#update() function
dict1 = {"firstname": "John", "Age" : 25,  "perm" : True, "Location" : "Weehawken"};
print(dict1)
dict1.update({"lastname" : "Doe"});
print(dict1);
# So it basically combines 2 list. You can also use it to insert an item into the dictionary.
dict2 = {"zipcode" : "08823"};
dict1.update(dict2);
# What happens here -->
dict2.update(dict1)
dict2.popitem();
print(dict2);

#What if we have similar keys in 2 dictionaries while merging. It just simpley overwrites. 
dict3 = {"firstname": "Jane", "Age2" : 25,  "perm2" : True, "Location2" : "Weehawken"};
dict3.update(dict1);
print(dict3);

#zip() function
list1 = [1,2,3];
list2 = ["John", "Doe", "Jane"];

zipped_dict = dict(zip(list1, list2));
print(zipped_dict);

# what will happen if we have lists of 2 different size and you use it in zip?
list1 = [1,2,3];
list2 = ["John", "Doe", "Jane", "Doe"];
zipped_dict = dict(zip(list1, list2));
print(zipped_dict);
#It ignores the last item which is not matching the keys

#Using get() method
print(zipped_dict.get(1));
# why do we have a get() method and how it is different --> this is a safe method which returns None when the item is not present
print(zipped_dict.get(7));

#Copy function
copy_dict = zipped_dict.copy();
print(copy_dict); print(zipped_dict);
print(hex(id(copy_dict)));
print(hex(id(zipped_dict)));
#What if I modify the copy dict?
copy_dict.update({4:"foo"});
zipped_dict.update({5:"bar"});
print(copy_dict);
print(zipped_dict);

#Copy Function vs Assignment
assign_dict = zipped_dict; #--> What happens when I do an assignment.
print(hex(id(zipped_dict)));
print(hex(id(assign_dict)));
print(zipped_dict);
assign_dict.update({4:"Foo"});
print(zipped_dict);

#setDefault()
default_dict = {"firstname": "Jane", "Age2" : 25,  "perm2" : True, "Location2" : "Weehawken"};
print(default_dict);
# Key and value both don't exist
value = default_dict.setdefault("zipcode", "08823");
print(default_dict);
print(value);

# Key exists and value is different
value = default_dict.setdefault("firstname", "John");
print(default_dict);
print(value);

# Key doesn't exist and we are not passing a value to it
value = default_dict.setdefault("middlename");
print(default_dict);
print(value);

#fromkeys() function creates a new dictionary with default values for all the specified keys.
# if default value is not specified, all keys are set to None.

from_keys_demo = dict.fromkeys(["firstname", "lastname"], "John");
print(from_keys_demo);

from_keys_demo = dict.fromkeys(["firstname", "lastname"]);
print(from_keys_demo);

#Nested Dictionary

# Dictionary Comprehension
new_dict = dict();
new_dict[0] = 0;
new_dict[1] = 1;
new_dict[2] = 4;
new_dict[3] = 9;
new_dict[4] = 16;

print(new_dict);
#Just in a for loop
for i in range(4):
    new_dict[i] = i*1
print(new_dict);

#Comprehensed
new_dict = {x: x*x for x in range(0,5)};
print(new_dict);

#Another Example - Problem --> Given a String RED --> I need a dict R: RRR, E: EEE, D: DDD
new_dict = {c:c*3 for c in "PYTHON"};
print(new_dict);

#Another Example -> First letter of the list item will be the key and value will be the upper cased list item.
list1 = ["Red", "Blue", "Green"];
new_dict = {c.lower() : c.upper() for c in list1};
print(new_dict);

#Extracting the subset from a dictionary
orig_dict = {x: x*x for x in range(0,11)};
selectedKeys = [0, 4, 8];
new_dict = {x: orig_dict[x] for x in selectedKeys};
print(new_dict);

#Initialize a dictionary with comprehension.
new_dict = {x:0 for x in range(0,11)};
print(new_dict);

#Filter items from a dictionary
orig_dict = {x: x*x for x in range(0,11)};
keys_to_remove = [0, 4, 8];
new_dict = {x:orig_dict[x] for x in orig_dict.keys() - keys_to_remove};
print(new_dict);

#Lets to a Reverse mapping of dictionary
orig_dict = {x: x*x for x in range(0,11)};
new_dict = {orig_dict[x] : x for x in orig_dict.keys()};
print(new_dict);

#If clause in Dictionary Comprehension
new_dict = {x:x*x for x in range(11) if x%2 == 0}
print(new_dict);


