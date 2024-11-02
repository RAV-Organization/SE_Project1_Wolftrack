import unittest
from flask import Flask
from bs4 import BeautifulSoup
from app import app  

class TestChartRendering(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_chart_elements_present(self):
        response = self.client.get("/stats")
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.data, 'html.parser')

        canvas_chart = soup.find(id="chartContainer")
        self.assertIsNotNone(canvas_chart)

        chart_area = soup.find(class_="chart-area")
        self.assertIsNotNone(chart_area)

        y_axis_labels = soup.find_all(class_="y-axis-values")
        self.assertTrue(len(y_axis_labels) > 0)

        bars = soup.find_all(class_="bar")
        self.assertEqual(len(bars), 5)


if __name__ == "__main__":
    unittest.main()
