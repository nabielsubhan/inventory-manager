# Inventory Manager
**Tugas 2 PBP**

**Nama    : Muhammad Nabiel Subhan**<br>
**NPM     : 2206081553**<br>
**Kelas   : PBP A**<br>

Tautan untuk menuju aplikasi Inventory Manager -> [Inventory Manager](https://inventory-manager.adaptable.app/main/)

## Membuat Proyek Django Baru
1. Membuat direktori baru dengan nama `Tugas 2`, lalu membuka *command prompt* pada direktori tersebut.
2. Membuat virtual environment dengan menjalankan perintah `python -m venv env`.
3. Mengaktifkan *virtual environment* dengan menjalankan perintah `env\Scripts\activate.bat`.
4. Membuat file baru dengan nama `requirements.txt` pada direktori yang sama, lalu memasukkan beberapa *dependencies* yang akan digunakan, yaitu:
```txt
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
5. Memasang *dependencies* tersebut dengan menjalankan perintah `pip install -r requirements.txt`.
6. Membuat proyek *Django* baru dengan nama `inventory-manager` menggunakan perintah `django-admin startproject inventory-manager .`.
7. Menambahkan '*' pada 'ALLOWED_HOST' pada file `settings.py` untuk mengizinkan akses ke semua host sehingga aplikasi dapat diakses secara luas.
```python
...
ALLOWED_HOSTS = ["*"]
...
```
8. Menjalankan server *Django* dengan menggunakan perintah `python manage.py runserver` pada *command prompt* dan pergi ke http://localhost:8000 untuk mengecek apakah aplikasi *Django* telah berhasil dibuat yang ditandai dengan adanya animasi roket.
9. Menonaktifkan *virtual environment* setelah aplikasi *Django* berhasil dibuat dengan menjalankan perintah `deactivate`.
10. Menambahkan file `.gitignore` dan mengisinya dengan teks berikut untuk menentukan file dan direktori mana saja yang perlu diabaikan oleh Git.
```txt
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak 

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod] 
*$py.class 

# Distribution / packaging 
.Python build/ 
develop-eggs/ 
dist/ 
downloads/ 
eggs/ 
.eggs/ 
lib/ 
lib64/ 
parts/ 
sdist/ 
var/ 
wheels/ 
*.egg-info/ 
.installed.cfg 
*.egg 
*.manifest 
*.spec 

# Installer logs 
pip-log.txt 
pip-delete-this-directory.txt 

# Unit test / coverage reports 
htmlcov/ 
.tox/ 
.coverage 
.coverage.* 
.cache 
.pytest_cache/ 
nosetests.xml 
coverage.xml 
*.cover 
.hypothesis/ 

# Jupyter Notebook 
.ipynb_checkpoints 

# pyenv 
.python-version 

# celery 
celerybeat-schedule.* 

# SageMath parsed files 
*.sage.py 

# Environments 
.env 
.venv 
env/ 
venv/ 
ENV/ 
env.bak/ 
venv.bak/ 

# mkdocs documentation 
/site 

# mypy 
.mypy_cache/ 

# Sublime Text
*.tmlanguage.cache 
*.tmPreferences.cache 
*.stTheme.cache 
*.sublime-workspace 
*.sublime-project 

# sftp configuration file 
sftp-config.json 

# Package control specific files Package 
Control.last-run 
Control.ca-list 
Control.ca-bundle 
Control.system-ca-bundle 
GitHub.sublime-settings 

