#import question


questions = [
    'Too many chooices:\n\
    a. stuff\
    b. idk',
    'Other question:'
]

answers = [
    ['a'],
    ['a']
]

explanations = [
    ['food'],
    ['fun']

]



def quiz():

    wrong = 0
    right = 0
    number = 0

    for question, answer, explanation in zip(questions, answers, explanations):
        number += 1
        print('QUIZ QUESTION ' + str(number) + '\n\n' + str(question) + '\n')
        get_answer = raw_input('ENTER YOUR ANSWER: ')

        if get_answer in answer:
            print('\nCORRECT!\n\n')
            right += 1
        else:
            print('\nINCORRECT.\n' + explanation)
            wrong += 1
        if (number % 2) == 0:
            print('\n\n CORRECT = ' + str(right) + '\nINCORRECT = ' + str(wrong) + '\n')

if __name__ == '__main__':
    quiz()
