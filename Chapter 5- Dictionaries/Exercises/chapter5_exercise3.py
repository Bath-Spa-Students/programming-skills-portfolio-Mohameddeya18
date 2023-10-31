# Define the glossary (dictionary)
glossary = {
    "variable": "A container that stores data that can be changed during the execution of a program.",
    "function": "A block of reusable code that performs a specific task.",
    "loop": "A control structure that allows a block of code to be executed repeatedly based on a condition.",
    "string": "A sequence of characters, typically used to represent text.",
    "list": "An ordered collection of items, which can be of any data type.",
    "dictionary": "A data structure that stores a collection of key-value pairs.",
    "tuple": "An ordered, immutable collection of elements.",
    "module": "A file containing Python definitions and statements.",
    "method": "A function associated with a class or an instance of a class.",
    "class": "A blueprint for creating objects, providing initial values and behavior.",
}

# Print each word and its meaning
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")
