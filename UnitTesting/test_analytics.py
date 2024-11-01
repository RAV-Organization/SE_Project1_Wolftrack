import unittest
from flask import Flask
from bs4 import BeautifulSoup
from app import app  # Replace with the actual name of your Flask app


class TestChartRendering(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the test client
        cls.client = app.test_client()

    def test_chart_elements_present(self):
        # Make a request to the Flask endpoint
        response = self.client.get("/stats")
        self.assertEqual(response.status_code, 200)

        # Parse the HTML response
        soup = BeautifulSoup(response.data, 'html.parser')

        # Check for CanvasJS chart container
        canvas_chart = soup.find(id="chartContainer")
        self.assertIsNotNone(canvas_chart)

        # Check for static bar chart container
        chart_area = soup.find(class_="chart-area")
        self.assertIsNotNone(chart_area)

        # Check if Y-axis labels are present
        y_axis_labels = soup.find_all(class_="y-axis-values")
        self.assertTrue(len(y_axis_labels) > 0)

        # Verify the bar elements are loaded (number may vary based on your test data)
        bars = soup.find_all(class_="bar")
        self.assertEqual(len(bars), 5)


if __name__ == "__main__":
    unittest.main()
