from internal import calc

def test_plus_positive_positive(driver):
    syntax = "2+2=4"
    calc.run_click(driver, syntax)

def test_plus_positive_negative(driver):
    syntax = "4-1=3"
    calc.run_click(driver, syntax)

def test_plus_negative_positive(driver):
    syntax = "2-1=1"
    calc.run_click(driver, syntax)

def test_plus_negative_negative(driver):
    syntax = "-2+-2=-4"
    calc.run_click(driver, syntax)

