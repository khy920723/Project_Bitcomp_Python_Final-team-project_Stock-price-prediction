from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.utils import timezone
import os, glob
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from keras.models import load_model
from static import imform

img_w = 64
img_h = 64
model = load_model('./model/multi_img_classification.model')
from modelpage.models import mage
def sample(request):

    context = {

    }
    return render(request, 'sample_img.html', context=context)

def photo(request):
    if(request.method == 'POST'):
        post = mage()
        # post.title = request.POST['title']
        X = []
        for img in request.FILES.getlist('imgs'):
            img = Image.open(img)
            img = img.convert("RGB")
            img = img.resize((img_w, img_h))
            data = np.asarray(img)
            X.append(data)
        X = np.array(X)
        prediction = model.predict(X)
        np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
        cnt = 0

        for i in prediction:
            pre_ans = i.argmax()  # 예측 레이블
            print(i)
            print(pre_ans)
            pre_ans_str = ''
            print(pre_ans)
            B = ''
            C = ''
            A = ''
            title = ''

            if pre_ans == 0:
                pre_ans_str = "CorprinusComatus"
                B = "/static/mush_img/Corprinus.jpg"
                C = imform.corp
                A = imform.C
                title = imform.CTitle
            elif pre_ans == 2:
                pre_ans_str = "Morel"
                B = "/static/mush_img/Morel.jpg"
                C = imform.more
                A = imform.M
                title = imform.MTitle
            elif pre_ans == 1:
                pre_ans_str = "LingzhiMushroom"
                B = "/static/mush_img/LingzhiMushroom.jpg"
                C = imform.ling
                A = imform.L
                title = imform.LTitle
            elif pre_ans == 3:
                pre_ans_str = "OysterMushroom"
                B = "/static/mush_img/OysterMushroom.jpg"
                C = imform.oys
                A = imform.O
                title = imform.OTitle
            elif pre_ans == 4:
                pre_ans_str = "PineMushroom"
                B = "/static/mush_img/PineMushroom.jpg"
                C = imform.pine
                A = imform.P
                title = imform.PTitle
            elif pre_ans == 5:
                pre_ans_str = "Polyozellus"
                B = "/static/mush_img/Polyozellus.jpg"
                C = imform.poly
                A = imform.PL
                title = imform.PTitlee
            elif pre_ans == 6:
                pre_ans_str = "SarcodonAspratus"
                B = "/static/mush_img/SarcodonAspratus.jpg"
                C = imform.sar
                A = imform.S
                title = imform.Stitle
            elif pre_ans == 7:
                pre_ans_str = "TrenellaFuciformis"
                B = "/static/mush_img/TrenellaFuciformis.jpg"
                C = imform.tren
                A = imform.T
                title = imform.TTitle




            return render(request, "sample_detail.html",context= {'mush':pre_ans_str,
                                                              'ti':title, 'imim': B, 'txt':C, 'A': A})










# def result(req):
#     context = {
#
#     }
#     return render(req, 'modelspage/detail.html', context=context)
