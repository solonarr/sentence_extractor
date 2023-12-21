"""
Reading texts from epub.
We should think about reading texts
of different types.
PDF and docx in process
"""
import ebooklib
import os
from ebooklib import epub


class Book:
    def __init__(self, path):
        self.path = path
        self._text = self.read_text(self.path)

    def read_text(self, path):
        """
        Get string from path
        :param path: path to file
        :return: str with text from path
        """
        ext = os.path.splitext(path)[-1]
        if ext == '.epub':
            return self.extract_epub(path)
        elif ext == '.txt':
            return self.extract_txt(path)

    @staticmethod
    def extract_epub(path):
        """
        Get string from epub file
        :param path: path to epub file
        :return: str from epub file
        """
        text = epub.read_epub(path)
        return text

    @staticmethod
    def extract_txt(path):
        """
        Get string from txt file
        :param path: path to txt file
        :return: str from txt file
        """
        with open(path) as f:
            text = f.read()
        return text

    def get_text(self):
        return self._text


if __name__ == '__main__':
    bulgakov = Book('sentence_extractor/texts/eggs.epub')
    bulgakov.get_text()
