class Question:
    def __init__(self,prompt,ans):
        self.prompt = prompt
        self.ans = ans

    def validate(self,input):
        return self.ans == input