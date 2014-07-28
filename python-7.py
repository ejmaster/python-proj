"""
    Ask user for username and password
    class customers
          usernanmne, password, money
    ask user withdraw or deposit money
    modify the money

    k = 203
    if ( k == 203):
       k += 123
    k == 326


"""
class BankUser():
#This line tells the name and password.
    def __init__(self):
        self.username="Eric"
        self.password="Bank"
#Template for setting the username and password.
    def set_username(self, new_username):
        self.username = new_username
    def set_password(self, new_password):
        self.password = new_password
#Sets username+password for Eric.   
Eric=BankUser ()
Eric.set_username("Eric")
Eric.set_password("Bank")
#This line tells the name and passwordd.
class Money():
    def __init__(self):
        self.money=0
#Template for setting the money, lose money, or get money.
    def set_money(self, new_money):
        self.money += new_money
    def set_losemoney(self, new_losemoney):
        self.money -= new_losemoney
    def get_money (self):
        return self.money
#Sets self for money.
Eric=Money ()
#While above is true, loop the code.
while True:
#The username and password.
    u= input ( "Username:\n")
    p= input ( "Password:\n")
    if (u=="Eric" and p=="Bank"):
#Verification code.
         a= input ("Where do you live? For verification purpouses.\n")
    if (a=="Earth"):
         z= input ("Wrong answer.\n")
    else:
         print ("Wrong Answer")
    if (z==  "No it isnt"):
         m=input ("What is your favorite word?\n")
    else:
         print ("Wrong answer")
    if (m== "Word"):
         d= input ("Deposit or Withdraw?\n")
    else:
        print ("Wrong answer")
        d = ""
    if (d=="Deposit"):
         w= int(input ("How much?\n"))
         Eric.set_money(w)
    if (d=="Withdraw"):
         t= int(input ("How much?\n"))
         Eric.set_losemoney(t)
#Prints money amount. 
    print ("Money amount\n",Eric.get_money())








