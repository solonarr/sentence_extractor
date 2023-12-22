"""
Reading texts from epub.
We should think about reading texts
of different types.
PDF and docx in process
"""
import textract
import os
import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')


class Book:
    def __init__(self, path):
        self.path = path
        self.ext = os.path.splitext(self.path)[-1]
        self._text = self.read_text(self.path)
        self.sentences = self.get_sentence()

    def read_text(self, path):
        """
        Get string from path
        :param path: path to file
        :return: str with text from path
        """
        if self.ext == '.epub':
            return self.extract_epub(path)
        elif self.ext == '.txt':
            return self.extract_txt(path)

    @staticmethod
    def extract_epub(path):
        """
        Get string from epub file
        :param path: path to epub file
        :return: str from epub file
        """
        text = textract.process(path, encoding='utf-8').decode()
        return text

    @staticmethod
    def extract_txt(path):
        """
        Get string from txt file
        :param path: path to txt file
        :return: str from txt file
        """
        with open(path, 'r') as f:
            text = f.read()
        return text

    def get_text(self):
        return self._text

    def get_sentence(self):
        sentences = sent_tokenize(self._text)
        if self.ext == '.epub':
            sentences[0] = sentences[0].split('\n')[-1]  # because otherwise the name and the cover gets in
        return sentences


if __name__ == '__main__':
    bulgakov = Book('sentence_extractor/texts/eggs.epub')
    bulgakov.get_text()
