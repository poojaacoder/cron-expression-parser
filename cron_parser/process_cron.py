from cron_parser.constants import ASTRICK_VALUE, LIST_VALUE, RANGE_VALUE, STEP_VALUES
from cron_parser.utils.cron_helper import get_range_values, get_step_values, get_min_values, get_max_values


class ProcessCron:
    def __init__(self, cron_field_value, cron_field_name):
        self.cron_field_value = cron_field_value
        self.cron_field_name = cron_field_name
        self.values = []

    def process_star_value(self):
        """
        process start value function
        return: value
        """
        self.values = list(range(get_min_values(self.cron_field_name), get_max_values(self.cron_field_name) + 1))
    
    def process_range_value(self):
        """
        process range value function
        return: value
        """
        self.values = get_range_values(self.cron_field_value)
    
    def process_step_value(self):
        """
        process step value function
        return: value
        """
        step_elements = self.cron_field_value.split(STEP_VALUES)
        if int(step_elements[1]) > get_max_values(self.cron_field_name):
            raise ValueError(f"Invalid cron field value for {self.cron_field_name}: {self.cron_field_value}")
        self.values = get_step_values(step_elements[1], get_min_values(self.cron_field_name), get_max_values(self.cron_field_name))
        
    def process_list_value(self):
        """
        process list value function
        return: value
        """
        values = []
        elements = self.cron_field_value.split(",")
        for ele in elements:
            if ele == "*":
                continue
            if "/" in ele:
                step_parts = ele.split("/")
                if len(step_parts) == 2:
                    if int(step_parts[1]) > get_max_values(self.cron_field_name):
                        raise ValueError(f"Invalid cron field value for {self.cron_field_name}: {self.cron_field_value}")
                    range_values = get_step_values(step_parts[1], get_min_values(self.cron_field_name), get_max_values(self.cron_field_name))
                    values.extend(range_values)
                else:
                    raise ValueError(f"Invalid cron field value for {self.cron_field_name}: {self.cron_field_value}")
            elif "-" in ele:
                range_values = get_range_values(ele)
                values.extend(range_values)
            else:
                values.append(int(ele))
        self.values = values
    

    def process(self):
        """
        function to process the cron expression values based on value type
        return: value
        """
        if self.cron_field_value == ASTRICK_VALUE:
            self.process_star_value()
        elif LIST_VALUE in self.cron_field_value:
            self.process_list_value()
        elif RANGE_VALUE in self.cron_field_value:
            self.process_range_value()
        elif STEP_VALUES in self.cron_field_value:
            self.process_step_value()
        else:
            self.values = [int(self.cron_field_value)]

    def sort_values(self):
        self.values = sorted(self.values)
        self.values = list(dict.fromkeys(self.values))



