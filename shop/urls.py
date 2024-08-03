from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.reg,name='Register'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:name>',views.collectionsview,name='collections'),
    path('collections/<str:cname>/<str:pname>',views.product_details,name='product_details'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('addtocart',views.add_to_cart,name='addtocart'),
    path('Cart',views.Cart,name='Cart'),
    path('remove_cart/<str:cid>',views.remove_cart,name='remove_cart'),
    path('fav',views.fav_page,name='fav'),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    # path('payment/<str:pname>/',views.payment_page,name="payment"),
    path('payment/<str:pname>',views.payment_view_page,name="payment"),
    path('address/<str:pname>',views.shipping_address_view, name='address'),
    path('Editaddress/<str:pname>',views.edit_address, name='Editaddress'),
    path('cart_to_payment',views.cart_to_payment,name='cart_to_payment'),
    path('proceed_to_pay',views.proceed_to_pay,name='proceed_to_pay'),
    path('proceed_to_pay2',views.proceed_to_pay2,name='proceed_to_pay2'),
    path('order_page',views.order_page,name='order_page'),
    path('order_page_view',views.order_page_view,name='order_page_view'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]