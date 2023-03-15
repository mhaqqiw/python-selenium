from PIL import Image
from io import BytesIO
from selenium import webdriver
from datetime import datetime
from inspect import getmembers, isfunction
import importlib.util, sys, traceback, cv2, pytesseract, numpy, time
import test_listener

def get_text_from_canvas(driver, left, top, right, bottom):
    png = driver.get_screenshot_as_png() # saves screenshot of entire page

    im = Image.open(BytesIO(png)) # uses PIL library to open image in memory

    # print(top, left, bottom, right)

    im = im.crop((2*left, 2*top, 2*right, 2*bottom)) # defines crop points
    im.save('screenshot.png') # saves new cropped image

    # Grayscale image
    ret,img = cv2.threshold(numpy.array(im), 125, 255, cv2.THRESH_BINARY)

    # Older versions of pytesseract need a pillow image
    # Convert back if needed
    img = Image.fromarray(img.astype(numpy.uint8))

    im.save('screenshot1.png') # saves new cropped image
    text = pytesseract.image_to_string(img, config='--psm 7 -c tessedit_char_whitelist=0123456789.-')
    return text

def clickCoordinate(driver, el, coor):
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(el, coor["x"], coor["y"])
    action.click()
    action.perform()
    time.sleep(0.5)

def count(path: str, data):
    module_name = path.split(".")[0]
    spec = importlib.util.spec_from_file_location(module_name, path)
    foo = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = foo
    spec.loader.exec_module(foo)
    for i in getmembers(foo, isfunction):
        data["total"] = data["total"] + 1
        data["list"].append({"module": foo, "name": i[0], "file": path})



def loadModule(path: str, data):
    module_name = path.split(".")[0]
    spec = importlib.util.spec_from_file_location(module_name, path)
    foo = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = foo
    spec.loader.exec_module(foo)
    for i in getmembers(foo, isfunction):
        sub = {"name": i[0], "file": path, "is_pass": False, "traceback": None, "start": None, "end": None}
        bar = getattr(foo, i[0])
        try:
            sub["start"] = datetime.now()
            test_listener.before_test()
            bar(test_listener.driver)
            sub["is_pass"] = True
        except Exception as e:
            sub["traceback"] = str(e)
        finally:
            test_listener.after_test()
            sub["end"] = datetime.now()
            data["testcases"].append(sub)

def asserts(exp, act):
    if exp != act:
        raise Exception("AssertionError: \n\tActual: %s, Expected: %s" % (act, exp))

        