###########################################################################
# python program to give a quiz based on two input files
#
# updated: 2018/10/10
# project: https://nealalan.github.io/quiz-giver-sec-plus
#
# bugs:
#   - currently not handling answers with multiple letters correctly
#     if the answer is AD the only answer that is accepted as correct
#     is A (2018-10-10)

import re
import random
import string

###########################################################################
FILE_NAME1 = "quiz.txt"
FILE_NAME2 = "key.txt"
QUESTION_REGEX_PATTERN= "^[0-9]{1,2}.+$"
ANSWER_REGEX_PATTERN= "^[ABCDEFG]\."
QUESTION_NUMBER_PATTERN="^[0-9]+"
QUESTION_NUMBER_PATTERN_NUMBER="\b\d+\b"
QUESTION_NUMBER_ONLY="^[0-9]"
ANSWER_LIST=['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f']
SINGLE_LETTER_ANSWER_AFTER_NUMBER="[{A-F}]+[\\.]"
SINGLE_LETTER_ANSWER_NUMBER_ONLY="[{A-F}]"
YES=['Y', 'y']
questions = []
answer_key = []
min_question_num = 1
max_question_num = 999999

###########################################################################
def create_key(id_number, correct_answer, explanation):
    return {
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
        "id_number" : id_number,
        "choices" : []
    }

###########################################################################
def print_banner():
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
    print("\033[1;31;38m|  Multi-answer questions should always be answered answered   | \033[0m  ")
    print("\033[1;31;38m|   merged. Ex: AC                                             | \033[0m  ")
    print("\033[1;31;38m|                                                              | \033[0m  ")
    print("\033[1;31;38m|  #TEAM_PIGSTICK                                              | \033[0m  ")
    print("\033[1;31;38m\==============================================================/ \033[0m  ")
    print
    return

###########################################################################
# QUESTIONS: The input text file must be in a format of questions and answers
#   questions: will always be a single line and begin with a number followed
#              by a period.
#   answers: each answer will always be a single line and start with a letter
#            followed by a period.
#
# 1. Test question
# A. Answer 1
# B. Answer 2
# C. Answer 3
#
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
                #print(line_numbert, line_numbert + 1)
                questions.append(create_question(line_numbert,line))
            elif answer_regex.match(line):
                questions[len(questions) - 1]['choices'].append(create_answer(line))
    #print('QUESTIONES ADDED: ' + str(line_number))
    return questions
###########################################################################
# KEY: The input text file must be in a format of answers
# Question Number, followed by a period, correct answer(s), followed by a period,
# the explanation of the answer
#
# 1. AC. The answer is both A and C.
#
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
                # THIS CODE NEEDS TO BE UPDATED TO HANDLE MULTPLE LETTER ANSWERS
                correct_letter_a = re.findall(SINGLE_LETTER_ANSWER_AFTER_NUMBER,line)
                correct_letter = re.findall(SINGLE_LETTER_ANSWER_NUMBER_ONLY,correct_letter_a[0])
                answer_key.append(create_key(line_numbert,correct_letter,line))
    #print('ANSWERS ADDED: ' + str(line_number))
    return answer_key

###########################################################################
def question_range():
    # allow the global variables to be set in the function
    global min_question_num
    global max_question_num
    i = raw_input('\033[1;35;38m QUESTION RANGE? (Y or N) \033[0m ')
    if i in YES:
        print
        print("\033[1;31;38m/==============================================================\ \033[0m  ")
        print("\033[1;31;38m|  SY0-401 - Questions range from 1 - 11020                    | \033[0m  ")
        print("\033[1;31;38m|  SY0-501 - Questions range from 500001 - 511015              | \033[0m  ")
        print("\033[1;31;38m|   X##XXX - ## equals a chapter number                        | \033[0m  ")
        print("\033[1;31;38m|   XXX#XX - Range 0-1 = pretest, 2-3 = post-test              | \033[0m  ")
        print("\033[1;31;38m\==============================================================/ \033[0m  ")
        print
        min_question_num = raw_input('\033[1;35;38m MIN QUESTION NUMBER: \033[0m ')
        max_question_num = raw_input('\033[1;35;38m MAX QUESTION NUMBER: \033[0m ')
        if int(min_question_num) > int(max_question_num):
            min_question_num = raw_input('\033[1;35;38m MIN QUESTION NUMBER: \033[0m ')
            max_question_num = raw_input('\033[1;35;38m MAX QUESTION NUMBER: \033[0m ')
        return
###########################################################################
def print_all_questions():
    for i in range(len(questions)):
        print('-------------------------------------')
        print(questions[i])
        print(answer_key[i])
    return

###########################################################################
def get_question(current_question_record):
    return questions[current_question_record]

def check_question_number_range(question):
    if int(min_question_num) > int(question['id_number']) or int(question['id_number']) > int(max_question_num):
        #print("false: " + str(min_question_num) + " <= " + str(question['id_number']) + " >= " + str(max_question_num))
        return False
    else:
        #print("true: " + str(min_question_num) + " <= " + str(question['id_number']) + " >= " + str(max_question_num))
        return True

def check_answer_key(current_question_record):
    return answer_key[current_question_record]

###########################################################################
def quiz():
    number = 0
    wrong = 0
    right = 0
    continue_quiz = True
    while continue_quiz:
        number += 1
        infinity_loop_check = 0
        # pick a random number to use for a random question within the array
        current_question_record = random.randrange(0, len(questions), 1)
        current_question = get_question(current_question_record)
        # validate if the id_number from the question is within the subset desired
        while check_question_number_range(questions[current_question_record]) is False:
            if infinity_loop_check > 3000:
                print("NO QUESTIONS IN RANGE!!! (infinity loop stopped)")
                continue_quiz = False
                break
            current_question_record = random.randrange(0, len(questions), 1)
            current_question = get_question(current_question_record)
            infinity_loop_check += 1
        if continue_quiz is False:
            break
        print("\n\033[1;33;39m" + current_question['question'] + " \033[0m ")
        for choice in current_question['choices']:
            print("\033[1;33;39m" + choice['choice'] + " \033[0m ")
        get_answer = raw_input('ENTER YOUR ANSWER: ')
        while get_answer not in ANSWER_LIST:
            get_answer = raw_input('\033[5;35;38mENTER YOUR ANSWER:\033[0m ')
        get_answer = string.upper(get_answer)
        # read the answer key and print the answer
        current_answer_key = check_answer_key(current_question_record)
        if get_answer == current_answer_key['correct_answer'][0]:
            print("\n\033[5;31;38mCONGRATS, YOU'RE RIGHT! \033[0m ")
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
    print_banner()
    questions = extract_questions(FILE_NAME1)
    answer_key = extract_key(FILE_NAME2)
    question_range()
    #print_all_questions()
    quiz()
    print("\nBYE")
