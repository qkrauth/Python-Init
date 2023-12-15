value = 1
while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue # when you use CONTINUE it does not print that iteration it just goes back to the op of the loop. ans = 2,3,4,6,7,8,9,10,11
#     print(value)
# else:
#     print("value is now equal to " + str(value))

names = ["Quinten", "Larry", "Brilly"]
# for name in names:
#     print(name)

# for letter in "Mississippi":
#     print(letter)

for name in names:
    if name == "Larry":
        break
    print(name)