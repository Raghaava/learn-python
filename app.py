from Question import Question

question_prompts = [
    "What colors are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange",
    "What colors are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow",
    "What colors are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue",
]

questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b')
]


def test():
    score = 0
    for question in questions:
        ans = input(question.prompt+"\n")
        if ans == question.ans:
            score = score + 1
    return score


score = test()

print("your score "+str(score)+" out of "+str(len(questions)))
