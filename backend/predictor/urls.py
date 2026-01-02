from django.urls import path
from .views import predict_logistic, predict_tree,home

urlpatterns = [
    path("predict/logistic/", predict_logistic),
    path("predict/tree/", predict_tree),
]
