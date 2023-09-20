# Inventory Manager
**Tugas 2 PBP**

**Nama    : Muhammad Nabiel Subhan**<br>
**NPM     : 2206081553**<br>
**Kelas   : PBP A**<br>

Tautan untuk menuju aplikasi Inventory Manager -> [Inventory Manager](https://inventory-manager.adaptable.app/main/)

# Tugas 2: Implementasi Model-View-Template (MVT) pada Django
## Membuat Proyek Django Baru
1. Membuat direktori baru dengan nama `Tugas 2`, lalu membuka *command prompt* pada direktori tersebut.
2. Membuat *virtual environment* dengan menjalankan perintah `python -m venv env`.
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
6. Membuat proyek Django baru dengan nama `inventory-manager` menggunakan perintah `django-admin startproject inventory-manager .`.
7. Menambahkan `*` pada `ALLOWED_HOST` pada file `settings.py` untuk mengizinkan akses ke semua host sehingga aplikasi dapat diakses secara luas.
```python
...
ALLOWED_HOSTS = ["*"]
...
```
8. Menjalankan server Django dengan menggunakan perintah `python manage.py runserver` pada *command prompt* dan pergi ke http://localhost:8000 untuk mengecek apakah aplikasi Django telah berhasil dibuat yang ditandai dengan adanya animasi roket.
9. Menonaktifkan *virtual environment* setelah aplikasi Django berhasil dibuat dengan menjalankan perintah `deactivate`.
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

## Membuat aplikasi dengan nama `main` pada proyek `inventory-manager`
1. Mengaktifkan kembali *virtual environment* dengan menjalankan perintah `env\Scripts\activate.bat`.
2. Menjalankan perintah `python manage.py startapp main` untuk membuat aplikasi baru dengan nama `main`.
3. Mendaftarkan aplikasi `main` dengan cara pergi ke file `settings.py`, lalu menambahkan `'main'` ke dalam variabel `INSTALLED_APPS`.
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
 
## Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template  yang menampilkan nama aplikasi, nama, dan kelas
1. Membuat direktori baru dengan nama `templates`, lalu membuat file `main.html` di dalam direktori tersebut.
2. Mengisi file `main.html` dengan kode berikut.
```
<h1>{{ appname }}</h1>

<h5>Name: </h5>
<p>{{ name }}</p> <!-- Ubahlah sesuai dengan nama kamu -->
<h5>Class: </h5>
<p>{{ class }}</p> <!-- Ubahlah sesuai dengan kelas kamu -->
```
3. Setelah itu, membuka file `views.py` di dalam file aplikasi main, lalu menambahkan baris impor `from django.shortcuts import render` untuk mengimpor fungsi render dari modul `django.shortcuts` yang nantinya berfungsi untuk me-render file HTML yang sudah dibuat.
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
Nilai dari variabel yang didefinisikan pada `context` akan muncul pada file HTML dengan menggunakan sintaks `{{ appname }}`, `{{ name }}`, dan `{{ class }}`.

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
2. Buka command prompt di direktori `Tugas 2`, lalu membuat *branch* utama baru dengan menjalankan perintah `git branch -M master`, lalu menghubungkannya dengan repositori yang barusan dibuat di github dengan menjalankan perintah `git remote add origin https://github.com/nabielsubhan/inventory-manager.git`.
3. Melakukan *push* ke repositori GitHub dengan menjalankan perintah `git add .`, lalu `git commit -m "Proyek Inventory Manager Tugas 2 PBP"`, dan `git push -u origin master`.
4. Setelah itu, *login* ke [Adaptable.io](https://adaptable.io/).
5. Tekan tombol `New App`, lalu pilih `Connect an Existing Repository`.
6. Hubungkan [Adaptable.io](https://adaptable.io/) dengan GitHub dan pilih `All Repositories` pada proses instalasi.
7. Pilih repositori `inventory-manager` sebagai basis aplikasi yang akan di-*deploy* dan *branch* yang akan digunakan.
8. Pilih `Python App Template` sebagai template *deployment*.
9. Pilih `PostgreSQL` sebagai tipe basis data yang akan digunakan.
10. Mengganti versi python menjadi `3.11`.
11. Pada bagian `Start Command`, isi dengan `python manage.py migrate && gunicorn inventory_manager.wsgi`.
12. Masukkan `inventory-manager` sebagai nama aplikasi.
13. Centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses *deployment*.

## **BONUS: Membuat unit test**
Saya menambahkan tes untuk mengecek apakah model berhasil dibuat dan apakah data yang dibuat telah sesuai dengan menambahkan kode berikut ke file `tests.py`.
```python
from django.test import TestCase, Client
from main.models import Item

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.')

    def test_create_template(self):
        item = Item.objects.create(
            name="an item",
            amount="10",
            description="the total of this item is 10"
        )

        self.assertEqual(item.name, "an item")
        self.assertEqual(item.amount, "10")
        self.assertEqual(item.description, "the total of this item is 10")
```
Setelah menjalankan perintah `python manage.py test` pada *command prompt*, inilah hasil tes yang keluar.
```txt
Found 3 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
----------------------------------------------------------------------
Ran 3 tests in 0.012s

OK
Destroying test database for alias 'default'...
```

## Bagan *Request Client* pada Web Aplikasi Berbasis Django
![Bagan *Request Client*](image/bagan.png)<br>
Alur cara kerja Django dalam menerima *request* dari *client* adalah sebagai berikut:
1. **Permintaan dari *client***, biasanya melalui peramban web.
2. **Web Server**, permintaan *client* diterima oleh web server (Nginx atau Apache).
3. **WSGI (Web Server Gateway Interface)**, web server meneruskan *request* ke WSGI server yang bertindak sebagai perantara antara web server dengan aplikasi Django.
4. **Request**, *request client* dikirimkan ke aplikasi Django sebagai permintaan HTTP.
5. **URL Router**, mengarahkan *request* ke View yang sesuai dengan URL yang diterima.
6. **Views**, setelah menerima URL, Django memanggil fungsi pada `views.py` yang sesuai dengan permintaan.
7. **ORM (Object-Relational Mapping) dan Database**, View mengakses dan mengolah data dalam *database* sesuai dengan permintaan melalui ORM.
8. **Template Tags**, setelah selesai memproses data, View mengisi template dengan data yang akan ditampilkan (*template tags*).
9. **Context Processors**, *Context Processors* dapat digunakan untuk memberikan data tambahan yang akan ditampilkan.
10. **Template (HTML)**, setelah Template selesai diisi dengan data yang ingin ditampilkan, tampilan HTML akan siap ditampilkan ke pengguna.
11. **Response**, Django menghasilkan konten HTML dan informasi lain sebagai bentuk respons HTTP.
12. **WSGI**, respons HTTP dikirimkan kembali ke WSGI server.
13. **Web Server**, web server menerima respons HTTP dari WSGI server.
14. **Client**, *client* menerima respons dan halaman web yang sesuai dengan permintaan awal akan ditampilkan.

Hubungan antara `urls.py`, `views.py`, `models.py`, dan `html` adalah `urls.py` akan mengarahkan *request* yang diterima ke `View`, lalu `views.py` akan memanggil *function* yang sesuai dengan *request* tersebut. Nantinya `views.py` akan berinteraksi dengan `models.py` untuk memproses, mengubah, atau mengolah data di *database*. Setelah data diproses, file `html` akan diisi dengan template yang menggunakan sintaks dari Django yang memungkinkan untuk memasukkan data yang telah diperoleh dari View ke tampilan pengguna nantinya.

## Mengapa kita menggunakan *Virtual Environment*
Penggunaan *virtual environment* memberikan berbagai manfaat penting, diantaranya adalah terciptanya *environment* yang terpisah untuk setiap proyek yang kita miliki sehingga memungkinkan kita untuk menggunakan versi python, Django, maupun dependensi-dependensi yang berbeda untuk proyek yang berbeda tanpa perlu khawatir akan terjadi konflik. Selain itu, dengan menggunakan *virtual environment* akan membuat lingkungan kerja proyek menjadi lebih bersih dan terorganisir sehingga memudahkan kita untuk mengelola proyek-proyek yang berbeda. *Virtual environment* juga dapat memudahkan ketika melakukan pengerjaan suatu proyek dengan sebuah tim karena setiap anggota dapat memiliki lingkungan virtual masing-masing dengan dependensi yang mereka butuhkan.

## Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*?
Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*, tetapi akan terdapat beberapa masalah yang akan timbul, seperti konflik antara *dependencies* dan sulitnya mengelola versi python yang digunakan pada proyek berbeda. Bahkan, ketika kita mencoba untuk menghapus suatu *package* pada proyek tertentu, hal tersebut dapat berpotensi untuk merusak proyek-proyek lain yang menggunakan *package* tersebut. Oleh karena itu, penggunaan *virtual environment* sangat dianjurkan ketika membuat proyek aplikasi web berbasis Django.

## Apa itu MVC, MVT, dan MVVM
MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah suatu pola arsitektur perangkat lunak yang digunakan untuk merancang struktur dan organisasi umum suatu perangkat lunak. Pola arsitektur tersebut membagi perangkat lunak menjadi beberapa bagian sehingga pengembangan aplikasi dapat lebih terstruktur dan mudah untuk dikelola. Ketiga pola arsitektur tersebut mempunyai keunikan tersendiri dalam mengelola suatu proyek aplikasi.

* **MVC (Model-View-Controller)**
MVC membagi aplikasi menjadi 3 komponen, yaitu Model, View, dan Controller. Model berfungsi untuk memproses, menyimpan, dan mengelola data serta mengatur aturan bisnis aplikasi, View berfungsi untuk menampilkan data dari Model kepada pengguna, dan Controller berfungsi untuk mengelola aliran aplikasi dan menjaga ke-sinkronan antara Model dan View.
* **MVT (Model-View-Template)**
MVT memisahkan komponen-komponen pada aplikasi menjadi 3 bagian juga, yaitu Model, View, dan Template. Tugas Model pada MVT kurang lebih sama dengan Model pada MVC, yaitu untuk mengatur dan mengelola data aplikasi, View pada MVT berfungsi untuk mengelola logika presentasi data aplikasi kepada pengguna, sedangkan Template adalah komponen yang berfungsi untuk mengatur antarmuka yang akan ditampilkan kepada pengguna.
* **MVVM (Model-View-ViewModel)**
MVVM membagi aplikasi menjadi 3 komponen juga, yaitu Model, View, dan ViewModel. Model berfungsi untuk mengatur data dan logika bisnis aplikasi, View mengelola antarmuka untuk menampilkan data pada pengguna, sedangkan ViewModel berfungsi untuk Menghubungkan Model dan View serta menjalankan operasi untuk mengubah data pada Model yang nantinya akan ditampilkan oleh View.

MVC dan MVT biasanya digunakan untuk melakukan pengembangan web, sedangkan MVVM lebih umum digunakan untuk mengembangkan aplikasi yang berfokus pada tampilan antarmuka pengguna. Bahasa pemrograman yang biasa digunakan pada MVC adalah Ruby atau Python, pada MVT bahasa yang digunakan adalah Python, sedangkan untuk MVVM bahasa yang sering digunakan adalah C# atau Javascript. Meskipun begitu, bahasa yang digunakan ketika akan mengembangkan suatu aplikasi bergantung pada preferensi pengembang serta ekosistem yang akan digunakan.

# Tugas 3: Implementasi Form dan Data Delivery pada Django
##  Membuat input form untuk menambahkan objek model
1. Mengubah routing main/ menjadi / agar lebih sesuai dengan konvensi pada `urls.py` di folder `inventory_manager`.
```python
urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]
```
2. Membuat kerangka dasar untuk halaman web lainnya dengan membuat folder `templates` pada *root folder* dan membuat file dengan nama `base.html`. Setelah itu, isi file tersebut dengan kode berikut.
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```
3. Modifikasi file `settings.py` yang ada pada direktori `inventory_manager` dengan menambahkan kode berikut pada bagian `TEMPLATES`.
```python
'DIRS': [BASE_DIR / 'templates'],
```
4. Ubah file `main.html` pada subdirektori `templates` yang ada pada direktori `main` dengan menambahkan baris kode berikut di awal.
```html
{% extends 'base.html' %}
```
5. Membuat file baru dengan nama `forms.py` untuk membuat form yang dapat menerima data produk baru. Tambahkan kode berikut ke dalam file tersebut.
```python
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]
```
6. Buka `views.py`, lalu tambahkan *import* berikut.
```python
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
```
7. Buat fungsi `create_item` pada file `views.py` untuk membuat formulir yang dapat menambahkan data item baru ketika form di-*submit*.
```python
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```
8. Ubah fungsi `show_main` pada file `views.py` menjadi seperti berikut.
```python
def show_main(request):
    items = Item.objects.all()

    context = {
        'appname': 'Inventory Manager',
        'name': 'Muhammad Nabiel Subhan',
        'class': 'PBP A',
        'items': items
    }

    return render(request, "main.html", context)
```
9. *Import* fungsi `create_item` yang sudah dibuat sebelumnya ke file `urls.py` pada direktori `main` dengan menambahkan kode `from main.views import show_main, create_item`, lalu tambahkan *url path*-nya ke `urlpatterns` dengan menambahkan kode `path('create-item', create_item, name='create_item'),`.
10. Buat file dengan nama `create_item.html` pada direktori `main/templates` dan isi file tersebut dengan kode berikut.
```html
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
11. Tambahkan kode berikut pada file `main.html` di dalam `{% block content %}` untuk menampilkan data item dalam bentuk tabel dan menambahkan tombol `Add New Item` yang akan me-*redirect* ke file `create_item.html`.
```html
<table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>

        {% comment %} Berikut cara memperlihatkan data item di bawah baris ini {% endcomment %}

        {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.amount}}</td>
                <td>{{item.description}}</td>
                <td>{{item.date_added}}</td>
            </tr>
        {% endfor %}
    </table>

    <br />

    <a href="{% url 'main:create_item' %}">
        <button>
            Add New Item
        </button>
    </a>
```

## Menambahkan 5 fungsi baru pada `views.py` untuk menampilkan objek yang ditambahkan dalam bentuk HTML, XML, JSON, XML by ID, dan JSON by ID
1. Fungsi untuk menampilkan objek dalam bentuk HTML
* Fungsi `show_main` yang sudah pernah dibuat sebelumnya akan me-*render* file `main.html` yang berisi data item-item yang telah dimasukkan.
```python
def show_main(request):
    items = Item.objects.all()

    context = {
        'appname': 'Inventory Manager',
        'name': 'Muhammad Nabiel Subhan',
        'class': 'PBP A',
        'items': items
    }

    return render(request, "main.html", context)
```
2. Fungsi untuk menampilkan objek yang ditambahkan dalam bentuk XML
* Tambahkan kode *import* berikut pada file `views.py` yang ada pada direktori `main`.
```python
from django.http import HttpResponse
from django.core import serializers
```
* Buat fungsi `show_xml` yang menerima parameter berupa `request` dan memiliki *return statement* yang akan mengembalikan `HttpResponse` yang berisi data *query* yang sudah diserialisasi menjadi XML.
```python
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
3. Fungsi untuk menampilkan objek yang ditambahkan dalam bentuk JSON
* Buat fungsi `show_json` yang menerima parameter berupa `request` dan memiliki *return statement* yang akan mengembalikan `HttpResponse` yang berisi data *query* yang sudah diserialisasi menjadi JSON.
```python
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
4. Fungsi untuk mengembalikan data berdasarkan ID dalam bentuk XML
* Buat fungsi `show_xml_by_id` yang menerima parameter berupa `request` dan ID yang memiliki *return statement* yang akan mengembalikan `HttpResponse` yang berisi data *query* yang sudah diserialisasi menjadi XML.
```python
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
5. Fungsi untuk mengembalikan data berdasarkan ID dalam bentuk JSON
* Buat fungsi `show_json_by_id` yang menerima parameter berupa `request` dan ID yang memiliki *return statement* yang akan mengembalikan `HttpResponse` yang berisi data *query* yang sudah diserialisasi menjadi JSON.
```python
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
6. Setelah itu, *import* semua fungsi yang sudah dibuat di atas ke dalam file `urls.py` yang ada pada direktori `main`.
```python
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
```
7. Tambahkan *path url* ke dalam `urlpatters` agar bisa mengakses fungsi-fungsi yang sudah dibuat.
```python
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id')
]
```

## Perbedaan antara *form* `POST` dan `GET` pada Django
Perbedaan antara `POST` dan `GET` dapat dilihat pada cara pengiriman datanya. Method `POST` akan mengirimkan data yang ditulis pada form tanpa mencantumkan data tersebut ke url sehingga data yang dikirim tidak akan terlihat oleh siapapun. Biasanya method `POST` digunakan untuk mengirimkan data sensitif, seperti *password*. Di sisi lain, method `GET` akan mengirimkan data yang ditulis pada form dan mencantumkan data tersebut sebagai parameter pada url. Selain itu, perbedaan antara `POST` dan `GET` pada Django adalah tujuan penggunaannya, `POST` biasanya digunakan untuk mengirimkan data yang nantinya akan diolah di server atau melakukan perubahan data pada server, sedangkan `GET` digunakan untuk melakukan permintaan yang bersifat membaca saja.

## Perbedaan XML, JSON, dan HTML dalam konteks pengiriman data
* XML atau *eXtensible Markup Language* dirancang untuk menyimpan dan mengirimkan data. Data pada XML akan direpresentasikan seperti bentuk struktur *tree*. Cara menulisnya adalah dengan menyisipkan data yang ingin disusun pada sepasang *tag* pembuka dan *tag* penutup. Hal tersebut membuat XML memiliki aturan sintaksis yang cukup ketat dan lebih kaku. Selain itu, XML membutuhkan parser khusus untuk memproses data sehingga memakan waktu yang lama untuk mengurai data tersebut.
* JSON atau *JavaScript Object Notation* adalah format untuk menynusun data yang lebih ringan dan mudah dimengerti dibandingkan dengan XML. Data pada JSON disusun dalam bentuk text sehingga memudahkan kita untuk membaca dan memahami data tersebut. Cara menyusun data pada JSON adalah dengan menggunakan pasangan *key* dan *value*. Selain itu, JSON lebih mudah diproses oleh mesin maupun manusia dibandingkan dengan XML.
* HTML atau *HyperText Markup Language* biasanya dirancang untuk menampilkan data dalam bentuk halaman web yang nantinya akan di-*render* oleh web browser sehingga data yang ingin dibaca dapat ditampilkan kepada pengguna. HTML bukanlah format untuk menyimpan maupun melakukan pertukaran data seperti XML atau JSON.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON memiliki banyak keunggulan, seperti menggunakan syntax yang mudah dimengerti, lebih mudah diurai datanya dibandingkan XML, memiliki ukuran file yang lebih kecil, dan transmisi data yang lebih cepat.

## Mengakses kelima URL di poin 2 menggunakan Postman
* HTML (http://localhost:8000)
 ![alt-text](image/postman_html.png)
* XML (http://localhost:8000/xml)
 ![alt-text](image/postman_xml.png)
* JSON (http://localhost:8000/json)
 ![alt-text](image/postman_json.png)
* XML by ID (http://localhost:8000/xml/1)
 ![alt-text](image/postman_xml_by_id.png)
* JSON by ID (http://localhost:8000/json/2)
 ![alt-text](image/postman_json_by_id.png)

   
