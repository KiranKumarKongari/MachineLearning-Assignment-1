# Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
# kilograms in a separate list using Loop. N: No of students (Read input from user)
# Ex: L1: [150, 155, 145, 148]
# Output: [68.03, 70.3, 65.77, 67.13]

print("Enter the No of Students")
# n is variable which represents no of students to which the user has to provide the value
n = int(input())
i = 0
# Declared to empty lists L1 and L2
L1 = []
L2 = []
if n > 0:
    print("Enter the weights in lbs")
    # first loop to read weights and add them to a list L1
    while i < n:
        L1.append(int(input()))
        i = i+1
    print("List containing the weights in lbs : ", L1)  # display the list L1
# Second loop to covert the weights in lbs to kgs and add them to a list L2
for w in L1:
    L2.append(float("{:.2f}".format(w * 0.45359237)))
print("List containing the weights after converted to kgs : ", L2)  # display the resultant list L2






