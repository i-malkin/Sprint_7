import allure
from framework.create_order_objects import CreateOrder

class TestOrder:
    @allure.title("Проверка успешности создания заказа")
    def test_create_order(self, order_data):
        order = CreateOrder()
        order.send_order_request(order_data)
        order.check_send_request()
        order.check_response_is_201()