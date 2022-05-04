# Define a Function
def my_dict(d):
    for key,value in d.items():
        if type(value) == dict:
            print(key)
            my_dict(value)
        else:
            print(key,value)

# Sample Data
my_obj={"a":{"b":{"c":"d"}}} 

# Function Call
my_dict(my_obj)
        