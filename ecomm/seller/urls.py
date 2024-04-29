from .views import *
from rest_framework.routers import DefaultRouter

r=DefaultRouter()
r.register('pro',ProductModelViewSet,basename='pro')
r.register('order',OrderModelViewSet,basename='order')

urlpatterns=[]+r.urls
