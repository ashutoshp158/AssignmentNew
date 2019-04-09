from django.conf.urls import url

from views import FibonacciAPIView


urlpatterns = [

    url(r'^', FibonacciAPIView.as_view()),
]