# Visual Studio Code
.vscode/* 
!.vscode/settings.json 
!.vscode/tasks.json 
!.vscode/launch.json 
!.vscode/extensions.json 
.history
```

## Membuat aplikasi dengan nama `main` pada proyek `inventory-manager`\
1. Mengaktifkan kembali *virtual environment* dengan menjalankan perintah `env\Scripts\activate.bat`
2. Menjalankan perintah `python manage.py startapp main` untuk membuat aplikasi baru dengan nama `main`.

## Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`
1. Mendaftarkan aplikasi `main` dengan cara pergi ke file `settings.py`, lalu menambahkan `'main'` ke dalam variabel `INSTALLED_APPS`.
```python
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```

## Membuat model pada aplikasi `main`
1. Mengubah isi file `models.py` yang terdapat pada direktori aplikasi `main` untuk membuat model baru dengan nama `Item` yang memiliki atribut:
* `name` sebagai nama item dengan tipe `CharField`.
* `amount` sebagai jumlah item dengan tipe `IntegerField`.
* `description` sebagai deskripsi item dengan tipe `TextField`.
2. Mengisi file `models.py` dengan kode berikut.
```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```
3. Menjalankan perintah `python manage.py makemigrations` untuk membuat file migrasi yang berisi perubahan model basis data, lalu jalankan perintah `python manage.py migrate` untuk memigrasikannya ke dalam basis data lokal. Lakukan langkah ini setiap kali ada perubahan pada model.
 
## Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi, nama dan kelas
1. Membuat direktori baru dengan nama `templates`, lalu membuat file `main.html` di dalam direktori tersebut.
2. Mengisi file `main.html` dengan kode berikut.
```html
<h1>{{ appname }}</h1>

<h5>Name: </h5>
<p>{{ name }}</p> <!-- Ubahlah sesuai dengan nama kamu -->
<h5>Class: </h5>
<p>{{ class }}</p> <!-- Ubahlah sesuai dengan kelas kamu -->
```
3. Setelah itu, membuka file `views.py` di dalam file aplikasi main, lalu menambahkan baris impor `from django.shortcuts import render` untuk mengimpor fungsi render dari modul `django.shortcuts` yang nantinya berfungsi untuk me-render file html yang sudah dibuat.
4. Menambahkan fungsi `show_main` di dalam file `views.py` dengan kode berikut.
```python
def show_main(request):
    context = {
        'appname': 'Inventory Manager',
        'name': 'Muhammad Nabiel Subhan',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
```
Nilai dari variabel yang didefinisikan pada `context` akan muncul pada file html dengan menggunakan sintaks `{{ appname }}`, `{{ name }}`, dan `{{ class }}`.

## Mengonfigurasi *routing* URL
1. Membuat file baru dengan nama `urls.py` di dalam direktori `main` dan mengisinya dengan kode berikut agar aplikasi `main` dapat diakses melalui peramban web.
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
2. Membuka file `urls.py` yang ada di dalam direktori proyek `inventory_manager`, lalu menambahkan baris impor berikut.
```python
...
from django.urls import path, include
...
```
Lalu, tambahkan rute URL `main` ke dalam variabel `urlpatterns` dengan kode berikut.
```python
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```
Dengan begitu, rute URL proyek telah terhubung ke tampilan `main`.

## Melakukan *deployment* ke Adaptable terhadap aplikasi yang sudah dibuat
1. Membuka [GitHub](https://github.com/), lalu buat repositori baru dengan nama `inventory-manager`. Mengatur visibilitas proyek sebagai "Public" dan membiarkan pengaturan lainnya sesuai *default*.
2. Buka command prompt di direktori `Tugas 2`, lalu membuat branch utama baru dengan menjalankan perintah `git branch -M master`, lalu menghubungkannya dengan repositori yang barusan dibuat di github dengan menjalankan perintah `git remote add origin https://github.com/nabielsubhan/inventory-manager.git`.
3. Melakukan *push* ke repositori GitHub dengan menjalankan perintah `git add .`, lalu `git commit -m "Proyek Inventory Manager Tugas 2 PBP"`, dan `git push -u origin master`.
4. Setelah itu, *login* ke [Adaptable.io](https://adaptable.io/).
5. Tekan tombol `New App`, lalu pilih `Connect an Existing Repository`.
6. Hubungkan [Adaptable.io](https://adaptable.io/) dengan GitHub dan pilih `All Repositories` pada proses instalasi.
7. Pilih repositori `inventory-manager` sebagai basis aplikasi yang akan di-*deploy* dan branch yang akan digunakan.
8. Pilih `Python App Template` sebagai template *deployment*.
9. Pilih `PostgreSQL` sebagai tipe basis data yang akan digunakan.
10. Mengganti versi python menjadi `3.11`.
11. Pada bagian `Start Command`, isi dengan `python manage.py migrate && gunicorn inventory_manager.wsgi`.
12. Masukkan `inventory-manager` sebagai nama aplikasi.
13. Centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses *deployment*.

## Mengapa kita menggunakan *Virtual Environment*
Penggunaan *virtual environment* memberikan berbagai manfaat penting, diantaranya adalah terciptanya *environment* yang terpisah untuk setiap proyek yang kita miliki sehingga memungkinkan kita untuk menggunakan versi python, Django, maupun dependensi-dependensi yang berbeda untuk proyek yang berbeda tanpa perlu khawatir akan terjadi konflik. Selain itu, dengan menggunakan *virtual environment* akan membuat lingkungan kerja proyek menajdi lebih bersih dan terorganisir sehingga memudahkan kita untuk mengelola proyek-proyek yang berbeda. *Virtual environment* juga dapat memudahkan ketika melakukan pengerjaan suatu proyek dengan sebuah tim karena setiap anggota dapat memiliki lingkungan virtual masing-masing dengan dependensi yang mereka butuhkan.

## Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*?


   
