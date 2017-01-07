from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [

    url(r'^domov/', include('web.urls'), name='domov'),

    # admin section
    url(r'^admin/', admin.site.urls),

]
