from django.urls import path
from . import views

app_name = "storeapp"

urlpatterns = [
    path("", views.mainpage, name="mainpage"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    #path("addtweet/", views.addtweet, name="addtweet"),
    #path("listtweet/", views.listtweet, name="listtweet section"),
    #path("addtweetbyform/", views.addtweet_byform, name="addtweetbyform"),
    #path("addtweetbymodelform/", views.addtweet_bymodelform, name="addtweetbymodelform"),
    path("men/", views.men, name="men"),
    path("women/", views.women, name="women"),
    path("orders/", views.orders, name="orders"),
]