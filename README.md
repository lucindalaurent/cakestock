# CakeStock - Pengelolaan Stok Produk pada Toko Kue
### currently being disabled by Adaptable :( 

Nama: Lucinda Laurent<br>
NPM: 2206024745<br>
Kelas: PBP A<br>

## Checklist Tugas
- [x] Membuat sebuah proyek Django baru. <br>
* Membuat repositori github baru dengan nama "cakestock" dengan visibilitas _public_
* Membuat direktori lokal dengan nama "cakestock" juga lalu membuka _command prompt_ dari dalam direktori tersebut
* Membuat _branch_ utama dengan nama main dengan perintah `git branch -M main`
* Menghubungkan direktori lokal dengan repositori github menggunakan `git remote add origin https://github.com/lucindalaurent/cakestock.git`
* Menambahkan file .gitignore
* Membuat _virtual environment_ dengan perintah `python -m venv env`
* Mengaktifkan _virtual environment_ tersebut dengan perintah `env\Scripts\activate.bat`
* Membuat berkas `requirements.txt` berisi _dependencies_ yang dibutuhkan:
 ```bash
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
* Meng-_install dependencies_ tersebut dengan perintah `pip install -r requirements.txt`
* Membuat proyek Django bernama `cakestock` dengan perintah `django-admin startproject cakestock .`
* Melakukan konfigurasi proyek dengan menambahkan * pada `ALLOWED_HOSTS` di `settings.py`supaya aplikasi dapat diakses secara luas
* Melakukan `add`, `commit`, dan `push` untuk menyimpan perubahan sementara <br>
- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.<br>
* Masih di direktori utama, aktifkan _virtual environment_ yang telah dibuat
* Jalankan perintah `python manange.py startapp main` untuk membentuk struktur awal aplikasi
* Daftarkan aplikasi main ke dalam proyek dengan membuka `settings.py`, kemudian tambahkan `main` ke dalam daftar `INSTALLED_APPS`
```bash
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```
- [x] Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`.<br>
* Membuka berkas `urls.py` dalam direktori proyek `cakestock`.
* Impor fungsi `include`, lalu tambahkan rute url untuk mengarahkan ke tampilan `main`  

```bash
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```
- [x] Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut. <br>
* name sebagai nama item dengan tipe CharField.
* amount sebagai jumlah item dengan tipe IntegerField.
* description sebagai deskripsi item dengan tipe TextField. <br>
Dilakukan dengan membuka models.py pada direktori aplikasi `main` kemudian mengisi file dengan kode:
```bash
from django.db import models
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
```
Lalu membuat berkas migrasi berisi perubahan model yang belum diaplikasikan dengan `python manage.py makemigrations`. Terapkan migrasi ke dalam basis data lokal menggunakan `python manage.py migrate`

