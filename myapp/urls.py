from django.urls import path
from .views import (HomeView,DashboardView,CarView,BusView,TrainView,FlightView,BookingView,
SigninView,RegisterView,logoutView,ProfileView,ChangePassView,SlipView)
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate,login
from .form import PassResetForm,SetNewPassForm


urlpatterns = [

    # home
    path('home/', HomeView, name='home'),

    # Dashboard
    path('dashboard/', DashboardView, name='dashboard'),


    # # Booking
    path('booking/<int:id>/', BookingView, name='booking'),

    # # Print Ticket
    path('slip/<int:id>/', SlipView, name='slip'),

    # # Category
    path('car/', CarView, name='car'),
    path('bus/', BusView, name='bus'),
    path('train/', TrainView, name='train'),
    path('flight/', FlightView, name='flight'),

    # # Auth
    path('signin/', SigninView, name='signin'),
    path('register/', RegisterView, name='register'),
    path('logout/', logoutView, name='logout'),
    path('profile/', ProfileView, name='profile'),
    path('changepass/', ChangePassView, name='changepass'),

    #Password Reset
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=PassResetForm), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=SetNewPassForm), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),

]
