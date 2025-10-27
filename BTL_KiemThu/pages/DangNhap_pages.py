from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class DangNhapPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "customer_email")
        self.password_input = (By.ID, "customer_password")
        self.login_button = (By.XPATH, "//input[@type='submit']")

    def open(self):
        self.driver.get("https://rubies.vn/account/login")

    def login(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def error_messages(self):
        """
        Lấy thông báo lỗi hiển thị trên màn hình nếu đăng nhập thất bại
        """
        try:
            err = self.driver.find_element(By.CSS_SELECTOR, ".invalid-feedback, .form-error, .alert-danger")
            return err.text.strip()
        except NoSuchElementException:
            return ""
