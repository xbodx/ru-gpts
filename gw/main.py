import pathlib
import sys

from gw.duration import duration

sys.path.append("gw/")

from datetime import datetime
from generation_wrapper import RuGPT3XL

SENTENCE_INCENTIVE_01 = 'Доброе утро!'
SENTENCE_INCENTIVE_02 = 'Я очень доволен результатом!'
SENTENCE_INCENTIVE_03 = 'Я в восторге от этого фильма!'
SENTENCE_INCENTIVE_04 = 'На празднике было очень весело!'
SENTENCE_INCENTIVE_05 = 'Какой чудесный подарок!'
SENTENCE_INCENTIVE_06 = 'Отличная новость!'
SENTENCE_INCENTIVE_07 = 'Я потрясён произошедшим!'
SENTENCE_INCENTIVE_08 = 'Я в шоке!'
SENTENCE_INCENTIVE_09 = 'Ненавижу это!'
SENTENCE_INCENTIVE_10 = 'Как можно было так поступить?!'
SENTENCE_INCENTIVE_11 = 'Почему я вынужден решать эту проблему один?!'
SENTENCE_INCENTIVE_12 = 'У меня не работает интернет.'
SENTENCE_INCENTIVE_13 = 'Дорогие россияне!'

TEST_QUESTION_01 = 'Где приземлился Гагарин?'
TEST_QUESTION_02 = 'Существует клон Теории Большого Взрыва?'
TEST_QUESTION_03 = 'Главные герои Теории Большого Взрыва?'
TEST_QUESTION_04 = 'Главные героини Теории Большого Взрыва?'
TEST_QUESTION_05 = 'Кто такой Шелдон Купер в Теории Большого Взрыва?'
TEST_QUESTION_06 = 'В каком году смогли заглянуть на обратную сторону Луны?'
TEST_QUESTION_07 = 'Первый человек ступивший на Луну?'
TEST_QUESTION_08 = 'Как зовут сына Дарт Вейдера?'
TEST_QUESTION_09 = 'Где утонул Титаник?'
TEST_QUESTION_10 = 'Сколько зубов у акулы?'
TEST_QUESTION_11 = 'Что думаешь про фильм «птичий короб?»'
TEST_QUESTION_12 = 'Что думаешь о Путине?'
TEST_QUESTION_13 = 'Столица Венесуэлы?'
TEST_QUESTION_14 = 'Кто лучший сноубордист?'
TEST_QUESTION_15 = 'Кто выпускает Жигули?'

path = pathlib.Path().absolute()
print(path)
gpt = RuGPT3XL.from_pretrained(f"../../rugpt3xl", seq_len=512)

def test_qa(question):
    print(f'Я  > {question}')
    answers = gpt.generate(
        question,
        max_length=64,
        no_repeat_ngram_size=3,
        repetition_penalty=2.,
    )
    answer = answers[0]
    bot = answer.find(question)
    if bot > -1:
        ln = len(question)
        answer = answer[bot + ln:].lstrip()
    eot = answer.find('<|endoftext|>')
    if eot > -1:
        answer = answer[:eot].rstrip()
    print(f'Оно> {answer}')
    print(f'-----------------------------------')

def test_list():
    start = datetime.now()
    test_qa(SENTENCE_INCENTIVE_01)
    test_qa(TEST_QUESTION_01)
    test_qa(SENTENCE_INCENTIVE_02)
    test_qa(TEST_QUESTION_03)
    test_qa(SENTENCE_INCENTIVE_03)
    test_qa(TEST_QUESTION_02)
    test_qa(TEST_QUESTION_04)
    test_qa(TEST_QUESTION_05)
    test_qa(SENTENCE_INCENTIVE_04)
    test_qa(TEST_QUESTION_06)
    test_qa(SENTENCE_INCENTIVE_05)
    test_qa(TEST_QUESTION_07)
    test_qa(SENTENCE_INCENTIVE_06)
    test_qa(TEST_QUESTION_08)
    test_qa(SENTENCE_INCENTIVE_07)
    test_qa(TEST_QUESTION_09)
    test_qa(SENTENCE_INCENTIVE_08)
    test_qa(TEST_QUESTION_10)
    test_qa(SENTENCE_INCENTIVE_09)
    test_qa(TEST_QUESTION_11)
    test_qa(SENTENCE_INCENTIVE_10)
    test_qa(TEST_QUESTION_12)
    test_qa(SENTENCE_INCENTIVE_11)
    test_qa(TEST_QUESTION_13)
    test_qa(SENTENCE_INCENTIVE_12)
    test_qa(TEST_QUESTION_14)
    test_qa(SENTENCE_INCENTIVE_13)
    test_qa(TEST_QUESTION_15)
    drtn = datetime.now() - start
    print(f"duration: {duration(drtn)}")

def test():
    start = datetime.now()
    print(f'\n=== Test #1 =======================')
    test_list()
    print(f'\n=== Test #2 =======================')
    test_list()
    print(f'\n=== Test #3 =======================')
    test_list()
    print(f'===================================')
    drtn = datetime.now() - start
    print(f"TOTAL: {duration(drtn)}")

def test2():
    test_qa('test')
    print('\n')
    start = datetime.now()
    test_qa('Вопрос: Сколько будет 15 плюс 15? Ответ: 30.\n'
            'Вопрос: Сколько будет 92 плюс 16? Ответ: 118.\n'
            'Вопрос: Сколько будет 18 плюс 24?')
    test_qa('Вопрос: Сколько будет 15 плюс 15? Ответ: 30.\n'
            'Вопрос: Сколько будет 92 плюс 16?')
    test_qa('Вопрос: Сколько будет 92 плюс 16?')
    test_qa('Сколько будет 92 плюс 16?')
    test_qa('92+16?')
    test_qa('Сколько будет 92+16?')
    print('\n')
    test_qa('Вопрос: красный, оранжевый, какой дальше цвет? Ответ: жёлтый.\n'
            'Вопрос: жёлтый, зелёный, какой дальше цвет? Ответ: голубой.\n'
            'Вопрос: голубой, синий, какой дальше цвет?')
    test_qa('Вопрос: красный, оранжевый, какой дальше цвет? Ответ: жёлтый.\n'
            'Вопрос: жёлтый, зелёный, какой дальше цвет?')
    test_qa('Вопрос: жёлтый, зелёный, какой дальше цвет?')
    test_qa('Жёлтый, зелёный, какой дальше цвет?')
    test_qa('Какие цвета в радуге?')
    print('\n')
    test_qa('Вопрос: после Ельцина бы Путин, кто следующий? Ответ: Медведев.\n'
            'Вопрос: после Путина был Медведев, кто следующий? Ответ: Путин.\n'
            'Вопрос: после Медведева был Путин, кто следующий?')
    test_qa('Вопрос: после Ельцина бы Путин, кто следующий? Ответ: Медведев.\n'
            'Вопрос: после Путина был Медведев, кто следующий?')
    test_qa('после Путина был Медведев, кто следующий?')
    test_qa('Кто следующий после Путина?')
    print('\n')
    test_qa('Какой Павел лучше?')
    test_qa('Какой Алексей лучше?')
    drtn = datetime.now() - start
    print(f"TOTAL: {duration(drtn)}")

if __name__ == "__main__":
    test2()