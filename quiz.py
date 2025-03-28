print("************************************************")
print("This is your Quiz Game")
print("************************************************")

question_bank=[
    {"text":"How many strokes are there in the Ashoka Chakra?","answer":"D"},
    {"text":"Bollywood movie Dangal was based on which sport","answer":"A"},
    {"text":"The statue of unity is located in which state?","answer":"C"},
    {"text":"In object oriented programming, the ability of one class to acquire methods and attributes of another class is called _______", "answer":"A"},
    {"text":"When is children's day?","answer":"A"},
    {"text":"Which Programming language is used for data science?","answer":"C"},
    {"text":"What is the chemical symbol for sodium?","answer":"B"},
    {"text":"Which is the national fruit of India?","answer":"D"},
    {"text":"In 2018, which denomination of Indian Currency was banned?","answer":"B"},
]
options=[["A. 41","B. 74","C. 6","D. 24"],["A. wrestling","B. cricket","C. swimming","D. football"],
         ["A. goa","B. mp","C. gujarat","D. odisha"],
         ["A. Inheritance","B. Abstraction","c. Objects","D. Classes"],
         ["A. 14 november","B. 15 september","C. 24 february","D. 18 december"],
         ["A. java","B. js","C. python","D. c++"],
         ["A. Au","B. Na","C. K","D. H"],
         ["A. Apple","B. Banana","C. Papaya","D. Mango"],
         ["A. 2000","B. 1000","C. 20","D. 100"]
         ]
score=0
def check(user,correct):
    if user==correct:
        return True
    else:
        return False
for question_num in range(len(question_bank)):
    print(question_bank[question_num]['text'])
    for i in options[question_num]:
        print(i)

    answer=input("Choose one option (A/B/C/D): ").upper()
    is_correct=check(answer,question_bank[question_num]["answer"])  
    if is_correct:
        print("Yayyyyy!! Correct Answer")
        score+=1   
    else:
        print("Incorrect Answer")
        print("The correct answer is",question_bank[question_num]["answer"])
    print(f"Your current score is {score}/{question_num+1}\n")

print(f"You have given {score} correct answers")    
print(f"Your final score is {(score/len(question_bank))*100}%")