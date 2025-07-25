from selenium.webdriver.common.by import By


class TodoPageLocators:
    caption = (By.CSS_SELECTOR, 'header h1')
    new_todo_input = (By.CSS_SELECTOR, '.new-todo')
    todo_count = (By.CSS_SELECTOR, '.todo-count')
    toggle = (By.CSS_SELECTOR, '.toggle')
    completed_button = (By.CSS_SELECTOR, '[href="#/completed"]')
    todo_list_items = (By.CSS_SELECTOR, "ul.todo-list li")
    clear_completed_button = (By.CSS_SELECTOR, '.clear-completed')
    toggle_all = (By.CSS_SELECTOR, 'input.toggle-all')
