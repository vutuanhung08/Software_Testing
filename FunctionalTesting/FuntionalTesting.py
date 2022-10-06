import unittest


def electricity_to_money(e):
    if not isinstance(e, int) or e < 0:
        return -1
    elif e <= 50:
        money = (e * 1678) * 1.08
    elif e <= 100:
        money = (83900 + (e - 50) * 1734) * 1.08
    elif e <= 200:
        money = (170600 + (e - 100) * 2014) * 1.08
    elif e <= 300:
        money = (372000 + (e - 200) * 2536) * 1.08
    elif e <= 400:
        money = (625600 + (e - 300) * 2834) * 1.08
    else:
        money = (909000 + (e - 400) * 2927) * 1.08
    return round(money)


class TestBoundaryValue(unittest.TestCase):
    def test_electricity_to_money_case1(self):
        self.assertEqual(electricity_to_money(0), 0)

    def test_electricity_to_money_case2(self):
        self.assertEqual(electricity_to_money(1), 1812)

    def test_electricity_to_money_case3(self):
        self.assertEqual(electricity_to_money(100), 184248)

    def test_electricity_to_money_case4(self):
        self.assertEqual(electricity_to_money(2147483646), 6788539119645)

    def test_electricity_to_money_case5(self):
        self.assertEqual(electricity_to_money(2147483647), 6788539122807)


class TestEquivalencePartitioning(unittest.TestCase):
    def test_electricity_to_money_case1(self):
        self.assertEqual(electricity_to_money(-10), -1)

    def test_electricity_to_money_case2(self):
        self.assertEqual(electricity_to_money(17), 30808)

    def test_electricity_to_money_case3(self):
        self.assertEqual(electricity_to_money(51), 92485)

    def test_electricity_to_money_case4(self):
        self.assertEqual(electricity_to_money(200), 401760)

    def test_electricity_to_money_case5(self):
        self.assertEqual(electricity_to_money(255), 552398)

    def test_electricity_to_money_case6(self):
        self.assertEqual(electricity_to_money(333), 776652)

    def test_electricity_to_money_case7(self):
        self.assertEqual(electricity_to_money(567), 1509634)
