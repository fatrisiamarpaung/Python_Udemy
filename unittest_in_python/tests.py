from socket import fromfd
import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        self.assertEqual(
            eat("brocoli", is_healthy=True),
            "Im eating brocoli, beacuse my body is a temple"
        )
    def test_eat_unhealty(self):
          self.assertEqual(
            eat("pizza", is_healthy=False),
             "Im eating pizza because YOLO"
        )
    def test_short_nap(self):
        self.assertEqual(
            nap(6),
            "I'm feeling refreshed after my 1 hour nap"
        )
    def test_long_nap(self):
        self.assertEqual(
            nap(12),
            "Ugh I overslept. I didnt mean to nap for 12 hour"
        )
if __name__ == '__main__':
    unittest.main()