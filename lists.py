users = ["Quinten", "William", "Grace", "Bullocks"]

data = ["Quinten", 19, False]

empty = []

print("Quinten" in users)

print(users[0])
print(users[-1]) # Last value in the list

print(users.index("William"))

print(data[0:2]) # Prints values FROM index 0 to index 2 WITHOUT including index 2

print(len(users))
print(len(empty))

users.append("Peter") # both of these append to the end of the list
users += ["Jack"]
print(users)

users.extend(["Robert", "Benson"]) # pass in another list on the end of the list
print(users)

users.insert(1, "Krauth") # insert a value at the index that you want
print(users)

users[1:3] = ["Rebecca", "Martin"] # how to replace a value in a list
print(users)

print(users.pop()) # removes the last value from the list and returns it
print(users)

del users[1] # deletes user
print(users)


# Tuples

mytuple = tuple(("Quinten", "Fish", 7, True))

anothertuple = (1,2,4,8)

print(mytuple)
print(anothertuple)
print(type(mytuple))

# Tuples are like Lists but the data inside cannot change neither can the order the data is in