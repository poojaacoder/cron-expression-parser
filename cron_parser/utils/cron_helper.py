from cron_parser.constants import  VALUES 

def get_min_values(field_name):
    """
    get min values for given field_name
    parameters: field_name
    return: min value
    """
    min_values = {
         VALUES.MINUTE: 0,
         VALUES.HOUR : 0 ,
         VALUES.DAY_OF_MONTH: 1 ,
         VALUES.MONTH : 1,
         VALUES.DAY_OF_WEEK : 0
    }
    return min_values[field_name]

def get_max_values(field_name):
    """
    get max values for given field_name
    parameters: field_name
    return: max value
    """
    max_values = {
         VALUES.MINUTE : 59,
         VALUES.HOUR : 23,
         VALUES.DAY_OF_MONTH: 31,
         VALUES.MONTH : 12,
         VALUES.DAY_OF_WEEK : 6
    }
    return max_values[field_name]

def get_range_values(range_str):
    """
    get range values for specified range
    parameters: range_str
    return: list of values
    """
    
    start, end = map(int, range_str.split("-"))
    return list(range(start, end + 1))


def get_step_values(step_str, min_value, max_value):
    """
    get step values for specified range
    parameters: step_str, min_value, max_value
    return: list of values
    """
    values = []
    step = int(step_str)
    for value in range(min_value, max_value + 1):
        if (value - min_value) % step == 0:
            values.append(value)
    return values


def return_output_as_table(fields, command):
    table = []
    for field in fields:
        table.append(f"{field.cron_field_name:<14}{' '.join(map(str, field.values))}")

    table.append(f"{'command':<14}{command}")

    return "\n".join(table)