# Dictionaries:
# Dictionaries are like Objects as in they are used for KEY VALUE PAIRS

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

bandtwo = dict(vocals="Plant", guitar="Page")

print(band)
print(bandtwo)
print(type(band))
print(len(bandtwo))

# Access items in Dict
print(band["vocals"])
print(band.get("guitar"))

# Return all keys
print(bandtwo.keys())

# Return all values
print(band.values())

# Return the KEY VALUE PAIRS as tuples
print(band.items())

# Nested Dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
# members1 & 2 are the KEYS
band = {
    "member1": member1,
    "member2": member2
}

print(band)

print(band["member1"]["name"])


# Sets:

nums = {1, 2, 3, 4}
numstwo = set((1, 2, 3, 4))

print(nums)
print(numstwo)

# In sets NO DUPLICATES ARE ALLOWED

badnums = {1, 2, 3, 3}
print(badnums)

# programming shortcut True generally means 1 ans False generally means 0