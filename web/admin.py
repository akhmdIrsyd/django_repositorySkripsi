from django.contrib import admin
from .models import mahasiswa,dosen,User,jurusan,fakultas
# Register your models here.

admin.site.register(User)
admin.site.register(mahasiswa)

admin.site.register(dosen)
admin.site.register(jurusan)
admin.site.register(fakultas)
