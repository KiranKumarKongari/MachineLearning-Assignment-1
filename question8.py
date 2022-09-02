# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# “The area of a circle with radius 10 is 314 meters square.”

radius = 10
area = 3.14 * radius ** 2
result = "radius =  {radius}\narea = 3.14 * radius ** 2\n" \
       "The area of a circle with radius {radius} is {area} meters square.".format(radius=10, area=3.14 * radius ** 2)
print(result)

