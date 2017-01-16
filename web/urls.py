from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.UserLoginView.as_view(), name='login'),
    url(r'^register/$', views.UserRegisterView.as_view(), name='register'),

    url(r'^logout/$', views._logout, name='logout'),

    url(r'^termin/(?P<termin_id>\d+)/', views.hala_termin, name='hala_termin'),
    url(r'^terminy/', views.hala_terminy, name='hala_terminy'),

    url(r'^hala/$', views.hala, name='hala'),
    url(r'^hala/termin/(?P<termin_id>\d+)/', views.hala_termin, name='hala_termin'),
    url(r'^hala/terminy/', views.hala_terminy, name='hala_terminy'),

    url(r'^posilnovna/$', views.posilnovna, name='posilnovna'),
    url(r'^posilnovna/termin/(?P<termin_id>\d+)/', views.posilnovna_termin, name='posilnovna_termin'),
    url(r'^posilnovna/terminy/', views.posilnovna_terminy, name='posilnovna_terminy'),

    url(r'^stena/$', views.stena, name='stena'),
    url(r'^stena/termin/(?P<termin_id>\d+)/', views.stena_termin, name='stena_termin'),
    url(r'^stena/terminy/', views.stena_terminy, name='stena_terminy'),

    url(r'^sauna/$', views.sauna, name='sauna'),
    url(r'^sauna/termin/(?P<termin_id>\d+)/', views.sauna_termin, name='sauna_termin'),
    url(r'^sauna/terminy/', views.sauna_terminy, name='sauna_terminy'),

]

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
