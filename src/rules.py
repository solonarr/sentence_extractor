from src.sentences import SentenceSyntax


class Rules:
    def __init__(self, sentence: SentenceSyntax):
        self.sentence = sentence
        self.sent_info = sentence.get_sentence_info()
        self.root_morph = sentence.get_root_morph()
        self.root_pos = sentence.root_pos
        self.text = sentence.get_text()

    def check_nominative(self):
        """
        ифы для номинатива
        :return: True or False
        """
        if self.root_pos != 'NOUN':
            return False

        for morph_tag in self.root_morph:
            if 'nomn' in morph_tag.tag:
                return True

    def check_genitive(self):
        """
        ифы для генитива
        :return: True or False
        """
        if self.root_pos != 'NOUN':
            return False

        for morph_tag in self.root_morph:
            if 'gen2' in morph_tag.tag or 'gent' in morph_tag.tag:
                return True

    def check_single_compound(self):
        for elem in self.sent_info:
            if (elem.get('dep') == 'csubj'
                    or 'nomn' in elem.get('morph')[0].tag):
                return False
        return True

    def check_infinitive(self):
        """
        ифы для инфинитивных
        :return: True or False
        """
        if self.root_pos == 'VERB':
            for tag in self.root_morph:
                if 'INFN' in tag.tag:
                    return True
        else:
            for elem in self.sent_info:
                if (elem.get('dep') == 'cop'
                        and 'INFN' in elem.get('morph')[0].tag):
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
                if 'Prdx' in tag.tag:
                    return True
        for word in self.sent_info:
            if word.get('dep') == 'xcomp' and word.get('pos') == 'PRED' \
                    or 'Prdx' in word['morph'][0].tag:
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
        for tag in self.root_morph:
            if '1per' in tag.tag or '2per' in tag.tag or 'impr' in tag.tag:
                return True
        return False

    def check_vagpersonal(self):
        """
        ифы для неопределенно-личных
        :return: True or False
        """
        for tag in self.root_morph:
            if '3per' in tag.tag and 'plur' in tag.tag:
                return True
            elif 'plur' in tag.tag and 'past' in tag.tag:
                return True
        return False
