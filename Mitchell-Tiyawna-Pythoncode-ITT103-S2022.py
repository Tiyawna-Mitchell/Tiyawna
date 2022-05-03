#Author:Tiyawna Mitchell
#Date: May 3,2022
#Course:ITT103
#Purpose: To Calculate Commission

print('Calculating Commission')
print('Enter Sales')
sales=int(input(' '))
print('Enter salespersonid')
sales=int(input(' '))
print('Enter class')
class1=int(input(' '))
if class1==1:
 if sales<=1000:
  print (0.06*sales)
 elif 1000<sales<=2000:
   print(0.07*sales)
else:
   print(0.1*sales)
if class1==2:
 if sales <=1000:
   print (0.4*sales)
else:
 print(0.06*sales)
 if class1==3:
  print(0.045*sales)

  
  
        


