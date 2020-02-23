
from django.urls import path
from pharma import views

urlpatterns = [
   path(r'', views.pharma_view),
   path(r'pharma_website.html', views.pharma_view),
]
