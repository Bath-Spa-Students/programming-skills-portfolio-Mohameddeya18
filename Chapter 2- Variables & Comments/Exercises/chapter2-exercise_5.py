# Define the cost of one USB stick and the total budget
usb_stick_cost = 6
total_budget = 50

# Calculate how many USB sticks she can buy
num_usb_sticks = total_budget // usb_stick_cost

# Calculate how many pounds she will have left
remaining_budget = total_budget % usb_stick_cost

# Print the results
print(f"She can buy {num_usb_sticks} USB sticks.")
print(f"She will have £{remaining_budget} left.")
