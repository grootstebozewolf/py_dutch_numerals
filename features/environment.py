# features/environment.py
from behave import fixture, use_fixture
from py_dutch_numerals import Tel
from py_dutch_numerals.mock_logger import MockLogger

def before_scenario(context, scenario):
    context.mock_logger = MockLogger()
    Tel.set_logger(context.mock_logger)

def after_scenario(context, scenario):
    # Clean up if necessary
    pass