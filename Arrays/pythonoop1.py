# class
# methods
# static method
# overriding

class Customer:
        def __init__(self, name, membership_type):
            # def is method
            # init is initializer or constructor
            # name / membership_type are parameters
            self.name = name
            self.membership_type = membership_type
            # print("customer created")

        def update_memebership(self, new_membership):
            print("Calculating cost or other methods")
            self.membership_type = new_membership

        # static method - no self
        def read_customer(self):
            print("Reading customer from DB")
            # static method, attached directly to class

        # overriding -has self no parameters
        def __str__(self):
            print("Converting to string")
            return self.name + " " + self.membership_type

        def print_all_customers(customers):
            for customer in customers:
                print(customer)

        def __eq__(self, other): # comparison to check objects not data (memory)
            if self.name == other.name and self.membership_type == other.membership_type:
                return True
            return False

        __hash__ = None
        __repr__ = __str__

        # all above are in the class

# c = Customer("Caleb", "Gold")
# caleb and gold are arguments
# print(c.name, c.membership_type)

customers = [Customer("Caleb", "Gold"),
             Customer("Brad", "Bronze")]

Customer.read_customer()

# without def __str__
# print("Before: " + customers[1].membership_type)
# customers[1].update_memebership("Gold")
# print("After: " + customers[1].membership_type)

# with def __str__
# print(customers[1])
# customers[1].update_memebership("Gold")
# print(customers[1])

Customer.print_all_customers(customers)

# use the def __eq__ method
print(customers[0] == customers[1])

# after without __repr__
print(customers)