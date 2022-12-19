
from django.urls import path
from .views import CreateUser, CreateUserWithList, LoginView, LogoutView, UserInfo
from rest_framework.authtoken.views import obtain_auth_token 

# router = routers.SimpleRouter()
# router.register(r'', UserViewSet)


## test ##
urlpatterns = [
    path('', CreateUser.as_view(), name='User'),
    path('createWithList/', CreateUserWithList.as_view(), name='UserList'),
    path('login/', LoginView.as_view(), name='Login'),
    path('username/<str:username>/', UserInfo.as_view(), name='User'),
    path('logout/', LogoutView.as_view(), name='Logout'),
]
