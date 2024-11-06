from django.urls import path
from ProductItem import views
urlpatterns = [
    path('seeding_Item/', views.ProductView.as_view(), name='seeding_Item'), 

    path('product_detail/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),

    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),

    path('cart/',views.show_cart,name='showcart'),

    path('plus_cart/',views.plus_cart,name='plus_cart'),

    path('minus_cart/',views.minus_cart,name='minus_cart'),
    
    path('remove_cart/',views.remove_cart,name='remove_cart'),

    path('checkout/', views.checkout, name='checkout'),

    path('paymentdone/', views.paymentdone, name='paymentdone'),

    path('orders/', views.orders, name='orders'),

    path('machinery/',views.MachineryView.as_view(),name='machinery'),

    path('machinery-detail/<int:pk>',views.MachineryDetailView.as_view(),name='machinery-detail'),

    path('machinery_contact/',views.machinery_contact,name='machinery_contact'),

    path('rent/',views.rent,name='rent'),

    path('search/',views.search,name='search'),

    path('information/',views.information,name='information'),


]
