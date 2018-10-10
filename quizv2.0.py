import re
import random
import string

###########################################################################
QUESTION_REGEX_PATTERN= "^[0-9]{1,2}.+$"
ANSWER_REGEX_PATTERN= "^[ABCDEFG]\."
#QUESTION_NUMBER_PATTERN="^[0-9]+[\\.]"
QUESTION_NUMBER_PATTERN="^[0-9]+"
QUESTION_NUMBER_PATTERN_NUMBER="\b\d+\b"
QUESTION_NUMBER_ONLY="^[0-9]"
ANSWER_LIST=['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f']
SINGLE_LETTER_ANSWER_AFTER_NUMBER="[{A-F}]+[\\.]"
SINGLE_LETTER_ANSWER_NUMBER_ONLY="[{A-F}]"
YES=['Y', 'y']
questions = []
answer_key = []
min_question_num = 0
max_question_num = 999999

###########################################################################
def create_key(id_number ,correct_answer, explanation):
    return {
#        "id_number" : re.findall(QUESTION_NUMBER_PATTERN_NUMBER, id_number),
        "id_number" : id_number,
        "correct_answer" : correct_answer,
        "explanation" : explanation
    }

def create_answer(text):
    return {
        "choice" : text
    }

def create_question(id_number, text):
    return {
        "question" : text,
#        "id_number" : re.findall(QUESTION_NUMBER_PATTERN_NUMBER, id_number),
        "id_number" : id_number,
        "choices" : []
    }

###########################################################################
def extract_questions(file_name):
    line_number = 0
    #print(line_number)
    with open(file_name) as f:
        question_regex = re.compile(QUESTION_REGEX_PATTERN)
        answer_regex = re.compile(ANSWER_REGEX_PATTERN)
        for line in f:
            #print(line)
            if question_regex.match(line):
                line_number += 1
                line_numbers = re.findall(QUESTION_NUMBER_PATTERN, line)
                line_numbert = int(filter(str.isdigit, line_numbers[0]))
#                print(line_numbert, line_numbert + 1)
                questions.append(create_question(line_numbert,line))
            elif answer_regex.match(line):
                questions[len(questions) - 1]['choices'].append(create_answer(line))
    print('QUESTIONES ADDED: ' + str(line_number))
    return questions

###########################################################################
def extract_key(file_name):
    line_number = 0
    with open(file_name) as f:
        question_regex = re.compile(QUESTION_REGEX_PATTERN)
        for line in f:
            # if the Q & A are out of order, print and check through
            #print questions[line_number]
            if question_regex.match(line):
                line_number += 1
                line_numbers = re.findall(QUESTION_NUMBER_PATTERN,line)
                line_numbert = int(filter(str.isdigit, line_numbers[0]))
                correct_letter_a = re.findall(SINGLE_LETTER_ANSWER_AFTER_NUMBER,line)
                correct_letter = re.findall(SINGLE_LETTER_ANSWER_NUMBER_ONLY,correct_letter_a[0])
                answer_key.append(create_key(line_numbert,correct_letter,line))
    print('ANSWERS ADDED: ' + str(line_number))
    return answer_key

###########################################################################
###########################################################################
def quiz():
    number = 0
    wrong = 0
    right = 0
    continue_quiz = True
    while continue_quiz:
        number += 1
        # pick a random number to user for a random question
        current_question_record = random.randrange(0, len(questions), 1)
        # print out a random question
        current_question = questions[current_question_record]
        print('\n')
        print("\033[1;33;39m" + current_question['question'] + " \033[0m ")
        for choice in current_question['choices']:
            print("\033[1;33;39m" + choice['choice'] + " \033[0m ")
        get_answer = raw_input('ENTER YOUR ANSWER: ')
        while get_answer not in ANSWER_LIST:
            get_answer = raw_input('\033[5;35;38mENTER YOUR ANSWER:\033[0m ')
        get_answer = string.upper(get_answer)
        # read the answer key and print the answer
        current_answer_key = answer_key[current_question_record]
        if get_answer == current_answer_key['correct_answer'][0]:
            print("\033[5;31;38mCONGRATS, YOU'RE RIGHT! \033[0m ")
            right += 1
        else:
            print('   CORRECT ANSWER: ' + current_answer_key['correct_answer'][0])
            wrong += 1
        print("\033[1;33;39m" + current_answer_key['explanation'] + " \033[0m ")
        get_answer = raw_input("PRESS ENTER TO CONTINUE OR X TO EXIT")
        if get_answer in ['X','x','Q','q']:
            continue_quiz = False

    print("\n\033[5;31;38mYOU GOT " + str(right) + " RIGHT AND " + str(wrong) + " WRONG! OUT Of "+ str(right + wrong) + " QUESTIONS. \033[0m ")
    return
###########################################################################
if __name__ == '__main__':
    FILE_NAME1 = "quiz.txt"
    FILE_NAME2 = "key.txt"

    print("\n")
    print("\033[1;31;38m/==============================================================\ \033[0m  ")
    print("\033[1;31;38m| NEAL'S LITTLE PYTHON SCRIPT TO STUDY SECURITY PLUS QUESTIONS | \033[0m  ")
    print("\033[1;31;38m|                                                              | \033[0m  ")
    print("\033[1;31;38m|  Questions are randomly selected and will continue forever   | \033[0m  ")
    print("\033[1;31;38m|    unless you eXit or you reach 1,000,000 right answers.     | \033[0m  ")
    print("\033[1;31;38m|                                                              | \033[0m  ")
    print("\033[1;31;38m|  Updated to include SY0-401 and SY0-501 questions.           | \033[0m  ")
    print("\033[1;31;38m|    The 501 question numbers start with 50.                   | \033[0m  ")
    print("\033[1;31;38m|  https://nealalan.github.io/                                 | \033[0m  ")
    print("\033[1;31;38m|                                                              | \033[0m  ")
    print("\033[1;31;38m|  #TEAM_PIGSTICK                                              | \033[0m  ")
    print("\033[1;31;38m\==============================================================/ \033[0m  ")
    print

    questions = extract_questions(FILE_NAME1)
    answer_key = extract_key(FILE_NAME2)

#    for i in range(len(questions)):
#        print('-------------------------------------')
#        print(questions[i])
#        print(answer_key[i])

    if raw_input('\033[1;35;38m QUESTION RANGE? (Y or N) \033[0m ') == YES:
        print("\n")
        print("\033[1;31;38m/==============================================================\ \033[0m  ")
        print("\033[1;31;38m|  SY0-401 - Questions range from 1 - 11020                    | \033[0m  ")
        print("\033[1;31;38m|  SY0-501 - Questions range from 500001 - 511015              | \033[0m  ")
        print("\033[1;31;38m|   X##XXX - ## equals a chapted number                        | \033[0m  ")
        print("\033[1;31;38m|   XXX#XX - Range 0-1 = pretest, 2-3 = post-test              | \033[0m  ")
        print("\033[1;31;38m\==============================================================/ \033[0m  ")
        print
        min_question_num = raw_input('\033[1;35;38m MIN QUESTION NUMBER: \033[0m ')
        max_question_num = raw_input('\033[1;35;38m MAX QUESTION NUMBER: \033[0m ')

    quiz()
    print("\nBYE")
