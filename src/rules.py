from src.sentences import SentenceSyntax

class Rules:
    def __init__(self, sentence: SentenceSyntax):
        self.sentence = sentence
        self.sent_info = sentence.sent_info()
        self.root_morph = sentence.get_root_morph()
        self.root_pos = sentence.root_pos

    def check_nominative(self):
        """
        ифы для номинатива
        :return: True or False
        """
        if self.root_pos != 'NOUN':
            return False

        for morph_tag in self.root_morph:
            if 'nomn' in morph_tag:
                return True


    def check_genitive(self):
        """
        ифы для генитива
        :return: True or False
        """
        if self.root_pos != 'NOUN':
            return False

        for morph_tag in self.root_morph:
            if 'gen2' in morph_tag or 'gent' in morph_tag:
                return True

    def check_vocative(self):
        """
        ифы для вокатива
        :return: True or False
        """
        if self.root_pos != 'NOUN':
            return False

        for morph_tag in self.root_morph:
            if len(self.sent_info == 1) and ('voct' in morph_tag or ('nomn' in morph_tag and )):
                return True


    def check_infinitive(self):
        """
        ифы для инфинитивных
        :return: True or False
        """
        pass

    def check_impersonal(self):
        """
        ифы для безличных
        :return: True or False
        """
        pass

    def check_defpersonal(self):
        """
        ифы для определенно-личных
        :return: True or False
        """
        check_cond = []
        for elem in self.sent_info[0]:
            if 'nomn' in elem['morph'].tag or elem.get('dep') == 'csubj':
                return False
            if elem.get('dep') == 'ROOT' and '1per' in elem.get('morph').tag or '2per' in elem.get(
                    'morph').tag or 'impr' in elem.get('morph').tag:
                check_cond.append(True)
            if check_cond:
                return True
            return False

    def check_vagpersonal(self):
        """
        ифы для неопределенно-личных
        :return: True or False
        """
        pass
