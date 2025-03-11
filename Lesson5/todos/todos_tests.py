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

    def test_AddTaskFilterCompleted_NothingLeftInTotalCounter(self):
        input_field = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        input_field.clear()
        input_field.send_keys('action1')
        input_field.send_keys(Keys.ENTER)

        button_completed = self.driver.find_element(By.CSS_SELECTOR, '[href="#/completed"]')
        button_completed.click()

        tasks = self.driver.find_elements(By.CSS_SELECTOR, "ul.todo-list li")

        assert len(tasks) == 0

    def test_AddTaskMarkAsCompletedFilterCompleted_OneItemsLeftInTotalCounter(self):
        input_field = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        input_field.clear()
        input_field.send_keys('action1')
        input_field.send_keys(Keys.ENTER)

        checkbox = self.driver.find_element(By.CSS_SELECTOR, "ul.todo-list li input.toggle")
        checkbox.click()

        filter_completed_button = self.driver.find_element(By.LINK_TEXT, "Completed")
        filter_completed_button.click()

        tasks = self.driver.find_elements(By.CSS_SELECTOR, "ul.todo-list li")
        assert len(tasks) == 1

    def test_AddTaskMarkAsCompleted_AppearsButtonClearCompleted(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action1')
        todo.send_keys(Keys.ENTER)

        toggle = self.driver.find_element(By.CSS_SELECTOR, '.toggle')
        toggle.click()

        counter = self.driver.find_element(By.CSS_SELECTOR, '.clear-completed')

        self.assertEqual('Clear completed', counter.text)

    def test_AddTaskMarkAsCompletedPressButtonClearCompleted_NothingLeftInTotalCounter(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action1')
        todo.send_keys(Keys.ENTER)

        toggle = self.driver.find_element(By.CSS_SELECTOR, '.toggle')
        toggle.click()

        button_clear_completed = self.driver.find_element(By.CSS_SELECTOR, '.clear-completed')
        button_clear_completed.click()

        counter = self.driver.find_element(By.CSS_SELECTOR, '.todo-count')
        self.assertEqual('Nothing left', counter.text)

    def test_AddTwoTasksMarkFirstCompletedPressButtonClearCompleted_SecondTaskOnTaskListOneItemsLeftInTotalCounter(
            self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action1')
        todo.send_keys(Keys.ENTER)

        todo.send_keys('action2')
        todo.send_keys(Keys.ENTER)

        # Обозначение первой задачи как выполненной
        first_task_checkbox = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .toggle")
        first_task_checkbox.click()

        # Нажать на кнопку "Clear completed"
        clear_completed_button = self.driver.find_element(By.CSS_SELECTOR, "button.clear-completed")
        clear_completed_button.click()

        # Проверка, что вторая задача осталась в списке
        tasks = self.driver.find_elements(By.CSS_SELECTOR, "ul.todo-list li")
        self.assertTrue(tasks)

        # Проверка, что счётчик задач показывает '1 Items left'
        counter = self.driver.find_element(By.CSS_SELECTOR, '.todo-count')
        self.assertEqual('1 Items left', counter.text)

    def test_AddTwoTasksClickButtonMarkAll_AllTasksMarkedCompletedNothingLeftInTotalCounter(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action1')
        todo.send_keys(Keys.ENTER)

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
