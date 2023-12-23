import unittest
from src.rules import Rules
from src.sentences import SentenceSyntax

class RulesBaseTests(unittest.TestCase):

    def test_check_nominative(self):
        self.assertEqual(True, False)



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



if __name__ == '__main__':
    unittest.main()
