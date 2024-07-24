def test_addition_method_should_return_six(calculator):
    result = calculator.addition()
    expected = 6
    assert result == expected


def test_subtraction_method_should_return_two_negative(calculator):
    result = calculator.subtraction()
    expected = -2
    assert result == expected


def test_multiplication_method_should_return_eight(calculator):
    result = calculator.multiplication()
    expected = 8
    assert result == expected


def test_division_method_should_return_zero_point_five(calculator):
    result = calculator.division()
    expected = 0.5
    assert result == expected
