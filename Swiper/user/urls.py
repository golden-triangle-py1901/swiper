from django.urls import path

from user import apis

urlpatterns = [
    path('verify_phoneNum/',apis.verify_phoneNum),
    path('login/',apis.login),
    path('get_profile/',apis.get_profile),
    path('set_profile/',apis.set_profile)

]