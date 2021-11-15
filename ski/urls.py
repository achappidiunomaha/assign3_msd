from django.urls import path, include
from .views import client, employee, ski
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', ski.home, name='home'),
                  path('signup/', client.ClientSignUpView.as_view(), name='signup'),
                  path('accounts/password_reset/',
                       auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
                       name='password_reset'),
                  path('accounts/password_reset/done/',
                       auth_views.PasswordResetDoneView.as_view(template_name="registration/reset_email_sent.html"),
                       name='reset_email_sent'),
                  path('accounts/reset/<uidb64>/<token>/',
                       auth_views.PasswordResetConfirmView.as_view(template_name="registration/reset_confirm.html"),
                       name='reset_confirm'),
                  path('accounts/reset/done/',
                       auth_views.PasswordResetCompleteView.as_view(template_name="registration/reset_complete.html"),
                       name='reset_complete'),
                  path('Client/', include(([
                                               path('', client.client_home.as_view(), name='client_home'),
                                               path('account', client.client_details, name='client_details'),
                                               path('account/edit/', client.client_edit, name='client_edit'),
                                               path('password_change/',
                                                    auth_views.PasswordChangeView.as_view(
                                                        template_name="registration/password_change.html"),
                                                    name='password_change'),
                                               path('password_change/done/',
                                                    auth_views.PasswordChangeDoneView.as_view(
                                                        template_name="registration/password_change_done.html"),
                                                    name='password_changed'),
                                               path('equipment/', client.equipmentall, name='equipment'),
                                               path('equipment/<int:id>/', client.equipmentdetail,
                                                    name='equipment_detail'),
                                               path('equipment/<int:id>/checkout/', client.order_checkout,
                                                    name='checkout'),
                                               path('orders', client.orders, name='orders'),
                                               path('orders_pending', client.orders_pending, name='orders_pending'),
                                               path('orders/<int:id>/delete/', client.orders_delete, name='orders_delete'),
                                               path('orders_pending/<int:id>/delete/', client.orders_pending_delete, name='pending_delete'),
                                           ], 'ski'), namespace='client')),
                  path('Employee/', include(([
                                                 path('', employee.employee_home.as_view(), name='employee_home'),
                                                 path('orders_pending', employee.order_list, name='orders_pending'),
                                                 path('orders_pending/<int:id>/approved', employee.order_approve,
                                                      name='order_approve'),
                                                 path('orders_pending/<int:id>/declined', employee.order_declined,
                                                      name='order_declined'),
                                                 path('orders_processed', employee.order_processed, name='order_processed'),
                                                 path('orders_pending/<int:id>/delete/', employee.orders_pending_delete,
                                                      name='pending_delete'),
                                                 path('orders_processed/<int:id>/delete/', employee.orders_delete,
                                                      name='orders_delete'),
                                             ], 'ski'), namespace='employee')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
