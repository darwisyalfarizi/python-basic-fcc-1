# Set

nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)

print(type(nums))
print(type(nums2))

print(len(nums))



# no duplicated allow

nums = {1, 2, 2, 3}
print(nums )


# True is dupe of 1, false is a dupe of 0   True=1 False=0

nums ={1, True, 2, False, 3, 4, 0}
print(nums)


#check if a value  is in set
print(2 in nums)

# you cannot refer to an element in the set with an idex position or key


# add new elements to a set
nums.add(8)
print(nums)


# add elements from one set to another
morenums ={5, 6, 7}
nums.update(morenums)
print(nums)


# update with list, tuple   and dict too\


#merge 2 set

one = {1, 2, 3}
two = {4, 5, 6}

mynewset = one.union(two)
print(mynewset)

# keep only duplicate

one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)


# keep everything except duplicate
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)



