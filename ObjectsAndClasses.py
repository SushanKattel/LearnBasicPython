#This program is for working with object and classes in python


#class employee:
#    pass  # If you want to keep it empty, use this or else there will be error !!

#emp1 = employee()
#emp2 = employee()

#emp1.firstname = "Shyam"
#emp1.lastname = "Kumar"
#emp1.email = "shyam.kumr@company.com"
#emp1.pay = 50000

#emp2.firstname = "Shyam"
#emp2.lastname = "Kumar"
#emp2.email = "shyam.kumr@company.com"
#emp2.pay = 50000

#print(emp1.email)

# To avoid this repetition which is tidious, we use the concept of classes and objects.


class employee:
    # def __init__(self):      # This is initializer or constructor !! After self, we initialize arguments we want to give.
    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname    #self.jpt = firstname.. it is like above, emp1.firstname = "shyam"
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + "." + lastname + "@company.com"

    def fullname(self, ):
        return "{} {}" .format(self.firstname,self.lastname)  # Look below about this

emp1 = employee("Shyam", "Kumar", "50000")
print(emp1)  # Gives the Address of memory location.
print(emp1.firstname)
print(emp1.email)

#print("{} {}".format(emp1.firstname,emp1.lastname))  # This is tidious so, we creste it in class as fullnname

print(emp1.fullname())
# print(employee.fullname(emp1)) # The above line transforms to this during execution







