import def_lib



print("This program will tell you wether a certain number or word is a pallendrom or not!")



a=def_lib.get_answer("So don't be a chicken give me a word: ",False)       

b=def_lib.rev(a)

if a==b:
  print ("Yes, This is a pallendrom")
else:
  print ("No,This is not a pallendrom")

