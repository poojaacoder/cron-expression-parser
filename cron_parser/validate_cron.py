from croniter import croniter

class ValidateCron:
    def __init__(self, expression):
        self.expression = expression

    def validate(self):
        return croniter.is_valid(self.expression)
    

            
