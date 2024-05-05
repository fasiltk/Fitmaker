from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('registers/', registers, name='registers'),
    path('inputpage/', inputpage, name='inputpage'),  # Wrap the view with login_required
    path('outputpage/', outputpage, name='outputpage'),
    path('change_password/',change_password,name='change_password'),
    path('logout/', logout_view, name='logout'),
    path('diseases/',diseases,name='diseases'),
    path('Diabetes/',Diabetes,name='Diabetes'),
    path('Cholesterol/',Cholesterol,name='Cholesterol'),
    path('BloodPressure/',BloodPressure,name='BloodPressure'),
    path('patients/',patients,name='patients'),
    path('heart/',heart,name='heart'),
    path('disc/',disc,name='disc'),
    path('kidney/',kidney,name='kidney'),
    path('backbone/',backbone,name='backbone'),
    path('demo/',demo,name='demo'),
]
