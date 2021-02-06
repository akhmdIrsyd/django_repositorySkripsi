from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('dashboard', views.index, name='index'),
    path('akun/', views.list_akun, name='akun'),
    path('signupadmin/', views.SignUpView.as_view(), name='signupadmin'),
    path('signupDosen/', views.SignUpView.as_view(), name='signup_dosen'),
    path('updateAkun/<int:pk>', views.akunUpdateView.as_view(), name='update_akun'),
    path('deleteAkun/<int:pk>', views.akunDeleteView.as_view(), name='delete_akun'),
    path('mahasiswa/', views.list_mahasiswa, name='mahasiswa'),
    path('createMHS/', views.MHSCreateView.as_view(), name='create_mhs'),
    path('updateMHS/<int:pk>', views.MHSUpdateView.as_view(), name='update_mhs'),
    path('deleteMHS/<int:pk>', views.MHSDeleteView.as_view(), name='delete_mhs'),
    path('dosen/', views.list_dosen, name='dosen'),
    path('createDosen/', views.DosenCreateView.as_view(), name='create_dosen'),
    path('updateDosen/<int:pk>', views.DosenUpdateView.as_view(), name='update_dosen'),
    path('deleteDosen/<int:pk>', views.DosenDeleteView.as_view(), name='delete_dosen'),
    path('skripsi', views.detail_skripsi, name='skripsi'),
    path('skripsi_dosen', views.list_skripsiDosen, name='skripsi_dosen'),
    path('data_dosen', views.detail_dataDosen, name='data_dosen'),
    path('skripsi_dosen', views.list_skripsiDosen, name='skripsi_dosen'),
    path('data_mahasiswa', views.detail_dataMHS, name='data_mahasiswa'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
