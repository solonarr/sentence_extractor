import unittest

from src.sentences import SentenceSyntax
from src.rules import Rules


class RulesBaseTests(unittest.TestCase):

    def check_nominative_can_define_correct_sent_test(self):
        text = 'Снег да горки'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_nominative()
        self.assertEqual(result, True)

    def check_nominative_can_differentiate_similar_sent_test(self):
        text = 'Кать!'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_nominative()
        self.assertEqual(result, False)

    def check_vocative_recognises_vocatives_test(self):
        text = 'Мам.'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_vocative()
        self.assertEqual(result, True)

    def check_vocative_can_differentiate_similar_sent_test(self):
        text = 'Хлеба!'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_vocative()
        self.assertEqual(result, False)

    def check_infinitive_can_recognise_inf_copula_test(self):
        text = 'Быть художником.'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_infinitive()
        self.assertEqual(result, True)

    def check_infinitive_can_recognise_infinitives_with_modal_words_test(self):
        text = 'Можно начинать собираться'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_infinitive()
        self.assertEqual(result, True)




if __name__ == '__main__':
    unittest.main()
