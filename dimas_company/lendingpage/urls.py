from django.urls import path, include
from . import views
from django.views.generic import TemplateView

app_name = 'lending_page'

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'redoc/',
        TemplateView.as_view(template_name='lendingpage/index1.html'),
        name='redoc'
    ),
]