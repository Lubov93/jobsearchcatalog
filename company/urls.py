from django.urls import path
from . import views

app_name = 'company'
urlpatterns = [
    path('', views.get_all_companies, name='get_all_companies'),
    path('<int:id>', views.company_by_id, name='company_by_id'),
]