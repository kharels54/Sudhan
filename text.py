from re import A


print(".....Let's satart the quiz....")
#crate a list of quiz
quiz_data = [ 
{
"question": "When was the New zeland win their frist WTC"
"option" : ["A) june 22,2021", "b) March 23,2022", "C) june23,2021" ],
"answer" : "A"
},
{
"question": "Who's new zeland player have the most wicket in t 20"
"option" : [ "A) Trent boult" , "B) Virat kholi", "C Tim Southee" ],
"answer" : "C"
} ,
{
"question": "What is the lowest score of New zeland in T20 ? "
"option" : [ "A) 100" , "B) 49", "C 60" ],
"answer" : "C" 
} ,
{
"question": "Who is the most wining caption of new zeland cricket team"
"option": ["A) kane Williamson", "B Rohit poudel", "C) Stephen Fleming"] ,
"answer" : "C"
 }, ]
score = 0
total = quiz_data(len)
for items in quiz_data:
 print(items['question'])
for opt in items(['options']):
 print(items['opt'])
score=+1

if "question" == "answer":
 print('right')
else:
  print('wrong')

percent = (total/score)*100

print(f"you got a {'percent'}")
