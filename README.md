# django_repositorySkripsi
spesifikasi
Django
Postgresql

Cara install
1. install python 3.8
2. buka cmd
3. arahkan ke folder web
4. install requirment: pip install -r requirments.txt
5. migrate database:
   pyhon manage.py migrate
6. buat superuser:
   python manage.py createsuperuser
7. jalankan web:
   python manage.py runserver

ganti database ke mysql:
1. pip install folder/mysqlclient-1.4.6-cp38-cp38-win_amd64.whl
2. buat database
3. buka repasitory_fhut/setting.py 
4. ganti setting database
DATABASES = {
   'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'nama_database',
      'USER': 'root',
      'PASSWORD': '',
      'HOST': 'localhost',
      'PORT': '3306',
   }
}
5. ulangi tahan cara install dari point 5
