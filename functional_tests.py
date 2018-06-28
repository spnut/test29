from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_app(self):
        self.browser.get('http://localhost:8000/quiz')
        self.assertIn('Quiz', self.browser.title)
        create_page_bt = self.browser.find_element_by_name('create')
        self.assertEqual(create_page_bt.get_attribute('value'), 'Create Quiz')
        time.sleep(2)
        create_page_bt.click()

        # Create Quiz Page
        ############################################## Create Question ##############################################

        self.assertIn('Create Quiz', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('H1').text
        self.assertIn('Quiz Test', header_text)

        question_text = self.browser.find_element_by_tag_name('H3').text
        self.assertIn('Create Quiz', question_text)
        question_box = self.browser.find_element_by_name('quizbox')
        self.assertEqual(question_box.get_attribute('placeholder'), 'enter you quiz')
        question_box.send_keys('Fish is cat')
        time.sleep(2)

        choice_text = self.browser.find_element_by_tag_name('H4').text
        self.assertIn('Create Choice', choice_text)

        choice1_box = self.browser.find_element_by_name('a')
        self.assertEqual(choice1_box.get_attribute('placeholder'), 'Enter your choice1')
        choice1_box.send_keys('True')
        time.sleep(2)

        choice2_box = self.browser.find_element_by_name('b')
        self.assertEqual(choice2_box.get_attribute('placeholder'), 'Enter your choice2')
        choice2_box.send_keys('False')
        time.sleep(2)

        ans_text = self.browser.find_element_by_tag_name('H5').text
        self.assertIn('Create Answer', ans_text)

        ans_box = self.browser.find_element_by_name('answer')
        self.assertEqual(ans_box.get_attribute('placeholder'), 'Enter your answer')
        ans_box.send_keys('False')

        submit_bt = self.browser.find_element_by_name('enter')
        submit_bt.click()

        ############################################## Go to Quiz ##############################################

        go_to_quiz_bt = self.browser.find_element_by_name('quiz')
        self.assertEqual(go_to_quiz_bt.get_attribute('value'), 'Go to Quiz')
        go_to_quiz_bt.click()
        time.sleep(2)


        ########################################## Show question page ##########################################
        header_text_show_quiz = self.browser.find_element_by_tag_name('H1').text
        self.assertIn('Select your Quiz', header_text_show_quiz)

        select_quiz = self.browser.find_element_by_id("q1")
        self.assertEqual(select_quiz.get_attribute('name'), 'Fish is cat')
        select_quiz.click()

        ########################################### Detail Quiz page ###########################################
        # select choice
        show_question_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Fish is cat', show_question_text)

        choice_1 = self.browser.find_element_by_id("c1")
        self.assertEqual(choice_1.get_attribute('value'), 'True')

        choice_2 = self.browser.find_element_by_id("c2")
        self.assertEqual(choice_2.get_attribute('value'), 'False')
        choice_2.click()
        time.sleep(2)

        submit_Bt = self.browser.find_element_by_id('send')
        self.assertEqual(submit_Bt.get_attribute('value'), 'submit')
        submit_Bt.click()
        time.sleep(2)

        ############################################# result page #############################################
        self.assertIn('result', self.browser.title)
        result_text = self.browser.find_element_by_tag_name('p').text
        self.assertIn('You answer True', result_text)

        back_to_quiz_bt = self.browser.find_element_by_id("back")
        self.assertEqual(back_to_quiz_bt.get_attribute('value'), 'Back to Quiz')
        back_to_quiz_bt.click()
        time.sleep(2)

        self.fail('Finish the test!')


if __name__ == '__main__':
   unittest.main(warnings='ignore')