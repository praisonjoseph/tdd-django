from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')
        self.assertIn('To Do',self.browser.title)
        self.fail('Finish the test')
        # she is invited to enter a To do item straight away.

        # She types "Buy peacock feathers" into a text box

        # When she hits enter, the pages updates, and now the pages lists
        # "1: Buy peacock feathers" as an item in a to do list

        # There is still a text box inviting her to add another item. she
        # enter "Use peacock feathers to make a fly"

        # The page updates again and list both the items on her list.

        # Edith wonders if the site will remember her list. Then she sees that the site has generated  a unique URL for her 

        # She visits the URL. her todo lists are still there

        # Satisfied she goes to sleep

if __name__ == '__main__':
    unittest.main()