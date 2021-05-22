from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('lang/', views.lang_view, name = 'language'),
    path('chat/', views.chat_view, name='chat-home'),
    path('chathome/', views.index_view, name='index'),
    path('', views.home_view, name = 'user-home'),
    path('register/', views.reg_view, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('sent/', views.activation_sent_view, name="activation_sent"),
    # path('webhook/', views.webhook, name='webhook'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
