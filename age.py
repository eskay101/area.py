from datetime import datetime 
name = input ( ' enter your name : ' )
age =  int ( input ( ' enter your age : ' ) )
hundred = int ( ( 100 - age ) + datetime . now() . year )
print ( ' you will be this years old ' , (name , age , hundred))
