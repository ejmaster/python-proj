stuff  =  ["Apples","Bell Peppers","Carrots","Eggs","Oranges","Mangoes"]

def hello(user) :
    if (user == "Minecraft") :
        print ("Hi")
    else :
        print ("Error")
hello("Minecraft")

k= input ("What is my name?")
w= input ("Do you like cake?")
u= input ("Is this quiz awesome?")

if (k=="Eric" and w=="Yes" and u== "No") :
        print ("Three questions correct")
elif (k=="Eric" and w=="Yes" or k=="Eric" and u=="No" or w=="Yes" and u== "No" ) :
        print ("Two questions correct")
elif (k== "Eric" or w== "Yes" or u=="No") :
        print ("One question correct")
else :
        print ("No questions correct! Sorry!")

numWrong =0
while (numWrong<5):
    answer = input ("Is 'no' the next thing you're going to say?")
    if (answer == "Probably not"):
        print ("correct")
        break
    elif (answer != "Probably not") :
        numWrong +=1
        print ("Incorrect")
    else :
        break



