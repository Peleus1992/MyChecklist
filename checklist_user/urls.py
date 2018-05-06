from django.conf.urls import url

from . import views

urlpatterns = [
    url('signup', views.signup_view),
    url('login', views.login_view),
    url('logout', views.logout_view),
]