# advance version of min function

# find name who's length is minimum
names = ["harsh", "ram", "piyush", "nishant"]
print(min(names))  # this print min word not min len word

# using lambda function print minimum length name
print(min(names, key=lambda item: len(item)))

# example 2
student_1 = [
    {"name": "harsh", "age": 20},
    {"name": "ram", "age": 25},
    {"name": "rajesh", "age": 36},
]
# print student detail who's age is minimum
print(min(student_1, key=lambda item: item["age"]))

# print only name of student who's age is min
print(min(student_1, key=lambda item: item["age"])["name"])

# example 3
student_2 = {
    "harsh": {"marks": 59, "age": 20},
    "rajesh": {"marks": 90, "age": 25},
    "ranu": {"marks": 99, "age": 36},
}
# print name who's marks is min
minimum = min(student_2, key=lambda item: student_2[item]["marks"])
print(minimum)

# Example 4
# minimum element till K value
k = 4
test_list = [1, 5, 6, 3, 9, 4, 6, 7]
print(min([i for i in test_list if i <= k]))

# Example 5
# minimum element in tuple list
tuple_list = [(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]

# using lambda function
min_tuple = min(min(tuple_list, key=lambda x: min(x)))
print("minimum value tuple:", min_tuple)

# using comprehension
print(min(j for i in tuple_list for j in i))

# Example 6
# find min element in between perticular range

# using comprehension
test_list = [1, 5, 6, 10, 9, 4, 6, 7]
print(min(test_list[x] for x in range(2, 5)))

# using lambda


# Example 7
# Sort dictionary by max / min element in value list
test_dict = {
    "Gfg": [6, 4],
    "is": [10, 3],
    "best": [8, 4],
    "for": [7, 13],
    "geeks": [15, 5],
}
print(
    {
        key: test_dict[key]
        for key in sorted(test_dict, key=lambda ele: min(test_dict[ele]))
    }
)

# example 8
# print key of  dictionary by value list length
test_dict = {"is": [1, 2], "gfg": [3], "best": [1, 3, 4]}
print(min(test_dict, key=lambda ele: len(test_dict[ele])))


# Example 9
# min in list by dictionary value
test_list = ["gfg", "is", "best"]
test_dict = {"gfg": 56, "is": 12, "best": 76}
print(min(test_list, key=lambda ele: test_dict[ele]))


# Example 10
# print the key of dict who's value key is minimum
nested_dict = {"a": {"key": 3}, "b": {"key": 1}, "c": {"key": 2}}
print(min(nested_dict, key=lambda ele: nested_dict[ele]["key"]))
