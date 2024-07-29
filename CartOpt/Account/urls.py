from django.urls import path
from .views import *

app_name = 'Account'
urlpatterns = [
    path('login', LoginHandler.as_view(), name='login'),
    path('reg', RegisterHandler.as_view(), name='reg'),
    path('change', ChangeAccountInfo.as_view(), name='change'),
    path('logout', logout_handler, name='logout')
]