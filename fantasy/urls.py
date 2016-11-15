
from django.conf.urls import url
from django.contrib import admin
import chat.views as HOME

urlpatterns = [
    url(r'^add_player/', HOME.add_player),
    url(r'^', HOME.home),
    url(r'^test/', HOME.testview),
]
