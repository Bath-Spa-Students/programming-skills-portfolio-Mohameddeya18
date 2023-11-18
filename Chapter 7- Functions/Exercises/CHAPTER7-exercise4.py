# making shirt with messages

def make_shirt(size="large", message="thank you big bro"):
    summary = f"Creating a {size}-sized shirt with the message: '{message}'."
    print(summary)

# Create a large shirt with the default message
make_shirt()

# Create a medium shirt with the default message
make_shirt(size="medium")

# Create a shirt of any size with a different message
make_shirt(size="small", message="thank you Lil bro")
