import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def wait_for(condition_function):
    start_time = time.time()
    while time.time() < start_time + 3:
        if condition_function():
            return True
        else:
            time.sleep(0.1)
    raise Exception(
        'Timeout waiting for {}'.format(condition_function.__name__)
    )

class wait_for_page_load(object):

    def __init__(self, browser):
        self.browser = browser

    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')

    def page_has_loaded(self):
        new_page = self.browser.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id

    def __exit__(self, *_):
        wait_for(self.page_has_loaded)


USER_NAME = ''
PASSWORD = ''

browser = webdriver.Firefox()
browser.get('http://yemeksepeti.com/ankara')

html = browser.page_source

username = browser.find_element_by_name("UserName")
username.send_keys(USER_NAME)

password = browser.find_element_by_name("Password")
password.send_keys(PASSWORD)

button = browser.find_element_by_id('ys-fastlogin-button')

#with wait_for_page_load(browser):
button.click()

print "Logged in"

html = browser.page_source
f = open('afterlogin.html','w+')
f.write(html.encode('utf8'))
f.close()

browser.execute_script("$(document).ready(function () {alert(window.Globals.CurrentState.LoginToken);});")
