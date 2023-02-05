import pytest

def test_calc_addition():
  # function tests the output of 2+4
  output = 2 + 4
  assert output == 6

def test_calc_substraction():
  # function tests the output of 2-4
  output  = 2 - 4
  assert output == -2

def test_calc_multiply():
  # function tests the output of 2*4
  output = 2 * 4
  assert output == 8

def test_calc_division():
  # function tests the output of 2/4
  output = 2 / 4
  assert output == 0.5

def test_coucou():
  # Function tests if the output return 'hello'
    output='hello'
    assert output == 'hello'


