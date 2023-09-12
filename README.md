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
<br>
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
<br>
- [ ] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
* Karena sudah memiliki akun, saya bisa langsung _sign in_ menggunakan akun github proyek.
* Setelah _sign in_, tekan tombol `New App`. Pilih `Connect an Existing Repository.`
* Hubungkan Adaptable.io dengan GitHub dan pilih _All Repositories_ pada proses instalasi.
* Pilihlah repositori proyek cakestock sebagai basis aplikasi yang akan di-deploy
* Pilihlah Python App Template sebagai template deployment.
* Pilih PostgreSQL sebagai tipe basis data yang akan digunakan.
* Menyesuaikan versi Python dengan spesifikasi aplikasi saya yaitu python 3.11. 
* Pada bagian Start Command masukkan perintah python manage.py `migrate && gunicorn cakestock.wsgi`.
* Masukkan `CakeStock` sebagai nama aplikasi yang juga akan menjadi nama domain situs web aplikasi.
* Centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses deployment aplikasi. -> belum berhasil deploy

- [x] Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.<br>
Tautan menuju aplikasi Adaptable belum tersedia.
* Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas html.
* Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? <br>







