from pytest import fixture
from learning_github_actions.calculator import Calculator


@fixture
def calculator():
    return Calculator(2, 4)
