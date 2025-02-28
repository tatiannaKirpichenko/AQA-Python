import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TodosTests(unittest.TestCase):
    page_url = 'https://todo.qa.apps.itschool.pro/#/'

    def setUp(self) -> None:
        super().setUp()

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        self.driver = webdriver.Chrome(options=options)

        self.driver.get(self.page_url)

    def tearDown(self) -> None:
        self.driver.quit()

        super().tearDown()

    def test_OpenPage_CaptionPresented(self):
        caption = self.driver.find_element(By.CSS_SELECTOR, 'header h1')

        self.assertEqual('todos', caption.text)

    def test_AddTask_IncTotalCounter(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action1')
        todo.send_keys(Keys.ENTER)

        counter = self.driver.find_element(By.CSS_SELECTOR, '.todo-count')

        self.assertEqual('1 Items left', counter.text)

    def test_AddTaskMarkCompleted_NothingLeftInTotalCounter(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action1')
        todo.send_keys(Keys.ENTER)

        toggle = self.driver.find_element(By.CSS_SELECTOR, '.toggle')
        toggle.click()

        counter = self.driver.find_element(By.CSS_SELECTOR, '.todo-count')

        self.assertEqual('Nothing left', counter.text)

