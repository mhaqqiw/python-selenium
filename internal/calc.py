import module
from elements import calc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

operator = ["+", "-", "/", "*"]

def expected_result(syntax):
    arr = syntax.split("=")
    if len(arr) < 1:
        raise Exception("Invalid Syntax: "+syntax)
    return arr[1], arr[0]

def run_click(driver, syntax):
    elem = driver.find_element(By.XPATH, calc.iframe_canvas)
    exp, str_auto = expected_result(syntax)
    actions = ActionChains(driver)
    actions.send_keys(str_auto)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    elem_dimension = elem.location
    size = elem.size
    w, h = size['width'], size['height']

    left = elem_dimension['x']
    top = elem_dimension['y']
    right = left + w
    bottom = top + 125
    txt = module.get_text_from_canvas(driver, left, top, right, bottom)
    module.asserts(exp, str(txt).strip())
