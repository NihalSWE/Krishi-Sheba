from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('profile/',views.ProfileView.as_view(),name='profile'),
 
    path('register/',views.RegistrationView.as_view(),name='register'),

    path('login/',auth_views.LoginView.as_view(template_name='Accounts/login.html',authentication_form=LoginForm),name='login'),

    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),

    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='Accounts/change_pass.html', form_class=MyPasswordChangeForm, success_url='/changepassword_done/'),name='change_password'),

    path('changepassword_done/', auth_views.PasswordChangeDoneView.as_view(template_name='Accounts/changepass_done.html'),name='changepassword_done'),

   
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='Accounts/resetpass.html', form_class=MyPasswordResetForm),name='reset_password'),


    path('reset_password/done/',auth_views.PasswordResetDoneView.as_view(template_name='Accounts/resetpassdone.html'),name='reset_pass_done'),

    path('reset_password-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='Accounts/resetpassconfirm.html',form_class=MySetPasswordForm),name='reset_pass_confirm'),


    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='Accounts/resetpasscomplete.html'),name='changepassword_complete'),


    path('address/',views.Address,name='address'),


  
]
