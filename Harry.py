class Question: 
    
    def __init__(self, asked, answer):
        
        """ 
        Gives instance attributes (what is asked and the answer) to
        describe what goes within a question 
        """
        
        self.asked = asked
        self.answer = answer
        
    def input_quiz(questions_array):
    
        """ 
        Uses the function start_quiz to run the quiz and then
        stores the user's answers into a list as they take the quiz
        """
        
        # This while loop part here taken from "End Chat" segment of A3 Chatbots but modified to start a bot
        
        test = True
        while test:
        
            msg = input('Type start or begin to take the quiz! :\t')
            out_msg = None
        
            if start_quiz(msg):
            
                test = False
        
    
        score = 0
        choices = ['a','b','c']
        user_choices = []
        
        for item in questions_array:
            while True:
                answer = input(item.asked)
                if answer in choices:
                    user_choices.append(answer)
                    break
                print('\033[1m' +'Invalid input! Must be a, b or c! Try again!'+'\033[0m')
        return user_choices
        
def start_quiz(self_input):
    
    """ 
    Allows user to start the quiz by typing start or begin
    into the bot 
    """
    
    if 'start' in self_input or 'begin' in self_input:
        return True
    else:
        return False


def evaluate_quiz(user_choices, questions_array):
    
    """ 
    Starts with an empty list and adds all the actual answers into a list so one can compare them with the user's answers.
    Then, it compares the two lists and when the items in the two lists are the same it adds one to the counter set to zero. It
    then returns the score 
    """
    
    answer_list = []
    score = 0
    for item in questions_array:
        answer_list.append(item.answer)
    for items in range(len(user_choices)):
        if user_choices[items] == answer_list[items]:
            score = score + 1
    return score

def results(score):
    
    """ 
    Takes the score from the evaluate_quiz function and prints a statement based on the conditions listed 
    """
    
    if score < 5:
        print('\033[1m' + 'You are not that big of a fan of Harry Styles! That is ok.'+'\033[0m')
        
    else:
        print('\033[1m' + 'You are a huge fan of Harry Styles! See you at the Love On Tour :)'+'\033[0m')
        
