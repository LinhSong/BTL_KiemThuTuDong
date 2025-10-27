from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class DangKyPage:
    def __init__(self, driver):
        self.driver = driver
        self.ho_input = (By.ID, "lastName")
        self.ten_input = (By.ID, "firstName")
        self.email_input = (By.NAME, "email")
        self.sdt_input = (By.NAME, "PhoneNumber")
        self.password_input = (By.ID, "password")
        self.register_button = (By.CSS_SELECTOR, "button.btn.btn-style")

    def open(self):
        self.driver.get("https://rubies.vn/account/register")

    def register(self, ho, ten, email, sdt, password):
        self.driver.find_element(*self.ho_input).send_keys(ho)
        self.driver.find_element(*self.ten_input).send_keys(ten)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.sdt_input).send_keys(sdt)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.register_button).click()
    
    def error_messages(self):
        try:
            errors = self.driver.find_elements(
                By.CSS_SELECTOR,
                ".invalid-feedback, .form-error, .alert-danger, .errors, .alert"
            )
            for e in errors:
                text = e.text.strip()
                if text:
                    return text
            try:
                h1 = self.driver.find_element(By.TAG_NAME, "h1").text.strip()
                if h1:
                    return h1
            except:
                pass
            return "Không tìm thấy kết quả"

        except:
            return "Không tìm thấy kết quả"