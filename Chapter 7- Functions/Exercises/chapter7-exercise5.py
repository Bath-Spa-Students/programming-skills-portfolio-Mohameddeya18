# describing cities

def describe_city(city, country="america"):
    description = f"{city} is in {country}."
    print(description)

# Call the function for three different cities

describe_city("london", "united kingdom")
describe_city("Paris", "France")
describe_city("New York") #this will use default country value
