import spacy
from spacy.lang.ru import Russian
import textract
import os
import nltk
from nltk.tokenize import sent_tokenize

from collections import namedtuple

from sentence_extractor.src.text_reading import Book
from sentence_extractor.src.sentences import SentenceSyntax
from sentence_extractor.src.rules import Rules

nltk.download('punkt')


class Extractor:

    SentNumber = namedtuple("SentNumber",
                            "nominative genitive vocative impersonal defpersonal vagpersonal infinitive")

    def __init__(self, path_to_book, nom=0, gen=0, voc=0,
                 impers=0, defpers=0, vagpers=0, infinit=0):
        self.book = Book(path_to_book)
        self._sentences = self.book.get_sentence()
        self.number_of_sentences = Extractor.SentNumber(nom, gen, voc, impers, defpers, vagpers, infinit)
        self.searched_sentences = self.find_sentences()

    def create_search_sent(self):
        all_sent = {}

        for key, value in self.number_of_sentences._asdict():
            if value > 0:
                all_sent[key] = []

        return all_sent

    def find_sentences(self):
        # список типов предложений которые мы ищем
        all_sent = self.create_search_sent()

        for one_sent in self._sentences:
            while any(len(value) < getattr(self.number_of_sentences, key) for key, value in all_sent.items()): # какое-то условие
                sentence = SentenceSyntax(one_sent)
                root_pos = sentence.root_pos
                rules = Rules(sentence)

                if root_pos == 'NOUN':
                    sent_type = self.nominal_sentence(rules)
                elif root_pos == 'VERB':
                    sent_type = self.verbal_sentence()
                else:
                    continue

                if sent_type:
                    if len(all_sent[sent_type]) < getattr(self.number_of_sentences, sent_type):
                        all_sent[sent_type].append(sentence.get_text())

        return all_sent

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
