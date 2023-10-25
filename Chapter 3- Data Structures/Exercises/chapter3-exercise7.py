# chapter 3 ending :)
places_to_visit = ['London', 'Tokyo', 'Milano', 'New York', 'Barcelona']

print("Original list:", places_to_visit)

print("Sorted list:", sorted(places_to_visit))

print("Original list (still in original order):", places_to_visit)

print("Reverse sorted list:", sorted(places_to_visit, reverse=True))

print("Original list (still in original order):", places_to_visit)

places_to_visit.reverse()
print("Reversed list:", places_to_visit)

places_to_visit.reverse()
print("Back to original order:", places_to_visit)

places_to_visit.sort()
print("Sorted list:", places_to_visit)

places_to_visit.sort(reverse=True)
print("Reverse sorted list:", places_to_visit)
