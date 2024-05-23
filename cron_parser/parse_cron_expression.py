from cron_parser.constants import EXPRESSION_FIELD_NAMES
from cron_parser.process_cron import ProcessCron
from cron_parser.validate_cron import ValidateCron
from cron_parser.utils.cron_helper import return_output_as_table
from cron_descriptor import get_description


class ParseCronExpression:
    def __init__(self, expression: str, cmd):
        self.expression = expression
        self.fields = []
        self.command = None
        self.cmd = cmd

    def evaluate(self):
        string_expression = self.expression.split(' ', 5)
        # command = self.cmd.split('')
        # print("**************")
        # print("here is a command : ", self.cmd)
        # self.command = "string_expression[-1]"
        if not ValidateCron(self.expression).validate():
            raise ValueError(f"Invalid cron expression.")
            
        for i, str_value in enumerate(string_expression):
            cron_field_name = EXPRESSION_FIELD_NAMES[i]
            cron_field_value = ProcessCron(str_value, cron_field_name)
            cron_field_value.process()
            cron_field_value.sort_values()
            self.fields.append(cron_field_value)
        
        print(get_description(self.expression))
        
        return return_output_as_table(self.fields, self.cmd)

