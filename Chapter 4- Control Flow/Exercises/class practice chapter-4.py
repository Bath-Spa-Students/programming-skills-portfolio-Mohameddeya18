# the actual example
Sales=float(input("enter Sales:"))
bonus=0
if Sales > 5000 :
     bonus=50
else:
     bonus=0
print("your bonus: "+str(bonus) )

# sec example/nested desicion structure
earning= int(input("enter your earning per year: "))
Spend = float (input("Enter your spend per year: "))
if earning > 30000:
 if  Spend >=2:
           print("your are eligible for loan")
 else :
           print("your spend is too high ur ending up broke in 5 years ") 
else :
           print("YOUR earning is less than 5000")

# new day new lesson
tempreature=float(input("Enter the weather degree in your city:"))
if tempreature >=60:
       print("your city is not eligible for sports at the moment")
elif tempreature >=40:
        print(" suggested to have a sun protection ")
elif tempreature >=20:
        print("have fun outside :)")
elif tempreature >=0:
        print("u need to wear some heavy clothes")
else :
       print("stay home for your safety")
