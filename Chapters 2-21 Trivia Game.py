#This program reads input from a .txt file and uses it as data for a simple trivia game.
import random
print('Hello user and welcome to the Chapters 2-21 Trivia Game!')
question = ()
Answers_Correct = 0
with open("Trivia Questions.txt", "r") as a:#Opening the file as a variable with a 'with' statement saves me the hassle of opening and closing it manually.
    Switch = True
    while True:
        while Switch == True:#This switch allows for swapping between the multiple choice loop and the true/false loop.
            q = a.readline()
            while q:#This loop accounts for multiple choice questions.
                question = q
                print(question)
                Choice1 = a.readline()
                print(Choice1)
                Choice2 = a.readline()
                print(Choice2)
                Choice3 = a.readline()
                print(Choice3)
                Choice4 = a.readline()
                print(Choice4)
                i = input('Enter the letter corresponding to the answer you choose:')

                Ans = a.readline()
        
                if i == Ans:
                    print('Correct answer!')
                    Answers_Correct = Answers_Correct + 1
                else:
                    print('Incorrect answer!')
                    print(Ans)

                Switch = False
                break

        while Switch == False:#This switch allows for swapping between the multiple choice loop and the true/false loop.
            r = a.readline()
            while r:#This loop accounts for True/False questions.
                question = r
                print(question)
                i = input('True/False:')
                Ans = a.readline()

                if i == Ans:
                    print('Correct answer!')
                    Answers_Correct = Answers_Correct + 1

                else:
                    print('Incorrect answer!')
                    print(Ans)

                Switch = True
                break

                  
    

