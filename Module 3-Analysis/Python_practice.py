##Practice Python
print("Hello World")
type (73.81)
type ("Hello World")
5 + 2 * 3
8 // 5 - 3
8 + 22 * 2 - 4
16 - 3 / 2 + 7 - 1
3 ** 3 % 5
5 + 9 * 3 / 2 - 4

#Lists and Lens
counties = ["Arapahoe", "Denver", "Jefferson"]
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
len(counties_dict)
print(len(counties_dict))
print(counties_dict.keys())

#Dictonary
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)

#If Else and For Loops
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
#F- strings
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")