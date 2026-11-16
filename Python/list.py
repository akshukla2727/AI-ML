marks = [97, 94, 34, 65, 78]
print(marks)
print(type(marks))

# indexing from 0 to len(marks)-1
# we can store diff types of data in one list
# string => immutable && list => mutable
# slicing same as string: marks[1:4] also can negative indexing also possible

# append(data) => add data at the end
# sort() => sort in ascending order
# sort(reverse=True) => sort in decending order
# reverse() => reverse the list
# insert(idx, el) => insert el at index idx
# remove(2) => first occur 2 will get remove from list
# pop(idx) => remove el from index idx

# TUPLE
# this is tuple and this is mostly as like as string means tuple is immutable
list = (87, 54, 67, 98, 43)

tup = (1,)
tup1 = (1)
# this is tuple
print(type(tup))
# this is simple integer
print(type(tup1))

# count(el)
# index(el)
# for palidrome first copy() then reverse then check for same list or diff ya phir if-else
