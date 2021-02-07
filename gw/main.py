import pathlib
import sys
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
    answer = gpt.generate(
        question,
        max_length=50,
        no_repeat_ngram_size=3,
        repetition_penalty=2.,
    )
    print(f'Оно> {answer}')
    print(f'-----------------------------------')

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
print(f'-----------------------------------')
duration = datetime.now() - start
print(f"duration: {duration}")