
from django.conf.urls import url
from django.contrib import admin
import chat.views as HOME

urlpatterns = [
    url(r'^', HOME.home),
    url(r'^add_player/', HOME.add_player),
]
