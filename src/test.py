
from unittest import TestCase, main


def div(a, b) -> float:
    return a / b


class UnitTest(TestCase):

    def test_login_window(self):
        for item in range(1, 200000):
            result: float = div(1, item)
        # self.assertEqual(result, 0.5)


if __name__ == "__main__":
    main()
