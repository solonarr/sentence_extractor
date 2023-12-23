import unittest

from src.sentences import SentenceSyntax
from src.rules import Rules


class RulesBaseTests(unittest.TestCase):

    def test_check_nominative_can_define_correct_sent(self):
        text = 'Снег да горки'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_nominative()
        self.assertEqual(result, True)

    def test_check_nominative_can_differentiate_similar_sent(self):
        text = 'Кать!'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_nominative()
        self.assertEqual(result, False)

    def test_check_infinitive_can_recognise_inf_copula(self):
        text = 'Быть художником.'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_infinitive()
        self.assertEqual(result, True)

    def test_check_infinitive_can_recognise_infinitives(self):
        text = 'Не упасть бы'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_infinitive()
        self.assertEqual(result, True)

    def test_check_impersonal_differs_personal_verbs_from_impersonal(self):
        text = 'Осталась дома'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_impersonal()
        self.assertEqual(result, False)

    def test_check_impersonal_recognises_predicatives(self):
        text = 'Сегодня холодно'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_impersonal()
        self.assertEqual(result, True)

    def test_check_defpersonal_ind(self):
        text = 'Пойдем со мной.'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_defpersonal()
        self.assertEqual(result, True)

    def test_check_defpersonal_impr(self):
        text = 'Принеси отцу пива.'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_defpersonal()
        self.assertEqual(result, True)

    def test_check_vagpersonal_in_pres(self):
        text = 'Тебя зовут гулять.'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_vagpersonal()
        self.assertEqual(result, True)

    def test_check_vagpersonal_in_past(self):
        text = 'В дверь позвонили.'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_vagpersonal()
        self.assertEqual(result, True)

    def test_check_single_compound_detects_single_compound_sent(self):
        text = 'Пойду в магазин.'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_single_compound()
        self.assertEqual(result, True)

    def test_check_single_compound_rejects_non_single_compound_sent(self):
        text = 'Я пойду в магазин.'
        sentence = SentenceSyntax(text)
        rule = Rules(sentence)
        result = rule.check_single_compound()
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
