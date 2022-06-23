from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_user/', views.create_user, name='create_user'),
    path('login_view/', views.login_view, name="login_view"),
    path('logout_view/', views.logout_view, name="logout_view"),
    path('gettoken/',obtain_auth_token),

    path('read_json_data/', views.read_json_data, name='read_json_data'),
    path('create_db/', views.create_db, name="create_db"),







]