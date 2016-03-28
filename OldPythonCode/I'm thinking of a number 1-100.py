'''
import random                           # we need to have this import to get a randon number generated

list1=[]                                # this is an empty list

                    # do this 10 times
    list1.append(random.randint(1,100)) # append 10 random numbers between 1 to 100 in list
'''


import random
print("Hello;I am thinking of a number 1-100")
list1=[]
for i in range(1): 
    list1 .append(random.randint(1,100));
    import random                           




tried=0                              
while 1:                                
             
        
    else:
        print ("Oops!! not a good number")
        continue                     
    tried = tried+1                     
    if ( guess in list1):               
        print(" My Number is ", list1) 
        print("you win... after ", tried , "times")
        break                         

    else:

        print ("Nah!! You did not get it.... You can say x to Give up. or guess again....")
        guess1=input()                  
        if (is_number(guess1)):         
            guess=int(guess1)           
            tried = tried+1             
            if ( guess in list1):       
                print("you win... after ", tried , "times")
                print(" My Number is ", list1) 
                break                  

        else:                          
            if (guess1.lower() == "x"):
                print(" Ha Ha ... CHICKEN........")
                print(" My Numbers are ", list1) 
                break                     
            else:
                print(" You are Brave. I give you that. Guess Again...")
        
         

print("Hope you liked it") 
                