- [x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
* Pada berkas `views.py` ditambahkan fungsi render_main untuk me-_render_ tampilan html menggunakan data yang diberikan. 
```bash
from django.shortcuts import render
def render_main(request):
    context = {
        'appname': 'CakeStock',
        'name': 'Lucinda Laurent',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
```
- [x] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`. 
* Membuat berkas `urls.py` di dalam direktori `main`.
* Isi file tersebut dengan 
```bash
from django.urls import path
from main.views import render_main

app_name = 'main'

urlpatterns = [
    path('', render_main, name='render_main'),
]
```
Sebelum melakukan deployment, saya memastikan untuk melakukan git add, commit, dan push semua perubahan yang saya lakukan pada direktori cakestock.
- [ ] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
* Karena sudah memiliki akun, saya bisa langsung _sign in_ menggunakan akun github proyek.
* Setelah _sign in_, tekan tombol `New App`. Pilih `Connect an Existing Repository.`
* Menghubungkan Adaptable.io dengan GitHub dan memiilih _All Repositories_ pada proses instalasi.
* Memilih repositori proyek cakestock sebagai basis aplikasi yang akan di-deploy
* Memilih Python App Template sebagai template deployment.
* Memilih PostgreSQL sebagai tipe basis data yang akan digunakan.
* Menyesuaikan versi Python dengan spesifikasi aplikasi saya yaitu python 3.11. 
* Pada bagian Start Command masukkan perintah python manage.py `migrate && gunicorn cakestock.wsgi`.
* Memasukkan `CakeStock` sebagai nama aplikasi yang juga akan menjadi nama domain situs web aplikasi.
* Mencentang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses deployment aplikasi. -> belum berhasil deploy

- [x] Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut. <br>
Tautan menuju aplikasi Adaptable belum tersedia :(
## Jawaban dari pertanyaan
* Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas html.
* Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? <br>
_Virtual environment_ adalah alat yang membantu memisahkan dependensi yang diperlukan oleh proyek berbeda dengan membuat lingkungan virtual python terisolasi untuk proyek tersebut. Kita menggunakan _virtual environment_ karena penggunaan _virtual environment_ memiliki banyak keunggulan.
Setiap _virtual environment_ memiliki _package_ tersendiri yang terisolasi dari _global package_ maupun _package_ dari _virtual environment_ lainnya. Ini memungkinkan kita untuk memiliki versi _package_ yang berbeda untuk proyek-proyek yang berbeda tanpa khawatir akan adanya konflik. Selain itu, kita dapat membuat file requirements.txt yang mencantumkan semua _package_ dan versi yang dibutuhkan oleh proyek kita. Jika seseorang ingin menjalankan kode kita di mesin mereka, mereka hanya perlu membuat _virtual environment_ baru dan menginstal semua paket yang tercantum dalam file requirements.txt. Ini memastikan bahwa mereka memiliki semua _dependencies_ yang diperlukan dan dalam versi yang tepat. Oleh karena itu, penggunaan _virtual environment_ sangat membantu dalam kolaborasi dan penyebaran kode. Ya, kita dapat tetap membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_. Jika proyek aplikasi web kita sederhana dan tidak _package-dependent_, kita tidak memerlukan isolasi untuk versi _package_ yang berbeda. Namun jika proyek kita memerlukan _package_ atau _library_ tambahan, sebaiknya kita memang menggunakan _virtual environment_ untuk mengelola _dependencies_ dan mencegah konflik antarversi _package_ yang berbeda. 

* Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Ini bagan](img/bagan_request_client.jpg)
Penjelasan:
1. Saat _user_ melakukan _request_ ke internet, Django akan menerima http _request_
2. Jika _path_ http _request_ yang diterima ada di dalam `urls.py`,  _request_ akan diteruskan dan memanggil fungsi pada `views.py`.
3. Secara umum, View(views.py) akan memproses _request_ sesuai dengan fungsi yang telah definisikan dengan mengambil data dari _database_ (models.py) dan menyajikan data tersebut sesuai isi file html di dalam Template(melakukan render template). Selain membaca, View juga bisa menulis atau menambahkan data ke _database_. 
4. Setelah prosesnya selesai, _request_ dari _user_ akan dikembalikan sebagai _response_ yaitu halaman html yang telah di-_render_.

* Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya. <br>
MVC, MVT, dan MVVM adalah macam-macam pola desain populer dalam pengembangan perangkat lunak yang digunakan untuk memisahkan logika aplikasi menjadi komponen-komponen yang berbeda.
1. MVC: Model-View-Controller
Model: komponen yang berisi tentang logika bisnis dan status data yang ada di dalam aplikasi. Komponen ini bertugas untuk mendapatkan dan memanipulasi data, berkomunikasi dengan Controller, berinteraksi dengan database, terkadang memperbarui tampilan dari aplikasi yang dikembangkan.
View: komponen yang berhubungan dengan antarmuka pengguna, biasanya terdiri dari HTML/CSS.XML. View berkerja sama dengan Controller untuk menciptakan tampilan dinamis pada aplikasi yang dikembangkan. Selain bertugas untuk menangani antarmuka dan interaksi pengguna, komponen View juga memiliki tugas untuk menyajikan data yang sesuai untuk pengguna.
Controller: komponen yang berfungsi sebagai komunikator antara View dan model. Komponen ini membutuhkan suatu input pengguna dari layanan View/REST. Lalu Permintaan “Get Data” diproses dari model dan diteruskan ke View untuk ditampilkan ke pengguna.
2. MVT: Model-View-Template
MVT adalah variasi dari pola MVC yang digunakan oleh Django. Dalam MVT, “Template” adalah apa yang disebut “View” dalam MVC, dan “View” dalam MVT adalah apa yang disebut “Controller” dalam MVC. Jadi, dalam MVT, View bertanggung jawab untuk menangani permintaan dan logika bisnis, sementara Template bertanggung jawab untuk menampilkan data kepada pengguna.
3. MVVM: Model-View-ViewModel
Model: Model yang digunakan untuk MVVM mirip dengan model yang digunakan MVC, dimana model tersebut terdiri dari data dasar yang digunakan untuk menjalankan perangkat lunak.
View: View digunakan sebagai antarmuka grafis antara pengguna dan pola desain, serta menampilkan output dari data yang telah diproses. View yang digunakan MVVM mirip dengan View yang digunakan dalam MVC. View pada MVVM juga menangani input user. 
ViewModel: ViewModel di satu sisi adalah abstraksi dari View, lalu di sisi yang lain, sebagai penyedia pembungkus data model untuk ditautkan. ViewModel terdiri dari Model yang diubah menjadi View, dan berisi perintah yang dapat digunakan oleh View untuk memengaruhi Model.








