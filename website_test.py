import unittest
from urllib.request import urlopen

class WebsiteTest(unittest.TestCase):
    def test_website_load(self):
        url = "https://atg.world"
        
        # Step 1: Print a message indicating that the test is starting
        print("Starting website load test...")
        
        # Step 2: Try to open the URL and retrieve the response
        try:
            response = urlopen(url)
            
            # Step 3: Check the HTTP status code to determine if the website loaded successfully
            if response.getcode() == 200:
                # Step 4: Print a success message if the website loaded successfully
                print("Website loaded successfully!")
            else:
                # Step 5: Print an error message if the website did not load successfully
                print("Website did not load successfully!")
                self.fail("Website load test failed.")
        except Exception as e:
            # Step 6: Print an error message if an exception occurred while trying to open the URL
            print(f"An exception occurred: {e}")
            self.fail("Website load test failed.")
            
        # Step 7: Print a message indicating that the test has finished
        print("Website load test completed.")

if __name__ == '__main__':
    unittest.main()

