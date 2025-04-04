# test.py

Base = __import__('models/base').max_integer

# Create an instance without passing an id
b1 = Base()
print(b1.id)  # Output: 1 (since this is the first object)

# Create another instance without passing an id
b2 = Base()
print(b2.id)  # Output: 2 (automatically incremented)

# Create an instance with a specific id
b3 = Base(42)
print(b3.id)  # Output: 42 (id provided manually)
