import pytest
from cron_parser.parse_cron_expression import ParseCronExpression
from cron_parser.process_cron import ProcessCron
from cron_parser.validate_cron import ValidateCron

@pytest.fixture
def valid_cron_input_expression():
    return "*/4 */4 3,9 * 1-5"

@pytest.fixture
def valid_cmd():
    return "/usr/bin -v foo"

@pytest.fixture
def invalid_cron_input_expression():
    return "*-/3 0 5,10 * 1-10 /usr/bin/find" 

def test_validate_cron_expression_for_valid():
    print(" ************ Test validate cron expression for valid value ****************\n")
    value = ValidateCron("*/15 0 1,15 * 1-5").validate()
    assert value == True

def test_validate_cron_expression_for_invalid():
    print(" ************ Test validate cron expression for invalid value  ****************\n")
    value = ValidateCron("*/5 0 1,15 * 8-9").validate()
    assert value == False

def test_valid_cron_value_parse():
    print(" ************ Test valid cron value parse ****************\n")
    field = ProcessCron("*/15", "minute")
    field.process()
    assert field.values == [0, 15, 30, 45]

def test_cron_value_parse_range():
    print(" ************ Test cron value parse range****************\n")
    field = ProcessCron("5-9", "hour")
    field.process()
    assert field.values == [5, 6, 7, 8, 9]


def test_valid_cron_expression_parse():
    print(" ************ Test valid cron expression parse ****************\n")
    field = ProcessCron("*/15,#", "day of month")
    with pytest.raises(ValueError):
        field.process()

def test_cron_expression_parse_valid(valid_cron_input_expression, valid_cmd):
    print(" ************ Test valid cron expression parse ****************\n")
    expression = ParseCronExpression(valid_cron_input_expression, valid_cmd)
    expression.evaluate()
    assert len(expression.fields) == 5


def test_cron_value_parse_list():
    print(" ************ Test cron value parse list ****************\n")
    field = ProcessCron("4,5,6", "day of month")
    field.process()
    assert field.values == [4, 5, 6]

def test_cron_value_parse_step():
    print(" ************ Test cron value parse step ****************\n")
    field = ProcessCron("*/3", "month")
    field.process()
    assert field.values == [1, 4, 7, 10]

def test_cron_expression_parse_invalid(invalid_cron_input_expression, valid_cmd):
    print(" ************ Test invalid cron expression parse ****************\n")
    expression = ParseCronExpression(invalid_cron_input_expression, valid_cmd)
    with pytest.raises(ValueError):
        expression.evaluate()

def test_cron_expression_format_table(valid_cron_input_expression, valid_cmd):
    print(" ************ Test cron expression format table ****************\n")
    expression = ParseCronExpression(valid_cron_input_expression, valid_cmd)
    table =  expression.evaluate()
    expected_table = """minute        0 4 8 12 16 20 24 28 32 36 40 44 48 52 56
hour          0 4 8 12 16 20
day of month  3 9
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin -v foo"""
    print(table)
    print(expected_table)
    assert table == expected_table
