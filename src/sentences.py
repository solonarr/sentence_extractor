"""
I guess we should do a sent_extractor here
"""
import spacy
from spacy.lang.ru import Russian


class SentenceSyntax:

    def __init__(self, sentence):
        self.sentence = sentence
        nlp = spacy.load("ru_core_news_sm")
        self.doc = nlp(sentence)
        self.root, self.root_morph = self.get_root_morph()

    def get_root_morph(self):
        """
        get sentence root and its morph characteristics
        :return: text of root, morph characteristic of root
        """
        for token in self.doc:
            if token.dep_ == 'ROOT':
                return token.text, token.morph
                # мне каж нам надо доставать морфологические характеристики по другому. например сделать
# короче хз че тут еще добавить, думаю насчет создания списков морф критериев и т.д
