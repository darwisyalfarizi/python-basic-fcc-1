# key value


band = {
    "vocals" : "Plant",
     "guitar" : "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)

print(type(band))
print(len(band2))



#access items in dict

print(band["vocals"])
print(band.get("guitar"))


# show list dict key
print(band.keys())

#show list dict values
print(band.values())

#show list key/values pair as tuples
print(band.items())


#verify a key exists

print("guitar" in band)
print("triangle" in band)


#change values
band["vocals"] = "Coverdale"
band.update({"bass" : "JP"})

print(band)


# remove items
band.pop("bass")
print(band)

# add new data
band["drums"] = "Bonham"
print(band)

#remove last item
print(band.popitem()) #tuple
print(band)


#delete and clear item

band["drums"] = "Bonham"
print(band)

del band["drums"]
print(band)


#clear 
band2.clear()
print(band2)

del band2


# copy dict

# band2 = band #create a reference
# print("Bad Copy !")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)


band2 = band.copy()
band2["drums"] = "Dave"
print("good copy!")
print(band)
print(band2)


# use dict to copy
band3 = dict(band)

print("good copy!")
print(band3)


#nested dict

member1 = {
    "name" : "Plant",
    "instrument" : "vocals"
}

member2 = {
    "name" : "Page",
    "instrument" : "guitar"
}

band = {
    "member1" : member1,
    "member2" : member2
}

print(band)

print(band["member1"]["name"])


