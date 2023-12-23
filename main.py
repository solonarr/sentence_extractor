# тут пишем вызов функций
# ну типа путь до книжки потом вызываем экстрактор

from src.extractor import Extractor

if __name__ == '__main__':
    path_to_olesya = './texts/olesya.epub'
    path_to_test = './texts/test.txt'

    extracting = Extractor(path_to_test, nom=3, gen=2)
    sentences = extracting.get_searched_sentences()
    print(sentences)
    for key, value in sentences.items():
        print(key, value)
