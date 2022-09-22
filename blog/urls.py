from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import Login

app_name = 'GunBlog'

urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    path('guns_list/create', views.UserCreate.as_view(), name='create'),
    path('guns_list/create/wrong_password', views.WrongPassword.as_view(), name='wrong_password'),
    path('guns_list/', login_required(views.GunsList.as_view()), name = 'guns_list'),
    path('guns_list/gun_create/', login_required(views.GunsCreate.as_view()), name = 'gun_create'), 
    path('guns_list/<str:slug>/', login_required(views.GunsDetailView.as_view()), name = 'gun_details'),
    path('guns_list/<str:slug>/comment/', login_required(views.CommentCreate.as_view()), name = 'gun_comment'),
    path('guns_list/<str:slug>/update/', login_required(views.GunUpdate.as_view()), name = 'gun_update'),
    path('guns_list/<str:slug>/delete/', login_required(views.GunDelete.as_view()), name = 'gun_delete'),
    path('login/', views.LoginView.as_view(template_name='registration/login.html', authentication_form=Login), name='login'), 
    path('logout/', login_required(views.LogOut.as_view(next_page=settings.LOGOUT_REDIRECT_URL)), name='logout'), 
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)