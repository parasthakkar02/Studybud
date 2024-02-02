from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),
    # main urls
    path("", views.home, name="home"),
    path("room/<str:pk>/", views.room, name="room"),
    # CRUD
    path("create_room/", views.createRoom, name="create_room"),
    path("update_room/<str:pk>/", views.updateRoom, name="update_room"),
    path("delete_room/<str:pk>/", views.deleteRoom, name="delete_room"),
]
