from django.urls import path
from App_Payment import views

app_name = "App_Payment"

urlpatterns = [
    path('checkout/', views.checkout, name="checkout"),
    path('print-invoice/<order_id>', views.print_invoice, name="print_invoice"),
    path('pay/', views.payment, name="payment"),
    path('status/', views.complete, name="complete"),
    path('purchase/<val_id>/<tran_id>/', views.purchase, name="purchase"),
    path('orders/', views.order_view, name="orders"),
    path('order/<order_id>', views.order_details_view, name="order_details"),
]
