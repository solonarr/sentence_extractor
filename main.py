# тут пишем вызов функций
# ну типа путь до книжки потом вызываем экстрактор

from src.extractor import Extractor

if __name__ == '__main__':
    path_to_olesya = './texts/olesya.epub'
    path_to_test = './texts/test.txt'

    extracting = Extractor(path_to_test, nom=1, gen=1, voc=1, impers=1, defpers=0, vagpers=0, infinit=0)
    sentences = extracting.get_searched_sentences()
    for key, value in sentences.items():
        print(key, value)
