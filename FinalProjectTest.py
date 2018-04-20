import unittest
from FinalProject import *

class testdatabase(unittest.TestCase):
    def test_top_ten2(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = '''SELECT Google.City, Google.Name, Google.Rating
        FROM Google JOIN Yelp ON Google.Id = Yelp.Id WHERE Google.Keyword = 'Mexican'
        AND Google.City = 'Bloomington'
        ORDER BY Google.Rating DESC LIMIT 3'''
        results = cur.execute(sql)
        result_list = results.fetchall()

        self.assertEqual(result_list[0][0], 'Bloomington')
        self.assertEqual(result_list[0][2],  4.6)
        self.assertEqual(result_list[0][0], 'Bloomington')
        conn.close()
    def test_top_ten1(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = '''SELECT Google.City, Google.Name, Google.Rating
        FROM Google JOIN Yelp ON Google.Id = Yelp.Id WHERE Google.Keyword = 'Mexican'
        AND Google.City = 'Bloomington'
        ORDER BY Google.Rating DESC LIMIT 3'''
        results = cur.execute(sql)
        result_list = results.fetchall()

        self.assertEqual(result_list[0][0], 'Bloomington')
        self.assertEqual(result_list[0][1], 'Taqueria El Porton')
        conn.close()
    def test_top_restaurant2(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = '''SELECT Google.City, Google.Name, Google.RATING FROM Google
         JOIN Yelp ON Google.Id = Yelp.Id WHERE Google.Type = 'restaurant'
         AND Google.City = 'Ann Arbor'
         ORDER BY Google.Rating DESC LIMIT 3'''
        results = cur.execute(sql)
        result_list = results.fetchall()

        self.assertEqual(result_list[0][0], 'Ann Arbor')
        self.assertEqual(result_list[0][1], 'Taste Kitchen')
        conn.close()

    def test_top_restaurant1(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = '''SELECT Google.City, Google.Name, Google.RATING FROM Google
         JOIN Yelp ON Google.Id = Yelp.Id WHERE Google.Type = 'restaurant'
         AND Google.City = 'Nashville'
         ORDER BY Google.Rating DESC LIMIT 3'''
        results = cur.execute(sql)
        result_list = results.fetchall()

        self.assertEqual(result_list[0][2], 4.5)
        self.assertEqual(result_list[0][0], 'Nashville')
        self.assertEqual(result_list[0][2], 4.5)
        conn.close()
    def test_top_city2(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = '''SELECT Google.City, Google.Type, AVG(Google.RATING) AS average FROM Google
        JOIN Yelp ON Google.Id = Yelp.Id WHERE Google.Type = 'restaurant'
        AND Google.City = 'Dallas'
        AND Google.Keyword = 'Italian'
        ORDER BY Google.Rating DESC LIMIT 3'''

        results = cur.execute(sql)
        result_list = results.fetchall()

        self.assertEqual(result_list[0][1], 'restaurant')
        self.assertEqual(result_list[0][2], 4.3)
        self.assertEqual(result_list[0][0], 'Dallas')
        conn.close()
    def test_top_city1(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = '''SELECT Google.City, Google.Type, AVG(Google.RATING) AS average FROM Google
        JOIN Yelp ON Google.Id = Yelp.Id WHERE Google.Type = 'restaurant'
        AND Google.City = 'Ann Arbor'
        AND Google.Keyword = 'American'
        ORDER BY Google.Rating DESC LIMIT 3'''

        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertEqual(result_list[0][0], 'Ann Arbor')
        self.assertEqual(result_list[0][1],'restaurant')
        conn.close()



unittest.main()
