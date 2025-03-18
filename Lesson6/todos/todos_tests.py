import unittest

from selenium import webdriver

from Lesson6.todos.config_manager import ConfigManager
from Lesson6.todos.pages.todo_page import TodoPage


class TodosTests(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        config = ConfigManager.get_config()
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(config.page_url)
        self.page = TodoPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()
        super().tearDown()

    def test_OpenPage_CaptionPresented(self):
        caption = self.page.get_caption_text()
        self.assertEqual('todos', caption)

    def test_AddTask_IncTotalCounter(self):
        self.page.add_task('action1')
        counter_text = self.page.get_todo_count()
        self.assertEqual('1 Items left', counter_text)

    def test_AddTaskMarkCompleted_NothingLeftInTotalCounter(self):
        self.page.add_task('action1')
        self.page.mark_task_completed()
        counter_text = self.page.get_todo_count()
        self.assertEqual('Nothing left', counter_text)

    def test_AddTaskFilterCompleted_NothingLeftInTotalCounter(self):
        self.page.add_task('action1')
        self.page.mark_task_completed()
        self.page.filter_completed_tasks()
        tasks = self.page.get_tasks()
        self.assertEqual(1, len(tasks))

    def test_AddTaskMarkAsCompletedFilterCompleted_OneItemsLeftInTotalCounter(self):
        self.page.add_task('action1')
        self.page.mark_task_completed()
        self.page.filter_completed_tasks()
        tasks = self.page.get_tasks()
        self.assertEqual(1, len(tasks))

    def test_AddTaskMarkAsCompleted_AppearsButtonClearCompleted(self):
        self.page.add_task('action1')
        self.page.mark_task_completed()
        clear_button_text = self.page.get_clear_completed_button_text()
        self.assertEqual('Clear completed', clear_button_text)

    def test_AddTaskMarkAsCompletedPressButtonClearCompleted_NothingLeftInTotalCounter(self):
        self.page.add_task('action1')
        self.page.mark_task_completed()
        self.page.clear_completed_tasks()
        todo_count_text = self.page.get_todo_count_text()
        self.assertEqual('Nothing left', todo_count_text)

    def test_AddTwoTasksMarkFirstCompletedPressButtonClearCompleted_SecondTaskOnTaskListOneItemsLeftInTotalCounter(self):
        self.page.add_multiple_tasks(['action1', 'action2'])
        self.page.mark_task_completed()
        self.page.clear_completed_tasks()

        tasks = self.page.get_remaining_tasks()
        self.assertTrue(tasks)

        todo_count_text = self.page.get_todo_count_text()
        self.assertEqual('1 Items left', todo_count_text)

    def test_AddTwoTasksClickButtonMarkAll_AllTasksMarkedCompletedNothingLeftInTotalCounter(self):
        self.page.add_multiple_tasks(['action1', 'action2'])
        self.page.mark_all_tasks_completed()

        all_tasks_completed = self.page.are_all_tasks_completed()
        self.assertTrue(all_tasks_completed, "Не все задачи помечены как выполненные.")

        todo_count_text = self.page.get_todo_count_text()
        self.assertEqual('Nothing left', todo_count_text)

    def test_AddTwoTasksClickOneCheckbox_OneItemsLeftInTotalCounter(self):
        self.page.add_multiple_tasks(['action1', 'action2'])
        self.page.mark_task_completed()

        todo_count_text = self.page.get_todo_count_text()
        self.assertEqual('1 Items left', todo_count_text)

    def test_AddTwoTasksTwoClickButtonMarkAll_TwoItemsLeftInTotalCounter(self):
        self.page.add_multiple_tasks(['action1', 'action2'])

        self.page.mark_all_tasks()
        self.page.mark_all_tasks()

        todo_count_text = self.page.get_todo_count_text()
        self.assertEqual('2 Items left', todo_count_text)

    def test_AddTwoTasksClickButtonMarkAll_NothingLeftInTotalCounter(self):
        self.page.add_multiple_tasks(['action1', 'action2'])
        self.page.mark_all_tasks()

        all_tasks_completed = self.page.are_all_tasks_completed()
        self.assertTrue(all_tasks_completed, "Не все задачи помечены как выполненные.")

        todo_count_text = self.page.get_todo_count_text()
        self.assertEqual('Nothing left', todo_count_text)
