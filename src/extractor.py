from collections import namedtuple

from src.rules import Rules
from src.sentences import SentenceSyntax
from src.text_reading import Book


class Extractor:

    SentNumber = namedtuple("SentNumber",
                            "nominative genitive impersonal \
                            defpersonal vagpersonal infinitive")

    def __init__(self, path_to_book, nom=0, gen=0,
                 impers=0, defpers=0, vagpers=0, infinit=0):
        self.book = Book(path_to_book)
        # self._sentences = self.book.get_sentence()
        self.number_of_sentences = Extractor.SentNumber(nom, gen,
                                                        impers, defpers,
                                                        vagpers, infinit)

    def create_search_sent(self):
        all_sent = {}

        for key, value in self.number_of_sentences._asdict().items():
            if value > 0:
                all_sent[key] = []

        return all_sent

    def find_sentences(self):
        all_sent = self.create_search_sent()

        for one_sent in self.book.sentences:
            if any(len(value) < getattr(self.number_of_sentences, key)
                   for key, value in all_sent.items()):

                sentence = SentenceSyntax(one_sent)
                root_pos = sentence.root_pos
                rules = Rules(sentence)

                if root_pos == 'NOUN':
                    sent_type = self.nominal_sentence(rules)
                elif root_pos == 'VERB':
                    sent_type = self.verbal_sentence(rules)
                else:
                    continue

                if sent_type:
                    if sent_type in all_sent:
                        if (len(all_sent[sent_type]) <
                                getattr(self.number_of_sentences, sent_type)):
                            all_sent[sent_type].append(sentence.get_text())
            else:
                return all_sent

        return all_sent

    @staticmethod
    def nominal_sentence(rules: Rules):
        """
        Обрабатываем именные, вокативные и генитивные предложения
        :return: sentence_type=str (nominative, genitive, vocative)
        """
        if rules.check_nominative():
            return 'nominative'
        if rules.check_genitive():
            return 'genitive'
        return None

    @staticmethod
    def verbal_sentence(rules: Rules):
        if not rules.check_single_compound():
            return None
        if rules.check_infinitive():
            return 'infinitive'
        if rules.check_defpersonal():
            return 'defpersonal'
        if rules.check_vagpersonal():
            return 'vagpersonal'
        if rules.check_impersonal():
            return 'impersonal'
        return None

    def get_searched_sentences(self):
        searched_sentences = self.find_sentences()
        return searched_sentences
