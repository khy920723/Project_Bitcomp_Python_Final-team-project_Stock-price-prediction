from django.shortcuts import render
# from modelpage.models import modelTest

# Create your views here.
import pandas as pd
# from keras.models import load_model
# from eunjeon import Mecab
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
#
#
# tokenizer = Tokenizer()
# mecab = Mecab(dicpath='C:/mecab/mecab-ko-dic')
# stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
# max_len = 13
#
# # 모델 불러오기
# loaded_model = load_model('./model/newsPNclassifier/model_ver1.h5')
#
#
# def run_model(request):
#     # 저장 된 데이터 생성
#     data = modelTest()
#
#     # 긍정 스코어(부정 스코어는 긍정 스코어로 계산)
#     pos_score = 0
#     # 뉴스 기사 갯수
#     i = 0

#     for title in data.TITLE:
#         print(title)
#         sentiment_predict(title, pos_score, i)
#         df_title.append(title)
#
#     return render(request, "result_test.html", context={'pos': pos_score, 'neg': (100-pos_score)})
#
# def sentiment_predict(new_sentence, pos_score, i):
#     new_sentence = mecab.morphs(new_sentence) # mecab 사용, 토큰화
#     new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
#     encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
#     pad_new = pad_sequences(encoded, maxlen = max_len) # 패딩
#     score = float(loaded_model.predict(pad_new)) # 예측
#     pos_score += score
#     i += 1