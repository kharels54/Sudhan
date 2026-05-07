from re import A


print(".....Let's satart the quiz....")
#crate a list of quiz
quiz_question = {"When was the New zeland win their frist WTC ? " , 
"Who's new zeland player have the most wicket in t 20 ? " , 
"What is the lowest score of New zeland in T20 ? " , 
"Who is the most wining caption of new zeland cricket team ?"}


quiz_option = { "A) june 22,2021", "b) March 23,2022", "C) june23,2021", 
"A) Trent boult" , "B) Virat kholi", "C) Tim Southee",
 "A) 50" , "B) 40" , "C) 60" ,
 "A) kane Williamson", "B) Rohit poudel", "C) Stephen Fleming"}

quiz_answer = { "A" , "C" , "C" , "C"}



score = 0
total = quiz_question(len)
for items in quiz_question:
 print(items['quiz_question'])
for quiz_opt in items(['options']):
 print(items['opt'])
score=+1

if "quiz_question" == "quiz_answer":
  print('right')
else:
  print(f"wrong {'answer'} was the answer" )

percent = (total/score)*100


print(f"you got a {'percent'}")


