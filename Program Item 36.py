# Author: Renato Baer Svirsky
# Python Version: 2.7.12
#Purpose: Item 36 of The Tech Academy (Portland,OR) Python Course

"""

Follow the instructions:
Use comments in your program to denote where you demonstrate each step. If there are any concepts you are not able to demonstrate, research them online first. If you still have trouble, ask an Instructor for assistance. 
1. Assign an integer to a variable
2. Assign a string to a variable
3. Assign a float to a variable
4. Use the print function and .format() notation to print out the variable you assigned  
5. Use each of these operators 
6. Use of logical operators: and, or, not
7. Use of conditional statements: if, elif, else
8. Use of a while loop
9. Use of a for loop
10. Create a list and iterate through that list using a for loop to print each item out on a new line
11. Create a tuple and iterate through it using a for loop to print each item out on a new line
12. Define a function that returns a string variable
13. Call the function you defined above and print the result to the shell

"""


#Assign an integer, a float and a string to different variables
# I made a program with a couple of the tasks...the others are individually at the end of the code
#Start the program
def start(current=0,birth=0):
    birth=BirthYear(birth)
    current=CurrentYear()

#Define the year
    
def CurrentYear():
    x=2016
    return x

#ask the year of birth for the user
def BirthYear(birth):
    stop = True
    while stop:
        birth = int(raw_input("\nWhen were you born? Type the year: "))
        while birth==0 or birth>2016:
             birth = int(raw_input("\nImpossible! When were you born? Type the year: "))#loop in case the user types 0                        
        else:
            age=2016-birth
            print ("\nYou have ")+str(age)+(" years old") #here you need to turn the functin age into a string in order to concatenate with othr texts
            if age > 19:
                print 'You are an adult'
            elif age>=13 and age<=19:
                print 'You are a teenager'
            else:
                print 'You are a child'
            print ("\nThanks!")
            
        stop=False
 
if __name__ == "__main__":
    start()

#creating a task that uses the for loop with  a tuple

classmates = ['Renato','Felipe','Rodrigo']
for mate in classmates:        
   print 'Abreviacao :'+'%.2s'%(mate).lower()

print "These are the the classmates nicknames!"

#creating a task that uses the for loop with  a list

classmates_grades=[
    ['Renato',7.325],
    ['Felipe',6],
    ['Rodrigo',3.75]]

for grade in classmates_grades:
    print '%04.2f'%grade[1]
    

 
# tasks apart from the program
#print the variables using .format (%)

y=2.625
x=15


print '%6d'%(x)



# Use the operators

print (x+y+12)
print ((x-y)/3)
print (x**y)


