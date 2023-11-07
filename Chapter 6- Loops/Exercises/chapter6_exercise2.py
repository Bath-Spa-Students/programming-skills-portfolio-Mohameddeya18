#loop exercise

while True:
    age = input("Please enter your age")

    age = int(age)

    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

#print the ticket price

    print(f"The cost of your movie ticket is ${ticket_price}.")
