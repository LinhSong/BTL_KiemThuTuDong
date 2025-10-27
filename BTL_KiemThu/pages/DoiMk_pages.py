from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class DoiMKPage:
    def __init__(self, driver):
        self.driver = driver
        # Locator
        self.old_pass_input = (By.ID, "OldPass")
        self.new_pass_input = (By.ID, "changePass")
        self.confirm_pass_input = (By.ID, "confirmPass")
        self.submit_button = (By.XPATH, "//button[contains(text(),'Đặt lại mật khẩu')]")


    def open(self):
        """Mở trang đổi mật khẩu"""
        self.driver.get("https://rubies.vn/account/changepassword")

    def change_password(self, old_pass, new_pass, confirm_pass):
        """Nhập dữ liệu và đổi mật khẩu"""
        self.driver.find_element(*self.old_pass_input).send_keys(old_pass)
        self.driver.find_element(*self.new_pass_input).send_keys(new_pass)
        self.driver.find_element(*self.confirm_pass_input).send_keys(confirm_pass)
        self.driver.find_element(*self.submit_button).click()

    def get_message(self):
        """Tìm thông báo lỗi/thành công"""
        try:
            msg = self.driver.find_element(
                By.CSS_SELECTOR,
                 ".form-error, .alert, .error, .message, .text-danger, h1"
            )
            return msg.text.strip()
        except NoSuchElementException:
                return ""
