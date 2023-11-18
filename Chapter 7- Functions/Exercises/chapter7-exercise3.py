# working in a t-shirt shop
def make_shirt(size, message):
    summary = f"Creating a {size}-sized shirt with the message: '{message}'."
    print(summary)

# Call the function using positional arguments
make_shirt("small", "thank you lil bro")

# Call the function using keyword arguments
make_shirt(size="large", message="thank you big bro")
