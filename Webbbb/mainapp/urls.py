from django.contrib import admin
from django.urls import path, include
from mainapp import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Admin URL
    path('superadmin/', admin.site.urls),

    # Genel URL
    path('', views.home, name='home'),

    # Vatandaş URL'leri
    path('admin/', views.vatandas_login, name='yonetici_login'),

    path('vatandas/', views.vatandas_login, name='vatandas_login'),
    path('vatandas/kayit', views.vatandas_register, name='vatandas_register'),
    path('vatandas/home/', views.vatandas_home, name='vatandas_home'),
    path('vatandas/logout/', views.vatandas_logout, name='vatandas_logout'),
    path('vatandas/randevu_al/', views.randevu_al, name='randevu_al'),
    path('vatandas/chatbox/', views.vatandas_chatbox, name='vatandas_chatbox'),

    # Chatbox URL'leri
    path('chatbox/chat/', views.chat_with_gemini, name='chat_with_gemini'),

    # Yetkili URL'leri
    path('yetkili/giris', views.yetkili_login, name='yetkili_login'),
    path('yetkili/home/', views.yetkili_home, name='yetkili_home'),
    path('yetkili/edit_authority/', views.admin_edit_authority, name='admin_edit_authority'),
    path('yetkili/search_authorities/', views.search_authorities, name='search_authorities'),
    path('yetkili/edit_citizen/', views.admin_edit_citizen, name='admin_edit_citizen'),
    path('yetkili/randevular/', views.randevular, name='yetkili_randevular'),
    path('yetkili/edit_citizen/<int:id>/', views.edit_citizen_detail, name='edit_citizen_detail'),
    path('yetkili/delete_citizen/<int:id>/', views.delete_citizen, name='delete_citizen'),


    # Randevu URL'leri
    path('randevu/<int:randevu_id>/', views.randevu_detay, name='randevu_detay'),
    path('randevu/<int:randevu_id>/delete/', views.delete_randevu, name='delete_randevu'),
    path('search_randevular/', views.search_randevular, name='search_randevular'),

    # JWT Token URL'leri
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Allauth URL'leri
    path('accounts/', include('allauth.urls')),
]
