from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('contact/', views.contact, name='contact'),
    path('login/',views.login_,name='login'),
    path('admin/',views.admin,name='admin'),
    path('product_desc/<int:p_id>',views.product_desc,name='desc'),
    path('profile/',views.profile,name='profile'),
    path('cart/',views.cart, name='cart'),
    path('addtocart/<int:id>',views.addtocart,name='addtocart'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('search/', views.search_results, name='search_results'),
    path('checkout/',views.checkout,name='checkout'),
    
  
]
