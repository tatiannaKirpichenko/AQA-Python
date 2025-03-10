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

        self.driver = webdriver.Chrome()

        self.driver.get(self.page_url)

    def tearDown(self) -> None:
        self.driver.quit()

        super().tearDown()

    def test_AddTwoTasksClickButtonCompleted_OneItemsLeftInTotalCounter(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action1')
        todo.send_keys(Keys.ENTER)

        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action2')
        todo.send_keys(Keys.ENTER)

        first_task_checkbox = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .toggle")
        first_task_checkbox.click()

        button_completed = self.driver.find_element(By.CSS_SELECTOR, '[href="#/completed"')
        button_completed.send_keys(Keys.ENTER)

        tasks = self.driver.find_elements(By.CSS_SELECTOR, "ul.todo-list li")
        self.assertTrue(tasks)

        counter = self.driver.find_element(By.CSS_SELECTOR, '.todo-count')
        self.assertEqual('1 Items left', counter.text)

        # Тест должен упасть на последнем пункте

    def test_AddTwoTasksTwoClickButtonMarkAll_TwoItemsLeftInTotalCounter(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action1')
        todo.send_keys(Keys.ENTER)

        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action2')
        todo.send_keys(Keys.ENTER)

        # Нажать на кнопку "Отметить все"
        mark_all_checkbox = self.driver.find_element(By.CSS_SELECTOR, "input.toggle-all")
        mark_all_checkbox.click()

        # Нажать на кнопку "Отметить все"
        mark_all_checkbox = self.driver.find_element(By.CSS_SELECTOR, "input.toggle-all")
        mark_all_checkbox.click()

        # Проверка счётчика оставшихся задач
        counter = self.driver.find_element(By.CSS_SELECTOR, '.todo-count')
        self.assertEqual('2 Items left', counter.text)

    def test_AddTwoTasksClickButtonMarkAllClickButtonCompleted_TwoItemsLeftInTotalCounter(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action1')
        todo.send_keys(Keys.ENTER)

        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action2')
        todo.send_keys(Keys.ENTER)

        # Нажать на кнопку "Отметить все"
        mark_all_checkbox = self.driver.find_element(By.CSS_SELECTOR, "input.toggle-all")
        mark_all_checkbox.click()

        button_completed = self.driver.find_element(By.CSS_SELECTOR, '[href="#/completed"')
        button_completed.send_keys(Keys.ENTER)

        # Проверка, что все задачи помечены как выполненные
        task_elements = self.driver.find_elements(By.CSS_SELECTOR, "ul.todo-list li")
        all_tasks_completed = True  # Переменная для отслеживания статуса

        for task in task_elements:
            if "completed" not in task.get_attribute("class"):
                all_tasks_completed = False  # Если найдена задача без класса "completed"
                print(f"Задача с текстом '{task.text}' не помечена как выполненная.")  # Вывод текста задачи

        assert all_tasks_completed, "Не все задачи помечены как выполненные."

        # Проверка счётчика оставшихся задач
        counter = self.driver.find_element(By.CSS_SELECTOR, '.todo-count')
        self.assertEqual('2 Items left', counter.text)

    def test_AddTwoTasksClickButtonMarkAllAddNewOneTask_OneItemsLeftInTotalCounter(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action1')
        todo.send_keys(Keys.ENTER)

        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action2')
        todo.send_keys(Keys.ENTER)

        # Нажать на кнопку "Отметить все"
        mark_all_checkbox = self.driver.find_element(By.CSS_SELECTOR, "input.toggle-all")
        mark_all_checkbox.click()

        # Проверка, что все задачи помечены как выполненные
        task_elements = self.driver.find_elements(By.CSS_SELECTOR, "ul.todo-list li")
        all_tasks_completed = True  # Переменная для отслеживания статуса

        for task in task_elements:
            if "completed" not in task.get_attribute("class"):
                all_tasks_completed = False  # Если найдена задача без класса "completed"
                print(f"Задача с текстом '{task.text}' не помечена как выполненная.")  # Вывод текста задачи

        assert all_tasks_completed, "Не все задачи помечены как выполненные."

        # Проверка счётчика оставшихся задач
        counter = self.driver.find_element(By.CSS_SELECTOR, '.todo-count')
        self.assertEqual('Nothing left', counter.text)

        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action3')
        todo.send_keys(Keys.ENTER)

        # Проверка, что задача есть в списке
        tasks = self.driver.find_elements(By.CSS_SELECTOR, "ul.todo-list li")
        self.assertTrue(tasks)

        counter = self.driver.find_element(By.CSS_SELECTOR, '.todo-count')
        self.assertEqual('1 Items left', counter.text)
