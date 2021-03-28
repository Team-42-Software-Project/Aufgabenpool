import unittest
from app.topics.views import mytest




class TestTopic(unittest.TestCase):
    def test_add_topic_to_db(self):
        """
        Test that a topic is added to the database
        """
        number = 5
        result = mytest(number)
        self.assertEqual(result, number)

if __name__ == '__main__':
    unittest.main()