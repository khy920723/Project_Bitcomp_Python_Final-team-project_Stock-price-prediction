from django.shortcuts import render, HttpResponse

import json
import csv


# Create your views here.

def data_json(request):
    f = open('samsung.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    data = list(data)
    date = list()
    for i in range(1, len(data) - 1):
        date.append(data[i][0])
    op = list()
    for i in range(0, len(data) - 1):
        op.append(data[i][1])
    high = list()
    for i in range(0, len(data)):
        high.append(data[i][2])
    low = list()
    for i in range(0, len(data)):
        low.append(data[i][3])
    close = list()
    for i in range(0, len(data)):
        close.append(data[i][4])
    volume = list()
    for i in range(0, len(data)):
        volume.append(data[i][5])

    data = {'columns': [date, op, high, low, close]}
    f.close()
    return HttpResponse(json.dumps(data), content_type='text/json')


def main_page(request):
    return render(request, 'main_page.html')


def data2_json(request):
    f = open('samsung.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    data = list(data)
    date = list()
    for i in range(1, len(data) - 1):
        date.append(data[i][0])
    volume = list()
    for i in range(0, len(data)):
        volume.append(data[i][5])

    data = {'columns': [date, volume]}
    f.close()
    return HttpResponse(json.dumps(data), content_type='text/json')


def main_page2(request):
    return render(request, 'main_page2.html')

def data3_json(request):
    f = open('fourCo.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    data = list(data)
    date = list()
    for i in range(1, len(data) - 1):
        date.append(data[i][0])
    Sam = list()
    for i in range(0, len(data) - 1):
        Sam.append(data[i][1])
    LG = list()
    for i in range(0, len(data)):
        LG.append(data[i][2])
    KT = list()
    for i in range(0, len(data)):
        KT.append(data[i][3])
    CJ = list()
    for i in range(0, len(data)):
        CJ.append(data[i][4])

    data = {'columns': [date, Sam, LG, KT, CJ]}
    f.close()
    return HttpResponse(json.dumps(data), content_type='text/json')

def main_page3(request):
    return render(request, 'main_page3.html')

