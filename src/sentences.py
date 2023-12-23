"""
I guess we should do a sent_extractor here
"""
import spacy
import pymorphy2


class SentenceSyntax:

    def __init__(self, sentence):
        self.text = sentence
        self.morph_analyzer = pymorphy2.MorphAnalyzer()
        nlp = spacy.load("ru_core_news_sm")
        self.doc = nlp(sentence)
        self.sent_info, self.root, \
            self.root_pos, self.root_morph = self.get_sent_info()

    def get_sent_info(self):
        """
        get sentence root and its morph characteristics
        :return: text of root, morph characteristic of root
        morph: dictionary with characteristics
        """
        sent_info = []
        root, root_pos, root_morph = '', '', ''

        for token in self.doc:
            if token.pos == 'PNCT':
                continue
            morph = self.morph_analyzer.parse(token.text)

            token_info = {'text': token.text,
                          'pos': token.pos_,
                          'dep': token.dep_,
                          'morph': morph}

            sent_info.append(token_info)

            if token.dep_ == 'ROOT':
                root = token.text
                root_pos = token.pos_
                root_morph = morph

        return sent_info, root, root_pos, root_morph

    def get_root_morph(self):
        return self.root_morph

    def get_sentence_info(self):
        return self.sent_info

    def get_text(self):
        return self.text
