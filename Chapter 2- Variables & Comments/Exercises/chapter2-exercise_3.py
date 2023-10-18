# Define the name with whitespace
person_name = "\t  \n   Messi   \t  \n"

# Print the name with whitespace
print(f'Name with whitespace: "{person_name}"')

# Strip the whitespace using lstrip(), rstrip(), and strip()
stripped_left = person_name.lstrip()
stripped_right = person_name.rstrip()
stripped_both = person_name.strip()

# Print the stripped names
print(f'Left stripped: "{stripped_left}"')
print(f'Right stripped: "{stripped_right}"')
print(f'Both sides stripped: "{stripped_both}"')
