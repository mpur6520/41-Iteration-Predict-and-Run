#Maru Puran
#November 2, 2023
# gain a better understanding of while loops and different types of conditions they have as well as how they work

# Example code 1

# Add comments to each line to say whehter it is inside or outside the loop and what it does.

# Explain the circumstances in which the loop will run.

#overall code in example 1 asks the user what the capital of france is and keeps running and asking until they get it right; this is an example of a loop ending because of user input


#both of the following lines of code are out of the loop
print("What is the capital of France? ") #this prints the words "what is the capital of france" for the user to see on the output screen, it is not in the loop
answer = input() #this creates the variable answer and stores the user's answer to the previous question what's the capital of france inside of it, allows the user to input an answer using the input function and is not inside of the loop

#paris is the correct answer for this question, so create a loop that will allow the user to keep guessing until they get the right answer; bases this off the user's input stored in answer
while answer != "Paris": #run this loop for as long as the user's answer is not "paris" because it's the incorrect answer (begins the loop but outside of the loop)
  print("Incorrect! Try again.") #prints words "incorrect try again" on the output screen to let the user know the answer they typed in is incorrect (inside of the loop)
  answer = input("What is the capital of France? ") #allows the user to retry, asks them the same question ("what is the capital of france") and stores the user's response in the variable answer, then runs the loop again to see if they got it right this time (inside of the loop)

#this loop will only terminate if the user types in the answer "Paris" exactly as is with a capital first letter -- the code can be improved because it can be changed to allow the user to type in the answer in any case (ex. capital or lowercase or with a space or without)

print("Correct!") #this is not in the code, we can tell because it's not indented beneath it; tell the user their answer is "correct" on the output console

# Example code 2

#the overall code of example code 2 prints out a counter as long as the counter is less than 5, this is an example of a count variable ending the code

counter = 1 #sets the variable counter = to 1 and establishes it, this code is outside the loop

while counter < 5: #this starts the loop using the while function, initializes the loop but is outside of the loop -- condition is that the counter is less than 5, the following indented code will run as long as this is true
  print("This code is inside the loop") #prints the words "this code is inside the loop" on the console log for the user to see, this code is inside the loop, this is printed 4 times
  counter += 1 #this adds 1 to the counter adding it to the previous one (1 + previous counter variable value), this is inside the loop -- this is what allows the count variable to change and therefore the code will eventually terminated