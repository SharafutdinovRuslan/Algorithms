import unittest
import random

from Sort.insertion_sort import insertion_sort
from Sort.selection_sort import selection_sort


class TestSorts(unittest.TestCase):

    SORTING_ALGORITHMS = (
        insertion_sort,
        selection_sort,
    )

    def setUp(self) -> None:
        self.test_cases = (
            list(range(5)),
            list(range(10)),
            list(range(20)),
            list(range(100)),
        )

    def tearDown(self) -> None:
        self.test_cases = None

    def test_simple_cases(self):

        for algorithm in self.SORTING_ALGORITHMS:
            for case in self.test_cases:
                with self.subTest(case=case, sorting_algorithm=algorithm):
                    self.assertEqual(
                        algorithm(random.sample(case, len(case))),
                        case
                    )


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSorts))
    unittest.TextTestRunner(verbosity=2).run(suite)
