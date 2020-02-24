from django.urls import path, re_path, include
#from Vehicle_Inventory import views
from .views import *

urlpatterns = [
    path('portal/vehicles', ListCarView.as_view(), name='Cars'),
    path('', add_car, name='add_new_car'),
    path('car/<int:pk>/', car_details),
    path('accounts/', include('django.contrib.auth.urls')),
]
