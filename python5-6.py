#k= input ( "User Name:\n")
#o= input ( "password\n")
#if (o=="password" ) :
    #print ("Welcome",k,)
    #book= {k: [o]}
#else:
    #print ("Wrong User or Password ")

#print (book.items())
#print out all the key-value pairs inside of book
#for item in book.keys() :
    #if ( item == "eric") :
        #print ("hi")
        #break

class Student():
    def __init__(self):
        self.name="Eric"
        self.age="12"
    def set_age(self, new_age):
        self.age = new_age
    def get_name(self):
        return self.name
Eric=Student ()
Eric.set_age(12)
Bob=Student ()
Bob.set_age(9)
Joe=Student ()
Joe.set_age(5)
Billy=Student()
Billy.set_age(67)
print (Eric.get_name())



