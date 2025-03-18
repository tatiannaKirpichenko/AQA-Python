from selenium.webdriver import Keys

from locators.todo_page_locators import TodoPageLocators


class TodoPage:
    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver

    def get_caption_text(self):
        return self.driver.find_element(*TodoPageLocators.caption).text

    def enter_task(self, task_name):
        todo_input = self.driver.find_element(*TodoPageLocators.new_todo_input)
        todo_input.clear()
        todo_input.send_keys(task_name)

    def submit_task(self):
        todo_input = self.driver.find_element(*TodoPageLocators.new_todo_input)
        todo_input.send_keys(Keys.ENTER)

    def add_task(self, task_name):
        self.enter_task(task_name)
        self.submit_task()

    def get_todo_count(self):
        return self.driver.find_element(*TodoPageLocators.todo_count).text

    def mark_task_completed(self):
        toggle = self.driver.find_element(*TodoPageLocators.toggle)
        toggle.click()

    def filter_completed_tasks(self):
        button_completed = self.driver.find_element(*TodoPageLocators.completed_button)
        button_completed.click()

    def get_tasks(self):
        return self.driver.find_elements(*TodoPageLocators.todo_list_items)

    def get_clear_completed_button_text(self):
        return self.driver.find_element(*TodoPageLocators.clear_completed_button).text

    def clear_completed_tasks(self):
        button_clear_completed = self.driver.find_element(*TodoPageLocators.clear_completed_button)
        button_clear_completed.click()

    def get_todo_count_text(self):
        return self.driver.find_element(*TodoPageLocators.todo_count).text

    def add_multiple_tasks(self, tasks):
        for task in tasks:
            self.add_task(task)

    def get_remaining_tasks(self):
        return self.driver.find_elements(*TodoPageLocators.todo_list_items)

    def mark_all_tasks_completed(self):
        mark_all_checkbox = self.driver.find_element(*TodoPageLocators.toggle_all)
        mark_all_checkbox.click()

    def are_all_tasks_completed(self):
        task_elements = self.driver.find_elements(*TodoPageLocators.todo_list_items)
        return all("completed" in task.get_attribute("class") for task in task_elements)

    def mark_all_tasks(self):
        mark_all_checkbox = self.driver.find_element(*TodoPageLocators.toggle_all)
        mark_all_checkbox.click()
