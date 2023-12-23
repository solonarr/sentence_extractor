import unittest

from src.extractor import Extractor
from src.sentences import SentenceSyntax
from src.rules import Rules

from pathlib import Path


class ExtractorBaseTests(unittest.TestCase):

    def test_create_search_sent(self):
        path_to_book = Path(__file__).parent.parent / './texts/test.txt'
        extractor_instance = Extractor(path_to_book=path_to_book, nom=2, impers=1)
        sample = {'nominative': [],
                  'impersonal': []}
        result = extractor_instance.create_search_sent()
        self.assertDictEqual(sample, result)

    def test_create_search_sent_empty(self):
        path_to_book = Path(__file__).parent.parent / './texts/test.txt'
        extractor_instance = Extractor(path_to_book=path_to_book)
        sample = {}
        result = extractor_instance.create_search_sent()
        self.assertDictEqual(sample, result)

    def test_create_search_other_sent(self):
        path_to_book = Path(__file__).parent.parent / './texts/test.txt'
        extractor_instance = Extractor(path_to_book=path_to_book, gen=3, nom=2, impers=1)
        sample = {
            'nominative': [],
            'genitive': [],
            'impersonal': []
        }
        result = extractor_instance.create_search_sent()
        self.assertDictEqual(sample, result)

    def test_find_sentence(self):
        path_to_book = Path(__file__).parent.parent / './texts/test.txt'
        extractor_instance = Extractor(path_to_book=path_to_book, nom=2, vagpers=1)
        sample = {'nominative': ['Снег да горки.', 'Зима.'],
                  'vagpersonal': ['В дверь постучали.']}
        result = extractor_instance.get_searched_sentences()
        self.assertDictEqual(sample, result)

    def test_find_sentence_empty(self):
        path_to_book = Path(__file__).parent.parent / './texts/test.txt'
        extractor_instance = Extractor(path_to_book=path_to_book)
        sample = {}
        result = extractor_instance.get_searched_sentences()
        self.assertDictEqual(sample, result)

    def test_nominal_sentence_nominatives(self):
        sentence = SentenceSyntax('Снег да горки.')
        rule = Rules(sentence)
        sample = 'nominative'
        result = Extractor.nominal_sentence(rule)
        self.assertEqual(sample, result)

    def test_nominal_sentence_genitives(self):
        sentence = SentenceSyntax('Народу!')
        rule = Rules(sentence)
        sample = 'genitive'
        result = Extractor.nominal_sentence(rule)
        self.assertEqual(sample, result)

    def test_verbal_sentence_impersonal(self):
        sentence = SentenceSyntax('Стало очень холодно.')
        rule = Rules(sentence)
        sample = 'impersonal'
        result = Extractor.verbal_sentence(rule)
        self.assertEqual(sample, result)

    def test_verbal_sentence_infinitive(self):
        sentence = SentenceSyntax('Мне бы уснуть.')
        rule = Rules(sentence)
        sample = 'infinitive'
        result = Extractor.verbal_sentence(rule)
        self.assertEqual(sample, result)

    def test_getter_test(self):
        path_to_book = Path(__file__).parent.parent / './texts/test.txt'
        extractor_instance = Extractor(path_to_book=path_to_book, nom=2, vagpers=1)
        sample = {'nominative': ['Снег да горки.', 'Зима.'],
                  'vagpersonal': ['В дверь постучали.']}
        result = extractor_instance.get_searched_sentences()
        self.assertDictEqual(sample, result)

    def test_getter_test_empty(self):
        path_to_book = Path(__file__).parent.parent / './texts/test.txt'
        extractor_instance = Extractor(path_to_book=path_to_book)
        sample = {}
        result = extractor_instance.get_searched_sentences()
        self.assertDictEqual(sample, result)


if __name__ == '__main__':
    unittest.main()
