
fruits = ["apple", "banana", "cherry"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

fruits[1] = "Blueberry"
# print(fruits)

fruits.append("berry")
# print(fruits)

fruits.remove("apple")
# print(fruits)

more_fruits = ["mango", "grape"]
fruits.extend(more_fruits)

# print("After extend: ", fruits)

fruits.insert(1, "blueberry")

# print("after insert:", fruits)

popped = fruits.pop(3)
# print("after popped: ", fruits)
# print("Pop fruit", popped)

index_of_cherry = fruits.index("cherry")
# print("index of: ", index_of_cherry)


packed_tuple = ("apple", "banana", "cherry")

(fruit1, fruit2, fruit3) = packed_tuple

# print("Fruit 1:", fruit1)
# print("Fruit 2:", fruit2)
# print("Fruit 3:", fruit3)


my_dict = {
    "name": "Jenia",
    "age": 34,
    "city": "USA"
}

# print("Entire Dictionary:", my_dict)
# print("name:", my_dict["name"])
# print("age:", my_dict["age"])
# print("city:", my_dict["city"])

my_dict["email"] = "jenia@gmail.com"
# print("after add email:", my_dict)


my_set = {1, 2, 3, 4, 5}

my_set.add(6)
print("after add element:", my_set)
my_set.add(3)
print("after add dublicate element:", my_set)

set_a = {1, 2, 3, 4}
set_b = {2, 5, 4, 6, 7, 1}

union_set = set_a.union(set_b)
print("Union set_a and _ set_Bb:", union_set)

interSection = set_a.intersection(set_b)
print("InterSection set_a and _ set_Bb:", interSection)

difference_set = set_a.difference(set_b)
print("Difference set_a and _ set_Bb:", difference_set)
