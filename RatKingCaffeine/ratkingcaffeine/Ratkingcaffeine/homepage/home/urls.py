from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

	path('', views.index,name ='index'),
	path('<int:page>/', views.index,name ='index'),
	path('comments/', views.comments, name='commments'),
	path('login/', auth_views.LoginView.as_view()),
	path('register/', views.register, name = 'register'),
	path('logout/',views.logout_user, name ='logout'),
	path('comment_json/', views.comment_json, name='comment_json'),
	path('customer_service/',views.customer_service , name ='customer_service'),
	path('home/',views.home , name ='home'),
	path('coffee/',views.coffee , name ='coffee'),
	path('Apperal/',views.Apperal , name ='Apperal'),
	path('utilities/',views.utilities , name ='utilities'),
	path('about/',views.about , name ='about'),
	path('profile/',views.profile , name ='profile'),
        path('profile_edit/',views.profile_edit , name ='profile_edit'),
	path("CoffeeDirectory/<str:room_name>/", views.service, name="room"),




]
