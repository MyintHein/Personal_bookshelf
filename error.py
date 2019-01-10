"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:
question_file = open('questions.txt', 'r')
sample = [i.strip().split('=') for i in question_file.readlines()]
question_file.close()


right_answer = 0
total_question = 0

for i in sample:
    q, a = i

    user_input = input('Enter the right answer: {} = '.format(q))
    if user_input == a:
        right_answer += 1
    total_question += 1

result = open('questions.txt', 'w')    # open result.txt
result.write('Your final score is {}/{}.'.format(right_answer, total_question))

result.close()
