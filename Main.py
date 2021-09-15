# Use a dictionary to store information about a person
# you know. Store their first name, last name, age, and
# the city in which they live. You should have keys
# such as first_name, last_name, age, and city. Print
# each piece of information stored in your dictionary.

parents = {
    "first_name": "Bruce",
    "last_name": "Morse",
    "age": 74,
    "city": "San Diego",
}

for key, value in parents.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
