# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('karan', 'prashanth', 'santhosh')
sisters = ('lavanya', 'gauthami', 'anusha')
print(brothers)
print(sisters)

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

# How many siblings do you have?
print("Number of Siblings is : ", len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# Modified siblings tuple by created a new tuple parents ,added it to siblings tuple and assigned it to family_members
parents = ('Narsimlu', 'Vijaya')
family_members = siblings + parents
print(family_members)
