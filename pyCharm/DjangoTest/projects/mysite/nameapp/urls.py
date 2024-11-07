from django.urls import path

from nameapp import views

app_name = 'nameapp'

urlpatterns = [
    path('chart', views.ChartView.as_view(), name="chart"),
    path('api/predict/', views.KospiPredictAPIView.as_view(), name="predict_kospi_api"),
    path('api/result/', views.ResultAPIView.as_view(), name="result_api"),
    path('chart_main', views.tests.as_view(), name='chart_main'),

    path('chart2', views.ChartView2.as_view(), name="chart2"),
    path('api/predict2/', views.KospiPredict2APIView.as_view(), name="predict_kospi_api2"),
    path('api/result2/', views.ResultAPIView2.as_view(), name="result_api2"),
    path('', views.titletest, name="titletest"),

]

