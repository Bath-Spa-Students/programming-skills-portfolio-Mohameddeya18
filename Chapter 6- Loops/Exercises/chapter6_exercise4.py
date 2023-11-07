# Create a list of sandwich orders

sandwich_orders = ["turkey", "ham and cheese", "omlet and cheese", "tuna", "pastrami", "chicken"]

# Create an empty list for finished sandwiches

finished_sandwiches = []

# Loop through the sandwich orders

while sandwich_orders:
    current_order = sandwich_orders.pop(0) 

# Make the sandwich and print a message

    print(f"I made you a {current_order} sandwich.")
    
# Add the finished sandwich to the list

    finished_sandwiches.append(current_order)

# Print the list of finished sandwiches

print("\nFinished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
