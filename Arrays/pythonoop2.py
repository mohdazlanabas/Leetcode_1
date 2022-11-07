# encapsulation
# inheritance
# polymorhpism

# inheritance
class User:
    def log(self):
        print(self)

# polymorhpism
class Teacher(User):
    def log(self):
        print("I am a teacher")

class Customer(User):
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def log(self):
        print("I am a customer")

    # encapsulation
    @property # decorator
    def name(self):
        print("Setting name")
        return self._name # _ means private

    @name.setter
    def name(self, name):
        print("Getting name")
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    def update_memebership(self, new_membership):
        print("Calculating cost or other methods")
        self.membership_type = new_membership

    def read_customer(self):
        print("Reading customer from DB")
        # static method, attached directly to class

    def __str__(self):
        print("Converting to string")
        return self.name + " " + self.membership_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False

    __hash__ = None
    __repr__ = __str__

users = [Customer("Caleb", "Gold"),
             Customer("Brad", "Bronze"),
             Teacher()]

# Customer.read_customer()
# Customer.print_all_customers(customers)
# print(customers[0] == customers[1])
# print(customers)
# # del customer[0].name
# print(customers[0].name)
# customers[1].log
# customers[2].log

for user in users:
    user.log()