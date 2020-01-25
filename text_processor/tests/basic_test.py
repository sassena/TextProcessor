import unittest
from text_processor.process import TextProcessor


class TestProcessor(unittest.TestCase):
    def setUp(self):
        self.p = TextProcessor()

    def test_punct(self):
        s = 'Ciao, come ti chiami?'
        self.assertEqual(self.p.remove_punct(s), 'Ciao come ti chiami')

    def test_spaces(self):
        s = ' What is  your name? ?'
        self.assertEqual(self.p.remove_spaces(s), 'What is your name? ?')

    def test_html(self):
        s = '<a href="http://www.website.com">keep only this</a>'
        print(self.p.strip_html(s))
        self.assertEqual(self.p.strip_html(s), "keep only this")

    def test_accents(self):
        s = "José"
        self.assertEqual(self.p.remove_accents(s), "Jose")

    def test_stopwords(self):
        s = "I am from Latin America"
        self.assertEqual(self.p.remove_stopwords(s), "Latin America")

    def test_tokenize(self):
        s = "hi my name is"
        self.assertListEqual(self.p.tokenize(s), ["hi", "my", "name", "is"])

    def test_preprocess(self):
        s = "Hi, my name is José, I am from Latin America. How are you?"
        self.assertIsInstance(self.p.preprocess(s), list)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestProcessor('test_preprocessor'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())



