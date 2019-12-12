from Harry import Question, start_quiz, results, evaluate_quiz


questions_asked = [
    '1. When you hear the word kiwi which one of these comes to mind?\n(a) The Harry Styles song!\n(b) The green and brown fruit!\n(c) The Australian bird!\n\n',
    '2. When is Harry Styles birthday?\n(a) October 31st, 1996\n(b) December 3rd, 1995\n(c) February 1st, 1994\n\n',
    '3. What color are Harry Styles eyes?\n(a) Green!\n(b) Blue!\n(c) Brown\n\n',
    '4. Which boyband was Harry Styles originally apart of?\n(a) BTS\n(b) Big Time Rush\n(c) One Direction\n\n',
    '5. Where was Harry Styles born?\n(a) Paris, France\n(b) Holmes Chapel, England\n(c) Melbourne, Australia\n\n',
    '6. Harry Styles used to work\n(a) As a dog walker!\n(b) In a bakery!\n(c) As a firefighter!\n\n',
    '7. How many tattoos does Harry Styles have?\n(a) 55\n(b) None\n(c) 1\n\n',
    '8. When does the newest Harry Styles album come out?\n(a) There is no new album :(\n(b) December 13th, 2019\n(c) January 1st, 2020\n\n',
    '9. Which is a song on the first Harry Styles album?\n(a) Lights Up\n(b) Sign of the Times\n(c) No Control\n\n',
    '10. Harry Styles slogan is\n(a) Treat People With Kindness\n(b) Do You Know Who You Are?\n(c) What Do You Mean?\n\n'
]


questions_array = [
    Question(questions_asked[0], 'a'),
    Question(questions_asked[1], 'c'),
    Question(questions_asked[2], 'a'),
    Question(questions_asked[3], 'c'),
    Question(questions_asked[4], 'b'),
    Question(questions_asked[5], 'b'),
    Question(questions_asked[6], 'a'),
    Question(questions_asked[7], 'b'),
    Question(questions_asked[8], 'b'),
    Question(questions_asked[9], 'a'),
]


# Imports the random module
import random

choices = ['a', 'b', 'c']
list_from_input_quiz = [] 

# Simulates a list of random user input 
for item in range(10):
    list_from_input_quiz.append(random.choice(choices))
print(list_from_input_quiz)


# Takes the simulated list and starts the code testing
def test_for_evaluate_quiz():
    
    """ 
    Tests to see if the user's score is between 0 and 10 and if it is an integer 
    """
    
    assert evaluate_quiz(list_from_input_quiz, questions_array) >= 0
    assert evaluate_quiz(list_from_input_quiz, questions_array) <= 10
    assert isinstance(evaluate_quiz(list_from_input_quiz, questions_array), int)
    assert callable(evaluate_quiz)
    
test_for_evaluate_quiz()


def test_start_quiz_function():
    
    """ 
    Tests to see if the user's input is 'start' or 'begin' to start the quiz 
    """
    
    assert callable(start_quiz)
    assert isinstance(start_quiz('start'), bool)
    assert start_quiz('start') == True
    assert isinstance(start_quiz('begin'), bool)
    assert start_quiz('begin') == True

test_start_quiz_function()
