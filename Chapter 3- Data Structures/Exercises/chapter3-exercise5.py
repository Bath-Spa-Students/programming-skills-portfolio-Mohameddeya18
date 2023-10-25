Guests = ['Lionel messi', 'Neymar JR', 'Zlatan ibrahimovic' , 'barbie']

Guest_cant_make_it = 'Zlatan ibrahimovic'
print(f"for some reason, {Guest_cant_make_it} can't make it to the dinner.")

new_Guest = 'michael jackson'
Guests.remove(Guest_cant_make_it)
Guests.append(new_Guest)

print(f"\nNew list of guests:")
for guest in Guests:
    print(guest)

for Guest in Guests:
    print(f"\nDear {Guest}, you are invited to dinner. I would be honored to have your presence.")
