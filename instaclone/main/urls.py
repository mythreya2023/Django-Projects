from django.urls import path
from main import views

urlpatterns = [
    path("login",views.loginView,name="loginPage"),
    path("register",views.registerView,name="registerPage"),
    path("logout",views.logoutView,name="logoutPage"),
    path("profile",views.profileView,name="profilePage"),
    path("post",views.postView,name="postPage"),
    path("update/<int:pid>",views.updatePost,name="updatePost"),
    path("delete/<int:pid>",views.delPost,name="delPost"),
    path("",views.homeView,name="homePage"),
]