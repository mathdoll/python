
import def_lib

aStr=def_lib.get_answer("How much money do you have",True)
if (def_lib.is_number(aStr)):           
    a=int(aStr)             
    if a<2000:
        print("Not Rich")
    else:
        print("Rich")
        
else:
     print ("Oops!! not a good number")



