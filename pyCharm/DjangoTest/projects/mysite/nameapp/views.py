from nameapp.models import KospiPredict
from nameapp.models import KospiPredict2
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View
from django.shortcuts import render
from time import mktime, strptime

class ResultAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        data = request.session.get('result')
        return Response(data)


class KospiPredictAPIView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        stocks = KospiPredict.objects.all().order_by('date')

        close_list = []
        open_list = []
        for stock in stocks:
            time_tuple = strptime(str(stock.date), '%Y-%m-%d %H:%M:%S')
            utc_now = mktime(time_tuple) * 1000
            close_list.append([utc_now, stock.close])
            open_list.append([utc_now, stock.open])

        data = {
            'close': close_list,
            'open': open_list
        }

        return Response(data)

class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'nameapp/chart.html')

class tests(View):
    def main_tests(request):
        return render(request, 'nameapp/maintest.html')


class ResultAPIView2(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        data2 = request.session.get('result2')
        return Response(data2)


class KospiPredict2APIView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        stocks = KospiPredict2.objects.all().order_by('date')

        close_list = []
        open_list = []
        for stock in stocks:
            time_tuple = strptime(str(stock.date), '%Y-%m-%d')
            utc_now = mktime(time_tuple) * 1000
            close_list.append([utc_now, stock.close])
            open_list.append([utc_now, stock.open])

        data2 = {
            'close': close_list,
            'open': open_list
        }

        return Response(data2)

class ChartView2(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'nameapp/chart2.html')

def titletest(request):
    return render(request, 'nameapp/title.html')


