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

question10 = Question(
    qno=10,
    text="Write a Python function to check if a number is a perfect number or not.",
    testcaseno=3,
    samplein="28",
    sampleout="True",
    tc1="6",
    tc2="12",
    tc3="496",
    tc1_sol="True",
    tc2_sol="False",
    tc3_sol="True"
)
question10.save()

question11 = Question(
    qno=11,
    text="Create a Python program to find the LCM (Least Common Multiple) of two numbers.",
    testcaseno=3,
    samplein="12 15",
    sampleout="60",
    tc1="7 13",
    tc2="18 27",
    tc3="4 10",
    tc1_sol="91",
    tc2_sol="54",
    tc3_sol="20"
)
question11.save()

question12 = Question(
    qno=12,
    text="Write a Python function to check if a string is an anagram of another string.",
    testcaseno=4,
    samplein="listen silent",
    sampleout="True",
    tc1="hello olleh",
    tc2="openai aiopen",
    tc3="python typhon",
    tc1_sol="True",
    tc2_sol="True",
    tc3_sol="False"
)
question12.save()

question13 = Question(
    qno=13,
    text="Create a Python program to find the factorial of a number using recursion.",
    testcaseno=3,
    samplein="5",
    sampleout="120",
    tc1="0",
    tc2="3",
    tc3="7",
    tc1_sol="1",
    tc2_sol="6",
    tc3_sol="5040"
)
question13.save()

question14 = Question(
    qno=14,
    text="Write a Python program to check if a given string is a valid palindrome ignoring non-alphanumeric characters.",
    testcaseno=3,
    samplein="A man, a plan, a canal, Panama!",
    sampleout="True",
    tc1="race car",
    tc2="hello",
    tc3="Was it a car or a cat I saw?",
    tc1_sol="True",
    tc2_sol="False",
    tc3_sol="True"
)
question14.save()

question15 = Question(
    qno=15,
    text="Create a Python function to find the number of vowels in a string.",
    testcaseno=3,
    samplein="Hello, World!",
    sampleout="3",
    tc1="OpenAI",
    tc2="programming",
    tc3="a e i o u",
    tc1_sol="3",
    tc2_sol="3",
    tc3_sol="5"
)
question15.save()

question16 = Question(
    qno=16,
    text="Write a Python program to check if two strings are anagrams of each other.",
    testcaseno=3,
    samplein="listen silent",
    sampleout="True",
    tc1="hello olleh",
    tc2="openai aiopen",
    tc3="python typhon",
    tc1_sol="True",
    tc2_sol="True",
    tc3_sol="False"
)
question16.save()

question17 = Question(
    qno=17,
    text="Create a Python program to reverse words in a given sentence.",
    testcaseno=3,
    samplein="Hello, OpenAI!",
    sampleout="olleH !IANepo",
    tc1="Python is awesome",
    tc2="Let's code",
    tc3="Reverse this sentence",
    tc1_sol="nohtyP si emosewa",
    tc2_sol="s'teL edoc",
    tc3_sol="esreveR siht ecnetnes"
)
question17.save()

question18 = Question(
    qno=18,
    text="Write a Python function to find the second largest number in a list.",
    testcaseno=3,
    samplein="3 5 2 9 6",
    sampleout="6",
    tc1="10 20 15 5",
    tc2="100 200 50 25 75",
    tc3="1 3 2",
    tc1_sol="15",
    tc2_sol="100",
    tc3_sol="2"
)
question18.save()

question19 = Question(
    qno=19,
    text="Create a Python program to find the sum of all even numbers in a list.",
    testcaseno=3,
    samplein="2 5 8 10 3",
    sampleout="20",
    tc1="11 13 15 17",
    tc2="22 26 30 34",
    tc3="1 3 5 7 9",
    tc1_sol="0",
    tc2_sol="112",
    tc3_sol="0"
)
question19.save()

question20 = Question(
    qno=20,
    text="Write a Python program to check if a string is a pangram or not.",
    testcaseno=3,
    samplein="The quick brown fox jumps over the lazy dog",
    sampleout="True",
    tc1="Hello, World!",
    tc2="Pack my box with five dozen liquor jugs",
    tc3="abcdefghijklmnopqrstuvwxyz",
    tc1_sol="False",
    tc2_sol="True",
    tc3_sol="True"
)
question20.save()

question21 = Question(
    qno=21,
    text="Create a Python program to sort words in a given sentence in alphabetical order.",
    testcaseno=3,
    samplein="This is an example sentence.",
    sampleout="This an example is sentence.",
    tc1="OpenAI is awesome",
    tc2="Let's code in Python",
    tc3="Sorting words is easy",
    tc1_sol="AI is awesome Open",
    tc2_sol="Let's Python code in",
    tc3_sol="easy is Sorting words"
)
question21.save()

question18 = Question(
    qno=18,
    text="Write a Python function to find the second largest number in a list.",
    testcaseno=3,
    samplein="3 5 2 9 6",
    sampleout="6",
    tc1="10 20 15 5",
    tc2="100 200 50 25 75",
    tc3="1 3 2",
    tc1_sol="15",
    tc2_sol="100",
    tc3_sol="2"
)
question18.save()

question19 = Question(
    qno=19,
    text="Create a Python program to find the sum of all even numbers in a list.",
    testcaseno=3,
    samplein="2 5 8 10 3",
    sampleout="20",
    tc1="11 13 15 17",
    tc2="22 26 30 34",
    tc3="1 3 5 7 9",
    tc1_sol="0",
    tc2_sol="112",
    tc3_sol="0"
)
question19.save()

question20 = Question(
    qno=20,
    text="Write a Python program to check if a string is a pangram or not.",
    testcaseno=3,
    samplein="The quick brown fox jumps over the lazy dog",
    sampleout="True",
    tc1="Hello, World!",
    tc2="Pack my box with five dozen liquor jugs",
    tc3="abcdefghijklmnopqrstuvwxyz",
    tc1_sol="False",
    tc2_sol="True",
    tc3_sol="True"
)
question20.save()

question21 = Question(
    qno=21,
    text="Create a Python program to sort words in a given sentence in alphabetical order.",
    testcaseno=3,
    samplein="This is an example sentence.",
    sampleout="This an example is sentence.",
    tc1="OpenAI is awesome",
    tc2="Let's code in Python",
    tc3="Sorting words is easy",
    tc1_sol="AI is awesome Open",
    tc2_sol="Let's Python code in",
    tc3_sol="easy is Sorting words"
)
question21.save()


admin.site.register(Question)
