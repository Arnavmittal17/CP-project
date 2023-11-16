from django.contrib import admin
from .models import Question
# Create a new question
# new_question = Question(
#     qno=1,
#     text='What is the capital of France?',
#     testcaseno=3,
#     samplein='Paris',
#     sampleout='Paris',
#     tc1='Question',
#     tc2='Answer',
#     tc3='Solution',
#     tc1_sol='Paris',
#     tc2_sol='Paris',
#     tc3_sol='Paris'
# )
# new_question.save()  # Save the question to the database
question1 = Question(
    qno=1,
    text="Write a Python function to calculate the factorial of a number.",
    testcaseno=3,
    samplein="5",
    sampleout="120",
    tc1="3",
    tc2="0",
    tc3="10",
    tc1_sol="6",
    tc2_sol="1",
    tc3_sol="3628800"
)
question1.save()
question2 = Question(
    qno=2,
    text="Implement a function to reverse a string in Python.",
    testcaseno=2,
    samplein="Hello",
    sampleout="olleH",
    tc1="OpenAI",
    tc2="12345",
    tc3="Programming",
    tc1_sol="IAepno",
    tc2_sol="54321",
    tc3_sol="gnimmargorP"
)
question2.save()
question3 = Question(
    qno=3,
    text="Create a Python class for a simple calculator with add, subtract, multiply, and divide methods.",
    testcaseno=3,
    samplein="10 5",
    sampleout="15 5 50 2",
    tc1="20 10",
    tc2="100 20",
    tc3="8 4",
    tc1_sol="30 10 200 2.5",
    tc2_sol="120 80 2000 5",
    tc3_sol="12 4 32 2"
)
question3.save()
question4 = Question(
    qno=4,
    text="Write a Python program to check if a given number is prime or not.",
    testcaseno=2,
    samplein="7",
    sampleout="True",
    tc1="15",
    tc2="1",
    tc3="23",
    tc1_sol="False",
    tc2_sol="False",
    tc3_sol="True"
)
question4.save()
question5 = Question(
    qno=5,
    text="Implement a Python function to find the maximum element in a list.",
    testcaseno=2,
    samplein="1 5 3 9 2",
    sampleout="9",
    tc1="10 20 15 5",
    tc2="100 200 50 25 75",
    tc3="1 3 2",
    tc1_sol="20",
    tc2_sol="200",
    tc3_sol="3"
)
question5.save()
# Example 6
question6 = Question(
    qno=6,
    text="Write a Python function to check if a string is a palindrome.",
    testcaseno=3,
    samplein="radar",
    sampleout="True",
    tc1="hello",
    tc2="madam",
    tc3="level",
    tc1_sol="False",
    tc2_sol="True",
    tc3_sol="True"
)
question6.save()

# Example 7
question7 = Question(
    qno=7,
    text="Create a Python function to find the sum of digits of a number.",
    testcaseno=2,
    samplein="12345",
    sampleout="15",
    tc1="98765",
    tc2="111",
    tc3="123456789",
    tc1_sol="35",
    tc2_sol="3",
    tc3_sol="45"
)
question7.save()

question8 = Question(
    qno=8,
    text="Write a Python function to check if a number is Armstrong number or not.",
    testcaseno=3,
    samplein="153",
    sampleout="True",
    tc1="370",
    tc2="100",
    tc3="9474",
    tc1_sol="True",
    tc2_sol="False",
    tc3_sol="True"
)
question8.save()

question9 = Question(
    qno=9,
    text="Create a Python program to find the GCD (Greatest Common Divisor) of two numbers.",
    testcaseno=3,
    samplein="24 36",
    sampleout="12",
    tc1="72 120",
    tc2="45 90",
    tc3="63 81",
    tc1_sol="24",
    tc2_sol="45",
    tc3_sol="9"
)
question9.save()


admin.site.register(Question)
