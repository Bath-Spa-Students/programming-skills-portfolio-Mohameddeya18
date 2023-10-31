# dictionaries for different pets
pet1 = {"kind": "dog", "owner": "Ahmed"}
pet2 = {"kind": "cat", "owner": "Bibo"}
pet3 = {"kind": "bird", "owner": "harvey"}
pet4 = {"kind": "fish", "owner": "Sarah"}

# Create a list called pets
pets = [pet1, pet2, pet3, pet4]

# Loop through the list and printing information about each pet.
for pet in pets:
    kind = pet["kind"]
    owner = pet["owner"]
    print(f"This is a {kind} and its owner is {owner}.")
