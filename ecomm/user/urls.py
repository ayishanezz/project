from django.urls import path
from .views import *

urlpatterns = [
    path("home",HomeView.as_view(),name="home"),
    path('prod/<str:cat>',ProductsView.as_view(),name='prod'),
    path('det/<int:pid>',DetailsView.as_view(),name='det'),
    path('acart/<int:pid>',addtocart,name='addcart'),
    path('cart',CartList.as_view(),name='cart'),
    path('delt/<int:cid>',CartDeleteView.as_view(),name='delt'),
    path('arev/<int:pid>',addreview,name='arev'),
    path('porder/<int:id>',Placeorder.as_view(),name='porder'),
    path('order',OrderList.as_view(),name="order"),
    path('corder/<int:id>',Ordercancel.as_view(),name="corder")

]