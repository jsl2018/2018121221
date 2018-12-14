import allure
import pytest


class Test01():
    @allure.step(title="测试步骤001")
    def test001(self):
        allure.attach("描述", "我是测试步骤001的描述")
        print("test001被执行了")

    def test002(self):
        print("test002被执行了")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test003(self):
        print("test003被执行了")
        assert 0

    def test004(self):
        print("test004被执行了")
