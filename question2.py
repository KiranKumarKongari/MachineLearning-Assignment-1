# Created an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Harry"
dog["color"] = "light yellow"
dog["bread"] = "Labrador Retriever"
dog["legs"] = 4
dog["age"] = "Male"

print(dog)

# Created a student dictionary and added first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary
student = {
  "first_name": "Kiran Kumar",
  "last_name": "Kongari",
  "gender": "Male",
  "age": 24,
  "marital status": "Single",
  "skills": ["C#", "Dot-Net", "Python"],
  "country": "India",
  "city": "Hyderabad",
  "address": "Telangana"
}

# Get the length of the student dictionary
print("Length of the student dictionary is : ", len(student))

# Get the value of skills and datatype of it.
x = student.get("skills")
print("Values of skills is : ", x)
print("Type of the skills item is : ", type(x))

# Modified the skills values by adding one more skill java
student["skills"].append("java")
print("List after adding another skill : ", student)

# Get the dictionary keys as a list
k = student.keys()
print("keys in the student list is : ", k)

# Get the dictionary values as a list
v = student.values()
print("Values in the student list is : ", v)
