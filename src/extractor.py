# тут пишем
import spacy
from spacy.lang.ru import Russian
import textract
import os
import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
from collections import namedtuple

from src.text_reading import Book
from src.sentences import SentenceSyntax
from src.rules import Rules


class Extractor:
    def __init__(self, path_to_book, nom=0, gen=0, voc=0,
                 impers=0, defpers=0, vagpers=0, infinit=0):
        self.book = Book(path_to_book)
        self._sentences = self.book.get_sentence()
        SentNumber = namedtuple("SentNumber",
                                "nominative genitive vocative impersonal defpersonal vagpersonal infinitive")
        self.number_of_sentences = SentNumber(nom, gen, voc, impers, defpers, vagpers, infinit)
        self.all_types = self.find_sentences()

    def find_sentences(self):
        # список типов предложений которые мы ищем
        all_sent = {}
        for key, value in self.number_of_sentences._asdict():
            if value > 0:
                all_sent[key] = []
        for one_sent in self._sentences:
            while  True: # какое-то условие
                sentence = SentenceSyntax(one_sent)
                root_pos = sentence.root_pos
                rules = Rules(sentence)
                if root_pos == 'NOUN':
                    sent_type = self.nominal_sentence(rules)
                    # вызываем метод для именных
                    # Нужно прописать логику добавления если sent_type не None в нужный список
                elif root_pos == 'VERB':
                    sent_type = self.verbal_sentence()
                else:
                    continue

    def nominal_sentence(self, rules: Rules):
        """
        Обрабатываем именные, вокативные и генитивные предложения
        :return: sentence_type=str (nominative, genitive, vocative)
        """
        if rules.check_nominative():
            return 'nominative'
        if rules.check_vocative():
            return 'vocative'
        if rules.check_genitive():
            return 'genitive'
        return None

    def verbal_sentence(self, rules):
        if rules.check_infinitive():
            return 'infinitive'
        if rules.check_defpersonal():
            return 'defpersonal'
        if rules.check_vagpersonal():
            return 'vagpersonal'
        if rules.check_impersonal():
            return 'impersonal'

        return None
