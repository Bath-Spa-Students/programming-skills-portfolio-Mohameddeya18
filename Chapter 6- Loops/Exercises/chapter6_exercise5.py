# Modify sandwich_orders to include 'pastrami' multiple times
sandwich_orders = ["turkey", "ham and cheese", "veggie", "tuna", "pastrami", "pastrami", "chicken", "pastrami"]

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Print message about running out of pastrami
print("Sorry, we've run out of pastrami!")

# Remove all occurrences of 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Take the first sandwich order
    
    # Make the sandwich and print a message
    print(f"I made your {current_order} sandwich.")
    
    # Add the finished sandwich to the list
    finished_sandwiches.append(current_order)

# Print the list of finished sandwiches
print("\nFinished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
