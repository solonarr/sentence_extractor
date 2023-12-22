"""
I guess we should do a sent_extractor here
"""
import spacy
import pymorphy2


class SentenceSyntax:

    def __init__(self, sentence):
        self.sentence = sentence
        self.morph_analyzer = pymorphy2.MorphAnalyzer()
        nlp = spacy.load("ru_core_news_sm")
        self.doc = nlp(sentence)
        self.root, self.root_pos, self.root_morph = self.get_root_morph()

    def get_root_morph(self):
        """
        get sentence root and its morph characteristics
        :return: text of root, morph characteristic of root
        morph: dictionary with characteristics
        """
        for token in self.doc:
            if token.dep_ == 'ROOT':
                morph = self.morph_analyzer(token.text)[0]
                return token.text, token.pos, morph

    def get_root_morph(self):
        return self.root_morph

# короче хз че тут еще добавить, думаю насчет создания списков морф критериев и т.д
