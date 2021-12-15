from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from blog.models import Post
from django.urls import reverse
import time
from selenium.webdriver.common.keys import Keys


class TestProjectLogic(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('blog/functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_login_alert_displayed(self):
        self.browser.get('https://clerleq.pythonanywhere.com/')

    # The user requests the page the first time
        login_click = self.browser.find_element_by_link_text('Войти')
        time.sleep(2)
        login_click.click()
        time.sleep(3)

        username_form = self.browser.find_element_by_id('id_username')
        password_form = self.browser.find_element_by_id('id_password')

        username_form.send_keys("CleRleQ")
        password_form.send_keys("*******")
        time.sleep(2)

        login_button = self.browser.find_element_by_class_name('login-button')
        login_button.click()
        time.sleep(3)

        add_post = self.browser.find_element_by_link_text('Добавить пост')
        add_post.click()
        time.sleep(2)

        title_form = self.browser.find_element_by_id('id_title')
        text_form = self.browser.find_element_by_id('id_text')
        text_info_form = self.browser.find_element_by_id('id_textinfo')

        title_form.send_keys('Test')
        text_form.send_keys('ompdfsgpmdffdg fdkgmfdmkvfdem dfsk;kmv fdm; 56165 dfg dfg df615gdfs5g ')
        text_info_form.send_keys('test selenium')
        time.sleep(2)

        submit = self.browser.find_element_by_id('id_save')
        submit.click()
        time.sleep(2)








