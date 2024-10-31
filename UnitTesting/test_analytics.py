from selenium import webdriver
import unittest

class TestChartRendering(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize the Chrome driver
        cls.driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH or specify path here
        cls.driver.implicitly_wait(10)

    def test_chart_elements_present(self):
        # Load the page
        self.driver.get("http://localhost:5000/stats")  # Ensure your Flask app is running
        
        # Check for CanvasJS chart container
        canvas_chart = self.driver.find_element_by_id("chartContainer")
        self.assertIsNotNone(canvas_chart)

        # Check for static bar chart container
        chart_area = self.driver.find_element_by_class_name("chart-area")
        self.assertIsNotNone(chart_area)
        
        # Check if Y-axis labels are present
        y_axis_labels = self.driver.find_elements_by_class_name("y-axis-values")
        self.assertTrue(len(y_axis_labels) > 0)

        # Verify the bar elements are loaded
        bars = self.driver.find_elements_by_class_name("bar")
        self.assertEqual(len(bars), 5)  # Should match the number of companies listed

    @classmethod
    def tearDownClass(cls):
        # Close the browser window
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
