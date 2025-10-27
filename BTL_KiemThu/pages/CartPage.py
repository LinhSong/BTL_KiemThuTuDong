from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_btn = (By.CSS_SELECTOR, "button.add_to_cart, button.btn_add_cart")
        self.cart_icon = (By.CSS_SELECTOR, "a[href*='cart'], .header-cart a")
        self.cart_product_name = (By.CSS_SELECTOR, ".ajaxcart__product-name.h4")

    def add_to_cart(self):
        """Click vào nút thêm vào giỏ hàng"""
        add_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_btn)
        )
        add_btn.click()

    def go_to_cart(self):
        """Đi đến giỏ hàng"""
        cart_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_icon)
        )
        cart_icon.click()

    def is_product_in_cart(self, expected_name):
        """Kiểm tra sản phẩm có trong giỏ hàng không"""
        try:
            # Chờ đến khi tên sản phẩm xuất hiện trong giỏ
            products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.cart_product_name)
            )
            # So sánh tên sản phẩm trong giỏ với tên mong đợi
            for p in products:
                if expected_name.lower() in p.text.lower():
                    return True
            return False
        except Exception as e:
            print(f"Lỗi khi kiểm tra giỏ hàng: {e}")
            return False
