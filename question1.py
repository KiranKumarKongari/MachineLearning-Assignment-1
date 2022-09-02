# imported the median package to calculate median
from statistics import median

# Created a list named ages contains positive integers
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sorted the ages list in ascending order using sort function
ages.sort()

# Finding the min value using min function and printing the result
minValue = min(ages)
print("Minimum value in the ages list is :", minValue)

# Finding the min value using max function and printing the result
maxValue = max(ages)
print("Maximum value in the ages list is :", maxValue)

# Adding the min and max value again to the ages list using append function and displayed the resultant list
ages.append(minValue)
ages.append(maxValue)
print("List after adding min and max value again : ", ages)

# Sorted the ages list again in order to find the median
ages.sort()
print("Sorted List after adding min and max value again : ", ages)

# Finding the median of the ages using the median function
print("Median of numbers in the ages list is : ", median(ages))

# Calculated the average of the numbers in the ages list and displayed it
average = sum(ages)/len(ages)
print("Average of numbers in the ages list is : ", average)

# Calculated the Range of ages list and displayed it
rangeOfAges = maxValue-minValue
print("Range of ages is : ", rangeOfAges)


