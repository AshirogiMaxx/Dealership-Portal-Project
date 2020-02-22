from django.urls import path, re_path
#from Vehicle_Inventory import views
from .views import *

urlpatterns = [
    path('portal/vehicles', ListCarView.as_view(), name='Cars'),
    path('', hello_world, name='hello_world')
]
