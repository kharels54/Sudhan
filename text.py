guess = []
index = 0
correct = 0
question = 0
print(".....Let's satart the quiz....")
#crate a list of quiz
quiz_questions = [
"When was the New zeland win their frist World Test Campinship ? ", 
"Who's new zeland player have the most wicket in T20 ? ", 
"What is the lowest score of New zeland in T20 ? ", 
"Who is the most wining caption of new zeland cricket team ? "
]


quiz_options = [
"A) june 22,2021" "b) March 23,2022" "C) june23,2021\n", 
"A) Trent boult" "B) Virat kholi" "C) Tim Southee\n",
"A) 50" "B) 40" "C) 60\n", 
"A) kane Williamson " "B) Rohit poudel" "C) Stephen Fleming\n,"
]

answer = ["A" , "C" , "C" , "C"]

for quiz_question in quiz_questions:
  answer = input(quiz_question)
if quiz_options in quiz_options[index]:
 
  print(quiz_options) 
  index +=1
  


guess = input('Select[A,B,C,D]')
