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
        if self.root_pos == 'INFN':
            return True
        else:
            for word in self.sent_info:
                if word['dep'] == 'cop' and word['pos'] == 'INFN':
                    return True
        return False

    def check_impersonal(self):
        """
        ифы для безличных
        :return: True or False
        """
        # первый случай: сказуемое выражено предикативом
        if self.root_pos == 'PRED':
            return True
        else:
            for tag in self.root_morph:
                if 'PRDx' in tag:
                    return True
        # второй случай: сказуемое - безличный глагол
        if 'Impe' in self.root_morph or 'Impx' in self.root_morph:
            return True
        # третий случай: сказуемое - личный глагол прош. вр. ср. рода ед. ч.
        if self.root_pos == 'VERB' and \
                'neut' in self.root_morph and \
                'sing' in self.root_morph and \
                'past' in self.root_morph:
            return True
        # четвертый случай: краткое страдательное причастие прошедшего времени
        if self.root_pos == 'PRTS' and \
            'perf' in self.root_morph and \
            'past' in self.root_morph and \
            'pssv' in self.root_morph and \
            'neut' in self.root_morph and \
            'sing' in self.root_morph:
            return True
        return False


    def check_defpersonal(self):
        """
        ифы для определенно-личных
        :return: True or False
        """
        pass

    def check_vagpersonal(self):
        """
        ифы для неопределенно-личных
        :return: True or False
        """
        pass
