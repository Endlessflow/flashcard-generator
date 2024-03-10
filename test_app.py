import unittest
import app

class TestApp(unittest.TestCase):

    # Check that the home page returns a 200 status code
    def test_root_status_code(self):
        tester = app.app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Check that the generate_flashcards route returns a 200 status code
    def test_generate_flashcards_status_code(self):
        tester = app.app.test_client(self)
        response = tester.post('/generate_flashcards', json={'text': 'test'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # Check that the generate_flashcards route doubles the input
    def test_generate_flashcards_output(self):
        tester = app.app.test_client(self)
        response = tester.post('/generate_flashcards', json={'text': 'test'}, content_type='application/json')
        self.assertEqual(response.json['output'], 'testtest')

if __name__ == '__main__':
    unittest.main(verbosity=2)