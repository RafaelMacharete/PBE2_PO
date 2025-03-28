from django.urls import path
from . import views

urlpatterns = [
    path("login/", view=views.login, name='login/'),
    path("account/", view=views.get_all_accounts, name='get_all_accounts'), 
    path('account/create/', view=views.create_account, name='create_account'),
    path('account/edit/<int:pk>', view=views.alter_account_state, name='alter_account_state'),
    path("account/delete/<int:pk>", view=views.alter_account_state, name='alter_account_state'),
]
