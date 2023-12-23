# тут пишем вызов функций
# ну типа путь до книжки потом вызываем экстрактор

from src.extractor import Extractor

if __name__ == '__main__':
    path_to_olesya = './texts/olesya.epub'
    path_to_test = './texts/test.txt'
    path_to_test_2 = './texts/test2.txt'

    extracting = Extractor(path_to_test, nom=2, gen=2, impers=2,
                           defpers=2, vagpers=2, infinit=2)
    sentences = extracting.get_searched_sentences()
    print(sentences)
    for key, value in sentences.items():
        print(key, value)
