# тут пишем
import spacy
from spacy.lang.ru import Russian
import textract
import os
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
from src.text_reading import Book
from src.sentences import SentenceSyntax


class Extractor:
    def __init__(self, path_to_book, nom=0, gen=0, voc=0,
                 impers=0, defpers=0, vagpers=0, infinit=0):
        self.book = Book(path_to_book)
        self._sentences = self.book.get_sentence()

    def find_sentences(self):
        nominatives = []
        genitives = []
        vocatives = []
        impers


