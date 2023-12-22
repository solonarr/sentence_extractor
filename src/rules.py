from src.sentences import SentenceSyntax

class Rules:
    def __init__(self, sentence: SentenceSyntax):
        self.sentence = sentence
        self.sent_info = sentence.get_sent_info()
        self.root_morph = sentence.get_root_morph()
        self.root_pos = sentence.root_pos

    def check_nominative(self):
        """
        ифы для номинатива
        :return: True or False
        """
        pass

    def check_genitive(self):
        """
        ифы для генитива
        :return: True or False
        """
        pass

    def check_vocative(self):
        """
        ифы для вокатива
        :return: True or False
        """
        pass

    def check_infinitive(self):
        """
        ифы для инфинитивных
        :return: True or False
        """
        pass