from django.urls import path, include
from .views import home, vehicles, vehicle, detail, VehiculoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('vehicles', VehiculoViewset)

urlpatterns = [
    path('', home, name="home"),
    path('vehicles', vehicles, name="vehicles"),
    path('vehicle', vehicle, name="vehicle"),
    path('detail/<id>', detail, name="detail"),
    path('api/', include(router.urls))
]