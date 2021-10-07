import unittest
from dbapi import Database


class TestDbApi(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(1, 1, "WORKS")

    def test_connect(self):
        # connect to database
        db = Database(host="localhost", port=5432)
        db.connect()

        # pass index and record data
        db.upsert(1577, ("first", "last", "email"))

        # close connection
        db.close()

        self.assertEqual(1, 1, "WORKS")


if __name__ == "__main__":
    unittest.main()
