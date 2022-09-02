it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


# Find the length of the set it_companies
print("length of the set it_companies is : ", len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("set after adding 'Twitter' company : ", it_companies)

# Insert multiple IT companies at once to the set it_companies
# Created a new set with the multiple IT companies and added this set to the it_companies set by using update method.
companies = {'Accenture', "Wipro", "Infosis"}
it_companies.update(companies)
print("set after adding multiple IT Companies : ", it_companies)

# Remove one of the companies from the set it_companies
# removed 'IBM' from the set it_companies
it_companies.remove('IBM')
print("set after removal of IBM company : ", it_companies)

# What is the difference between remove and discard
# Ans:
# If the item that you are supposed to remove does not exist in the set, remove() will raise an error whereas
# discard() will NOT raise an error.


# Join A and B (joined the sets A and B using union method)
set3 = A.union(B)
print("New set after joining A and B : ", set3)


# Find A intersection B
set4 = A.intersection(B)
print("Intersection of A and B is : ", set4)


# Is A subset of B (using issubset method found whether A is subset of B)
s = A.issubset(B)
print(s)  # returns true

# Are A and B disjoint sets (using isdisjoint method found whether A and B are disjoint sets)
d = A.isdisjoint(B)
print(d)  # returns false

# Join A with B and B with A (joined A with B and B with A using update method)
B.update(A)
print(B)
A.update(B)
print(A)

# What is the symmetric difference between A and B
# The symmetric difference between A and B with given data is {27, 28}
# The symmetric difference between A and B is None/ empty set if we execute it after performing above join step.
sd = A.symmetric_difference(B)
print("symmetric difference between A and B is : ", sd)

# Delete the sets completely
# Deleted the sets using del keyword
del A
del B

# Convert the ages to a set and compare the length of the list and the set.
age = [22, 19, 24, 25, 26, 24, 25, 24]
ageSet = set(age)
print("converted age set is : ", ageSet)
print("Length of age list is : ", len(age))
print("Length of age set is : ", len(ageSet))
