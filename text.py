total_question = 8
index = 0
score = 0
print(".....Let's satart the quiz....")
#crate a list of quiz_question and quiz_option
quiz_questions = [
"When was the New zeland win their frist World Test Campinship ? ", 
"Who's new zeland player have the most wicket in T20 ? ", 
"What is the lowest score of New zeland in T20 ? ", 
"Who is the most wining caption of new zeland cricket team ? ",
"Who is the fastest New Zeland bolwler ? ",
"Which New Zeland caption win the most icc Tourments ? ",
"What is the another name of New Zeland ceicket team ? ",
"Who knows as the frist over wicket tacker ?"
]


quiz_option = [
"A) june 22,2021 b) March 23,2022 C) june23,2021\n", 
"A) Trent boult B) Virat kholi C) Tim Southee\n",
"A) 50 B) 40 C) 60\n", 
"A) kane Williamson B) Rohit poudel C) Stephen Fleming\n",
"A) Trent boult B) Lockie Ferguson C) Albert Einsten\n",
"A) Stephen Fleming B) Ronaldo C) Kane Williamson\n",
"A) Kiwi B) Black caps C) Mori/n",
"A) Tim Southee B) Lockie Fergrusom C) Trent boult\n"
]

answer = ["A" , "C" , "C" , "C" , "B" , "C" , "B" , "C"]
#crate a lopp for print each option thats print correctly
for quiz_question in quiz_questions:
    print(quiz_question)
    print(quiz_option[index])
    
    user_input = input("Select [A, B, C, D]: ").upper()
    
    # Check if the guess matches the correct answer in the list
    if user_input == answer[index]:
        print("Correct!\n")
        score = score + 1
    else:
        print("Wrong!\n")
        print(f"The ringht answer was {answer[index]}\n")
        
    # add the item in the lists
    index = index + 1

Per_cent = ( score * 100)/total_question

print(f"Your total score was {score}")
print(f"You got the {Per_cent} percentage")

 


 
  
