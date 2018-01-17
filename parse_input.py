import re

questions = []
answer_key = []
QUESTION_REGEX_PATTERN= "^[0-9]{1,2}.+$"
ANSWER_REGEX_PATTERN= "^[ABCDEFG]\."

def create_key(id_number ,text):
    return {
        id_number : text
    }

def create_answer(text):
    return {
        "choice": text
    }

def create_question(id_number, text):
    return {
        id_number : text,
        "choices": []
    }

def extract_questions(file_name):
    with open(file_name) as f:
        question_regex = re.compile(QUESTION_REGEX_PATTERN)
        answer_regex = re.compile(ANSWER_REGEX_PATTERN)

        for line in f:
            if question_regex.match(line):
                print('Creating question...')
                questions.append(create_question(0,line))
            elif answer_regex.match(line):
                print("Adding answer...")
                questions[len(questions) - 1]['choices'].append(create_answer(line))

    return questions

def extract_key(file_name):
    with open(file_name) as f:
        question_regex = re.compile(QUESTION_REGEX_PATTERN)

        for line in f:
            if question_regex.match(line):
                print('Adding key answer...')
                answer_key.append(create_key(0,line))

    return answer_key


if __name__ == '__main__':
    FILE_NAME1 = "quiz.txt"
    FILE_NAME2 = "key.txt"
    questions = extract_questions(FILE_NAME1)
    answer_key = extract_key(FILE_NAME2)
    print(questions)
    print(answer_key)
