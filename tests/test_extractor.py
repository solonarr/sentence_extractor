import unittest

from src.extractor import Extractor
from src.sentences import SentenceSyntax
from src.rules import Rules


class ExtractorBaseTests(unittest.TestCase):

    def test_create_search_sent(self):
        extractor_instance = Extractor(path_to_book='texts/test.txt', nom=2, impers=1)
        sample = {'nominative': [],
                  'impersonal': []}
        result = extractor_instance.create_search_sent()
        self.assertDictEqual(sample, result)

    def test_create_search_sent_empty(self):
        extractor_instance = Extractor(path_to_book='texts/test.txt')
        sample = {}
        result = extractor_instance.create_search_sent()
        self.assertDictEqual(sample, result)

    def test_create_search_other_sent(self):
        extractor_instance = Extractor(path_to_book='texts/test.txt', gen=3, nom=2, impers=1)
        sample = {
            'nominative': [],
            'genitive': [],
            'impersonal': []
        }
        result = extractor_instance.create_search_sent()
        self.assertDictEqual(sample, result)

    def test_find_sentence(self):
        extractor_instance = Extractor(path_to_book='texts/test.txt', nom=2, impers=1)
        sample = {'nominative': ['Снег да горки.' 'Зима.'],
                  'impersonal': ['Стало очень холодно.']}
        result = extractor_instance.get_searched_sentences()
        self.assertDictEqual(sample, result)

    def test_find_sentence_empty(self):
        extractor_instance = Extractor(path_to_book='texts/test.txt')
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
        sentence = SentenceSyntax('Хлеба!')
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
        sentence = SentenceSyntax('Дать детям детство!')
        rule = Rules(sentence)
        sample = 'infinitive'
        result = Extractor.verbal_sentence(rule)
        self.assertEqual(sample, result)

    def test_getter_test(self):
        extractor_instance = Extractor(path_to_book='texts/test.txt', nom=2, impers=1)
        sample = {'nominative': ['Снег да горки.' 'Зима.'],
                  'impersonal': ['Стало очень холодно.']}
        result = extractor_instance.get_searched_sentences()
        self.assertDictEqual(sample, result)

    def test_getter_test_empty(self):
        extractor_instance = Extractor(path_to_book='texts/test.txt')
        sample = {}
        result = extractor_instance.get_searched_sentences()
        self.assertDictEqual(sample, result)


if __name__ == '__main__':
    unittest.main()
