# SETS
# Creating a set
thisset = {"Alvin", "Adams", "Asiachi"}
print(thisset)


#Making a set using set()constructor
thisset = set(("King", "Stephen", "Curry")) 
print(thisset)

#Duplicates are not allowed
thisset = {"Alvin", "Adams", "Asiachi","Adams"}
print(thisset)

#Accessing set items
thisFruits = {"Orange", "Banana", "Melons","Apples"}
for x in thisFruits:
    print(x)


#Checking for an item in a set
thisPeople ={"student", "teacher", "driver"}
print("driver" in thisPeople)


#Add Items to a Set
thisCars ={"bugatti", "lambo", "mclaren"}
thisCars.add("jeep")
print(thisCars)