from behave import given, when, then, use_step_matcher
from py_dutch_numerals import tel, Tel
from py_dutch_numerals.mock_logger import MockLogger

use_step_matcher("re")

@given('ik heb het Nederlandse getal "(.*)"')
def step_given_dutch_number(context, nederlands_getal):
    context.nederlands_getal = nederlands_getal

@when('ik het converteer naar een integer')
def step_when_convert_to_integer(context):
    context.result = tel(context.nederlands_getal)

@when('ik het probeer te converteren naar een integer')
def step_when_try_convert_to_integer(context):
    context.exception = None
    try:
        context.result = tel(context.nederlands_getal)
    except Exception as e:
        context.exception = e

@then('moet het resultaat (\d+) zijn')
def step_then_check_result(context, verwacht_resultaat):
    verwacht_resultaat = int(verwacht_resultaat)
    assert context.result == verwacht_resultaat, f"Verwacht {verwacht_resultaat}, maar kreeg {context.result}"
    assert context.mock_logger.info_logs[-1] == f"Successfully parsed input: {context.nederlands_getal} to {verwacht_resultaat}"

@then('moet er een fout optreden met de melding "(.*)"')
def step_then_check_error(context, error_message):
    assert context.exception is not None, "Verwachtte een fout, maar er trad geen fout op"
    assert str(context.exception) == error_message, f"Verwachtte foutmelding '{error_message}', maar kreeg '{str(context.exception)}'"
    assert context.mock_logger.error_logs[-1] == error_message
