calculation_to_units = 24
name_of_unit = "hours"

# function syntax
def days_to_units():
    print("output inside a function")

days_to_units()


# parameterized function
def parameters(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")

parameters(35)


def dual_parameters(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)

dual_parameters(30, "yo")