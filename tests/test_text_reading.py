import unittest
from src.text_reading import Book, UnknownExtensionError
from pathlib import Path


class BookBaseTests(unittest.TestCase):

    def test_extract_txt_empty_file(self):
        path = Path(__file__).parent.parent / './texts/test_empty.txt'
        book = Book(path)
        extracted_text = book.extract_txt(path)
        self.assertEqual(extracted_text, None)

    def test_read_text_file_extension_doesnt_exist(self):
        path = Path(__file__).parent.parent / './texts/test.pdf'
        with self.assertRaises(UnknownExtensionError):
            Book(path)

    def test_get_sentence_returns_correct_sent(self):
        path = Path(__file__).parent.parent / './texts/test.txt'
        book = Book(path)
        self.assertEqual(book.sentences, ['Проходите, пожалуйста.', 'Посмотрю попозже.',
                                          'Поедем вместе.',
                                          'В дверь постучали.', 'Тебе позвонят и скажут.',
                                          'Нам подали ужин.',
                                          'Снег да горки.', 'Зима.', 'Только бы счастье!',
                                          'Хлеба!', 'Народу!','Еды.', 'Стало очень холодно.',
                                          'Уже смеркается.', 'У меня нет никаких проблем.',
                                          'Про батарею Тушина было забыто.',
                                          'Мне сильно давило на голову.', 'Дать детям детство!',
                                          'Стоять!', 'Мне бы уснуть.', 'И что теперь делать?',
                                          'Быть грозе великой!'])

    def test_get_sentences_deals_with_difficult_sent(self):
        path = Path(__file__).parent.parent / './texts/test_random.txt'
        book = Book(path)
        self.assertEqual(book.sentences, ['ой .. 6.', 'привеет!!т.т.',
                                          'хай.."?\\\\'])


if __name__ == '__main__':
    unittest.main()
