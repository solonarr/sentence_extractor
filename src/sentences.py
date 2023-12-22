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

# короче хз че тут еще добавить, думаю насчет создания списков морф критериев и т.д
