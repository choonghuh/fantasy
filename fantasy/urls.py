
from django.conf.urls import url
from django.contrib import admin
import chat.views as HOME

urlpatterns = [
    url(r'^$', HOME.home),
    url(r'^admin/', admin.site.urls),
    url(r'^add_player/', HOME.add_player), 
    url(r'^test/', HOME.testview),
]
