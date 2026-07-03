from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as django_auth_views
from accounts import views as auth_views
from results import views as result_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.login_view),
    path('login/', auth_views.login_view),
    path('register/', auth_views.register_view),
    path('logout/', auth_views.logout_view),
    path('dashboard/', result_views.dashboard_view),
    path('marks/', result_views.marks_view),
    path('cgpa/', result_views.cgpa_view),

    # Password Reset URLs
    path('password-reset/',
        django_auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html'
        ),
        name='password_reset'),

    path('password-reset/done/',
        django_auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
        ),
        name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
        django_auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html'
        ),
        name='password_reset_confirm'),

    path('password-reset-complete/',
        django_auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
        ),
        name='password_reset_complete'),
]