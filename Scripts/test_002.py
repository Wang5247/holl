import allure


class Test_001:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("第1步")
    def test001(self):
        print("\n test001")

    @allure.severity(allure.severity_level.CRITICAL)
    def test002(self):
        print("\n test002")
        assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test003(self):
        print("\n test003")

    @allure.severity(allure.severity_level.MINOR)
    def test004(self):
        print("\n test004")

    @allure.severity(allure.severity_level.TRIVIAL)
    def test005(self):
        print("\n test005")
