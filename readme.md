# Automation Testing with Selenium Chrome Driver and Demo QA

## Introduction
This project demonstrates automation testing using Selenium Chrome Driver on the Demo QA website.

## Prerequisites
- Python
- pip (Python package installer)
- Selenium
- ChromeDriver
- Visual Studio Code (VS Code)

## Setup

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install dependencies:**
    Ensure you have pip installed and run:
    ```sh
    pip install selenium
    ```

3. **Download ChromeDriver:**
    Download the ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your project directory.

## Running Tests

1. **Configure ChromeDriver path:**
    Update the path to ChromeDriver in your test setup.

2. **Execute tests:**
    Run the tests using VS Code or via command line:
    ```sh
    python -m unittest discover
    ```

## Project Structure

- `tests`: Contains test cases.
- `requirements.txt`: Python dependencies file.

## Writing Tests

Here's an example of a simple test case:

```python
import unittest
from selenium import webdriver

class DemoQATest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='path/to/chromedriver')

    def test_demo_qa(self):
        self.driver.get("https://demoqa.com")
        # Add your test steps here

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```

## Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/en/)
- [Demo QA](https://demoqa.com)

## License

This project is licensed under the MIT License.
