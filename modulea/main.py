
print("welcome  to the quiz game")
ans=input("do you want to play the game ? ")

score=0
if ans.lower()=="yes" or ans=="Yes" or ans=="YES":
   print("lets play the game :) ")

   answer=input("what is the capital of INDIA ? ")
   if answer.lower()=="delhi" or answer=="Delhi" or answer=="DELHI":
       print("correct answer")
       score=score+1

   else:
       print("wrong answer")


   answer=input("whats does cpu stands for ? ")
   if answer.lower()=="central processing unit" or answer=="Central Processing Unit" or answer.capitalize=="Central Processing Unit":
       print("correct answer")
       score=score+1

   else:
       print("wrong answer")


   answer=input("In what language .py extension used  ? ")
   if answer.lower()=="python" or answer=="Python" or answer.capitalize=="Python":
       print("correct answer")
       score=score+1

   else:
       print("wrong answer")

   answer=input("GPU stands for  ? ")
   if answer.lower()=="graphics processing unit" or answer=="Graphics Processing Unit" or answer.capitalize=="graphics processing unit":
       print("correct answer")
       score=score+1

   else:
       print("wrong answer")




else:
   print(" Okayyyyy then, Have a nice day Buddy :) , see you later. ")
   quit()

print(f"your score is {score} and you got {score/4*100}% :) ")