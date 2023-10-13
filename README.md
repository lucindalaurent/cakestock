# CakeStock - Pengelolaan Stok Produk pada Toko Kue
### currently being disabled by Adaptable :( 

Nama: Lucinda Laurent<br>
NPM: 2206024745<br>
Kelas: PBP A<br>

<details>
<summary>Tugas 2</summary>

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
* Mengimpor fungsi `include`, lalu tambahkan rute url untuk mengarahkan ke tampilan `main`  

```bash
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```
- [x] Membuat model pada aplikasi main dengan nama Item dan memiliki atribut sebagai berikut. <br>
* _name_ sebagai nama item dengan tipe CharField.
* _amount_ sebagai jumlah item dengan tipe IntegerField.
* _description_ sebagai deskripsi item dengan tipe TextField. 
* _price_ sebagai harga item dengan tipe IntegerField (tidak wajib)<br>
Dilakukan dengan membuka models.py pada direktori aplikasi `main` kemudian mengisi file dengan kode:
```bash
from django.db import models
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
```
Lalu membuat berkas migrasi berisi perubahan model yang belum diaplikasikan dengan perintah `python manage.py makemigrations`. Berkas migrasi tersebut diterapkan ke dalam basis data lokal menggunakan `python manage.py migrate`

- [x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
* Pada berkas `views.py` ditambahkan fungsi `render_main` untuk me-_render_ tampilan html menggunakan data yang diberikan. 
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
* Mengisi file tersebut dengan 
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

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Ini bagan](img/bagan_request_client.jpg)
Penjelasan:
1. Saat _user_ melakukan _request_ ke internet, Django akan menerima http _request_
2. Jika _path_ http _request_ yang diterima ada di dalam `urls.py`,  _request_ akan diteruskan dan memanggil fungsi pada `views.py`.
3. Secara umum, View`(views.py)`akan memproses _request_ sesuai dengan fungsi yang telah definisikan dengan mengambil data dari _database_ `(models.py)` dan menyajikan data tersebut sesuai isi file html di dalam Template(melakukan render template). Selain membaca, View juga bisa menulis atau menambahkan data ke _database_. 
4. Setelah prosesnya selesai, _request_ dari _user_ akan dikembalikan sebagai _response_ yaitu halaman html yang telah di-_render_.

## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? <br>
_Virtual environment_ adalah alat yang membantu memisahkan dependensi yang diperlukan oleh proyek berbeda dengan membuat lingkungan virtual python terisolasi untuk proyek tersebut. Kita menggunakan _virtual environment_ karena penggunaan _virtual environment_ memiliki banyak keunggulan.
Setiap _virtual environment_ memiliki _package_ tersendiri yang terisolasi dari _global package_ maupun _package_ dari _virtual environment_ lainnya. Ini memungkinkan kita untuk memiliki versi _package_ yang berbeda untuk proyek-proyek yang berbeda tanpa khawatir akan adanya konflik. Selain itu, kita dapat membuat file `requirements.txt` yang mencantumkan semua _package_ dan versi yang dibutuhkan oleh proyek kita. Jika seseorang ingin menjalankan kode kita di mesin mereka, mereka hanya perlu membuat _virtual environment_ baru dan menginstal semua paket yang tercantum dalam file `requirements.txt`. Ini memastikan bahwa mereka memiliki semua _dependencies_ yang diperlukan dan dalam versi yang tepat. Oleh karena itu, penggunaan _virtual environment_ sangat membantu dalam kolaborasi dan penyebaran kode. <br>
Ya, kita dapat tetap membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_. Jika proyek aplikasi web kita sederhana dan tidak bersifat _package-dependent_, kita tidak memerlukan isolasi untuk versi _package_ yang berbeda. Namun jika proyek kita memerlukan _package_ atau _library_ tambahan, sebaiknya kita memang menggunakan _virtual environment_ untuk mengelola _dependencies_ dan mencegah konflik antarversi _package_ yang berbeda. 

## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya. <br>
MVC, MVT, dan MVVM adalah macam-macam pola desain populer dalam pengembangan perangkat lunak yang digunakan untuk memisahkan logika aplikasi menjadi komponen-komponen yang berbeda.
1. MVC: Model-View-Controller 
* Model: komponen yang berisi tentang logika bisnis dan status data yang ada di dalam aplikasi. Komponen ini bertugas untuk mendapatkan dan memanipulasi data, berkomunikasi dengan Controller, berinteraksi dengan database, terkadang memperbarui tampilan dari aplikasi yang dikembangkan.<br>
* View: komponen yang berhubungan dengan antarmuka pengguna, biasanya terdiri dari HTML/CSS.XML. View berkerja sama dengan Controller untuk menciptakan tampilan dinamis pada aplikasi yang dikembangkan. Selain bertugas untuk menangani antarmuka dan interaksi pengguna, komponen View juga memiliki tugas untuk menyajikan data yang sesuai untuk pengguna.<br>
* Controller: komponen yang berfungsi sebagai komunikator antara View dan model. Komponen ini membutuhkan suatu input pengguna dari layanan View/REST. Lalu Permintaan “Get Data” diproses dari model dan diteruskan ke View untuk ditampilkan ke pengguna.<br>
2. MVT: Model-View-Template
MVT adalah variasi dari pola MVC yang digunakan oleh Django. Dalam MVT, “Template” adalah apa yang disebut “View” dalam MVC, dan “View” dalam MVT adalah apa yang disebut “Controller” dalam MVC. Dalam MVT, View bertanggung jawab untuk menangani permintaan dan logika bisnis, sementara Template bertanggung jawab untuk menampilkan data kepada pengguna. <br>
3. MVVM: Model-View-ViewModel
* Model: Model yang digunakan untuk MVVM mirip dengan model yang digunakan MVC, dimana model tersebut terdiri dari data dasar yang digunakan untuk menjalankan perangkat lunak.<br>
* View: View digunakan sebagai antarmuka grafis antara pengguna dan pola desain, serta menampilkan output dari data yang telah diproses. View yang digunakan MVVM mirip dengan View yang digunakan dalam MVC. View pada MVVM juga menangani input user. <br>
* ViewModel: ViewModel di satu sisi adalah abstraksi dari View, lalu di sisi yang lain, sebagai penyedia pembungkus data model untuk ditautkan. ViewModel terdiri dari Model yang diubah menjadi View, dan berisi perintah yang dapat digunakan oleh View untuk memengaruhi Model.
<br>
</details>

<details>
 <summary>Tugas 3</summary>

- [x] Jawaban Pertanyaan <br>
## Apa perbedaan antara form POST dan form GET dalam Django? <br>
Dalam Django, form POST dan GET memiliki perbedaan dalam cara mengirimkan data. Saat menggunakan form POST, browser menggabungkan data formulir, mengkodekannya untuk transmisi, mengirimkannya ke server, dan kemudian menerima kembali responsnya. Form POST digunakan ketika data yang dikirimkan akan mengubah database di server. Misalnya saat pengguna mengisi form pendaftaran atau login yang memerlukan password. Sedangkan form GET digunakan untuk form yang tidak mengubah data pengguna, seperti form pencarian. Metode ini menggabungkan data yang dikirimkan menjadi string dan menggunakan string tersebut untuk membuat URL. URL akan berisi alamat tujuan pengiriman data, serta _keys_ dan _values_ dari data. Hal ini ditandai dengan adanya parameter dalam URL, seperti "?query=search_term". Dengan demikian, form POST lebih aman dari GET karena data yang dikirimkan tidak terlihat dalam URL. Artinya data tersebut tidak akan disimpan dalam log server atau riwayat browser. Sebaliknya, form GET mengirimkan data melalui URL, yang berarti data tersebut bisa terlihat oleh siapa saja yang melihat URL dan bisa disimpan dalam log server atau riwayat browser. Oleh karena itu, form GET cocok digunakan untuk form pencarian web karena URL yang mewakili permintaan GET dapat dengan mudah di-bookmark, dibagikan, atau dikirim ulang. <br>

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data? <br>
JSON dan XML adalah representasi data yang digunakan dalam pertukaran data antaraplikasi.
1. XML (eXtensible Markup Language):
* XML adalah bahasa markup yang digunakan untuk membuat dokumen yang dapat dibaca oleh manusia maupun mesin.
* XML biasanya digunakan untuk mengirim data yang kompleks dan sangat terstruktur seperti dokumen atau laporan keuangan.
* XML merepresentasikan item data menggunakan tag dan membentuk struktur pohon dengan _namespace_ untuk kategori data yang berbeda.
* XML tidak mendukung penggunaan _array_
* Struktur tag XML lebih kompleks untuk ditulis dan dibaca sehingga menghasilkan file yang memerlukan banyak ruang.
* Struktur XML rentan terhadap modifikasi yang tidak sah dan deklarasi tipe dokumen eksternal (external document type declaration/DTD) yang tidak terstruktur. 

2. JSON (JavaScript Object Notation):
* JSON adalah format pertukaran data menggunakan teks yang dapat dibaca baik oleh manusia maupun mesin.
* JSON umumnya merupakan pilihan yang lebih baik untuk API, aplikasi seluler, dan penyimpanan data.
* JSON merepresentasikan data sebagai objek yang berisi pasangan _attribute-value_
* JSON mendukung penggunaan _array_
* JSON memiliki ukuran file yang lebih kecil dan transmisi data yang lebih cepat.
* Selain terkesan ringan dan mudah digunakan, JSON memiliki keamanan data yang lebih baik dibandingkan XML.

3. HTML (HyperText Markup Language):
* HTML adalah bahasa markup standar untuk dokumen yang dirancang untuk ditampilkan di browser web.
* HTML tidak dirancang untuk menyimpan data. Sebaliknya, HTML digunakan untuk menampilkan data dan fokus pada bagaimana data terlihat dan disajikan.
* HTML menggunakan tag untuk menentukan bagaimana konten ditampilkan dalam browser web.

#### Dalam konteks pengiriman data, XML dan JSON digunakan untuk menyimpan dan mengirim data, sementara HTML digunakan untuk menampilkan data. XML dan JSON digunakan saat data perlu dikirim dari server ke klien atau sebaliknya, sementara HTML digunakan untuk menampilkan data tersebut ke pengguna. HTML bukanlah suatu bentuk representasi data. Akan tetapi, HTML dapat digunakan untuk mengumpulkan dan mengirim data ke server dengan menggunakan elemen `form`<br>

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern? <br>
Meningkatnya popularitas JavaScript turut meningkatkan popularitas JSON. Banyak pengembang yang bekerja dengan JavaScript lebih memilih sintaks JSON yang mudah dibaca daripada struktur XML yang kompleks. Selain itu, JSON lebih mudah diurai daripada XML. Kita dapat mengurai file JSON menjadi objek siap pakai yang dapat dibaca oleh manusia dan mesin. Berikut adalah kelebihan JSON yang menjadi alasan JSON sering digunakan:
1. **Ringan dan efisien**: JSON adalah format pertukaran data yang ringan, memungkinkan pertukaran data yang cepat dan efisien antara server dan klien.
2. **Mudah dibaca dan dipahami**: JSON mudah dibaca oleh manusia dan mesin, yang memudahkan pengembangan dan debugging.
3. **Struktur data fleksibe**l: JSON dapat merepresentasikan berbagai jenis data, termasuk tipe data dasar seperti string, angka, boolean, serta struktur yang lebih kompleks seperti objek dan array.
4. **Kompatibilitas lintas platform**: JSON didukung oleh sebagian besar bahasa pemrograman modern, memungkinkan data dalam format JSON dapat dengan mudah diolah dan dimanipulasi di berbagai platform dan lingkungan.  
5. **Ideal untuk API**: JSON bersifat independen dari setiap bahasa pemrograman dan merupakan output API umum dalam berbagai aplikasi. JSON sering digunakan pada API karena strukturnya yang sederhana dan mudah dipahami. <br>

## Jelaskan bagaimana cara kamu mengimplementasikan checklist secara step-by-step.
- [x] Membuat input form untuk menambahkan objek model pada app sebelumnya.
Sebelum kita membuat form, kita perlu membuat suatu _skeleton_ yang berfungsi sebagai kerangka _views_ untuk memastikan adanya konsistensi dalam desain situs web kita, serta memperkecil kemungkinan terjadinya redundansi kode. 
1. Membuat folder `templates` pada root folder dan membuat sebuah berkas HTML baru bernama `base.html` dengan isi sebagai berikut
```
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
2. Mengedit `TEMPLATES` pada file `settings.py` di subdirektori `cakestock` agar file `base.html` terdeteksi sebagai file template
```
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
        'APP_DIRS': True,
        ...
    }
]
...
```
Selanjutnya kita sudah bisa mulai membuat form
1. Membuat berkas baru pada direktori `main` dengan nama `forms.py` untuk membuat struktur form yang dapat menerima data item baru. Isi dari `forms.py`adalah 
```
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        #Ketika data dari form disimpan, isi dari form akan disimpan menjadi sebuah objek Item
        model = Item
        #Field/atribut dari object Item
        fields = ["name", "amount", "description", "price"]

```
2. Mengupdate berkas `views.py` pada folder `main`: 
* Menambahkan import
```
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
```
* Menambahkan fungsi `create_item`
```
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:render_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```
* Mengedit fungsi `render_main` menjadi seperti di bawah
```
def render_main(request):
    items = Item.objects.all()
    
    context = {
        'appname': 'CakeStock',
        'name': 'Lucinda Laurent',
        'class': 'PBP A',
        'items': items
    }

    return render(request, "main.html", context)
```
3. Mengimpor fungsi `create_item` pada `urls.py` di folder `main`
4. Menambahkan _path url_ ke dalam `urlpatterns` pada `urls.py` di `main` untuk mengakses fungsi `create_item`
```
path('create-item', create_item, name='create_item')
```
5. Membuat berkas HTML baru dengan nama `create_item.html` pada direktori `main/templates` yang berisi
```
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

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
6. Menambahkan kode berikut di dalam {% block content %} pada `main.html` untuk menampilkan data produk pada html dalam bentuk tabel serta tombol "Add New Item" yang akan redirect ke halaman form.
```
...
<table border="1">
    <tr>
        <th>Name</th>
        <th>Amount</th>
        <th>Description</th>
        <th>Price</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for item in items %}
    <tr>
        <td>{{item.name}}</td>
        <td>{{item.amount}}</td>
        <td>{{item.description}}</td>
        <td>{{item.price}}</td>
    </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_item' %}">
    <button>
        Add New Item
    </button>
</a>
{% endblock content %}
```
- [x] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
1. Fungsi views untuk menampilkan data objek pada html sudah dihandle oleh fungsi `render_main`
2. Mengimpor module dan class yang dibutuhkan
```
from django.http import HttpResponse
from django.core import serializers
```
3. Menambahkan fungsi-fungsi berikut pada `views.py` di folder `main`:
* Fungsi `show_xml`
```
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
* Fungsi `show_json` 
```
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
* Fungsi `show_xml_by_id`
```
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
* Fungsi `show_json_by_id`
```
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
- [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan.
1. Mengimpor semua fungsi views yang telah dibuat ke `urls.py` pada folder `main`
```
from main.views import render_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 
```
2. Menambahkan _path url_ ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.
```
...
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id')
```

## Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman
### Hasil akses HTML
![html](img/postman_tugas3/html.png)
### Hasil akses XML
![xml](img/postman_tugas3/xml.png)
### Hasil akses JSON
![json](img/postman_tugas3/json.png)
### Hasil akses XML by ID
![xml_id](img/postman_tugas3/xml_by_id.png)
### Hasil akses JSON by ID
![json_id](img/postman_tugas3/json_by_id.png)

</details>

<details>
<summary> Tugas 4 </summary>
- [x] Jawaban Pertanyaan <br>
## Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
`UserCreationForm` adalah impor form bawaan Django yang memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web. Dengan formulir ini, pengguna baru dapat mendaftar dengan mudah di situs web kita tanpa kita harus menulis kode dari awal. Untuk menggunakan `UserCreationForm`, kita perlu mengimpornya dari `django.contrib.auth.forms`. Django `UserCreationForm` hanya memiliki 3 buah _fields_: _username, password1, dan _password2_ (field untuk konfirmasi password). Oleh karena itu, kelebihan `UserCreationForm` adalah mudah digunakan dan terintegrasi dengan sistem autentikasi Django. Sedangkan kelemahannya, `UserCreationForm` memiliki _fields_ yang terbatas. Hal ini dapat merugikan, misalnya kita tidak bisa mengirim email verifikasi kepada _user_ yang baru mendaftar karena tidak terdapat _field_ email. Akibatnya kita perlu usaha ekstra untuk memodifikasi dan menambahkan _field_ email atau membuat form registrasi _user_ dari awal.

##  Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi adalah proses verifikasi identitas pengguna untuk membuktikan orang yang mengakses aplikasi adalah orang yang benar. Dengan kata lain, sistem memastikan apakah benar pengguna adalah siapa yang mereka klaim. Misalnya saat kita melakukan proses _login_, kita akan diminta mengisi _username_ dan _password_ untuk memastikan kita hanya bisa masuk ke akun masing-masing. Sistem kemudian memeriksa apakah ada pengguna dengan nama pengguna tersebut dan apakah kata sandi yang diberikan cocok dengan apa yang ada di sistem. 

Di sisi lain, otorisasi adalah proses lanjutan dari autentikasi, yaitu memverifikasi apakah pengguna memiliki akses terhadap _resource_ tertentu. Contoh penerapan otorisasi adalah adanya perbedaan hak akses untuk _admin_ dan _user_. _Admin_ dapat mengakses semua halaman atau _resource_ yang ada pada aplikasi, sedangkan _user_ memiliki akses terbatas. Kedua konsep ini penting karena autentikasi dan otorisasi membantu menjaga keamanan aplikasi web kita dengan melindungi data dan fungsi aplikasi kita dari akses yang tidak sah. Autentikasi memastikan bahwa hanya pengguna yang valid yang dapat masuk ke sistem aplikasi kita, sementara otorisasi memastikan bahwa pengguna hanya dapat melakukan tindakan yang sesuai dengan hak dan peran mereka (membatasi apa yang dapat dilakukan). 

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
_Cookies_ dalam konteks aplikasi web adalah file teks kecil berisi potongan data yang digunakan untuk mengidentifikasi komputer kita saat menggunakan jaringan. _Cookies_ dapat dianggap sebagai suatu token (barisan karakter) untuk mengenali _session_ yang unik pada aplikasi web tertentu. _Cookies_ spesifik digunakan untuk mengidentifikasi pengguna dan meningkatkan pengalaman _browsing_ web mereka. Django menyediakan kerangka kerja sesi yang memungkinkan untuk menyimpan dan mengambil data secara anonim pada basis pengunjung situs. Django mengabstraksi proses pengiriman dan penerimaan _cookies_, dengan menempatkan `session ID` sebagai _cookie_ di sisi klien, dan menyimpan semua data terkait di sisi server. Dengan cara ini, hanya `session ID` yang terlihat oleh pengguna, sementara data sesi tetap tersembunyi di server.
Cara Django menggunakan _cookies_ untuk mengelola data sesi pengguna:
1. Saat pengguna mengunjungi situs web Django, Django menciptakan `session` untuk pengguna tersebut.
2. Django kemudian mengirimkan `cookie` ke browser pengguna yang berisi `session ID`.
3. Ketika pengguna kembali ke situs web, browser mengirimkan `cookie` ini kembali ke server.
4. Django kemudian dapat menggunakan `session ID` ini untuk mengambil data `session` pengguna dari server.

Penggunaan `cookies` memungkinkan Django untuk “mengingat” pengguna dan menyediakan pengalaman yang disesuaikan untuk mereka. Misalnya, situs web _e-commerce_ menggunakan `cookies` untuk mengetahui barang apa yang telah dimasukkan pengguna ke dalam keranjang belanja mereka.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Pada dasarnya, _cookies_ aman digunakan dan tidak dapat membawa _virus_ atau _malware_ maupun mentransfer program berbahaya ke pengguna. Namun cara kerja _cookies_ dapat disalahgunakan oleh pihak yang tidak bertanggung jawab. Contoh serangan yang dapat terjadi:
* Cross-Site Request Forgery (CSRF)<br>
Serangan ini dapat terjadi karena browser akan mengirim _cookie_ sebagai respon atas sebuah _request_, tanpa mengecek siapa yang mengirim _request_ tersebut. 
* Cross-Site Scripting (XSS)<br>
Serangan di mana penyerang memasukkan script berbahaya ke dalam situs web. Script berbahaya tersebut kemudian dapat mengakses _cookies_. Jika situs web tidak memiliki prosedur keamanan yang ketat, penyerang dapat mencuri _cookies_, menggunakannya untuk menyamar sebagai pengguna tertentu dan mendapatkan akses ke akun dan informasi pengguna tersebut.

## Implementasi Checklist

- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar. <br>
1. Menambahkan fungsi untuk melakukan register, login, dan logout di `views.py`:
* Mengimpor _module, class_, dan `build-in function` yang diperlukan
```
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
```
* Membuat fungsi register
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
* Membuat fungsi login
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:render_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
* Membuat fungsi logout
```def logout_user(request):
    logout(request)
    return redirect('main:login')
```
2. Membuat berkas-berkas HTML baru pada folder `main/templates`:
* berkas `register.html`
```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
* berkas `login.html`
```
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```
3. Memodifikasi berkas `main.html` dengan menambahkan tombol _logout_ di bawah tombol _Add New Item_
```
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```
4. Membuka `urls.py` pada subdirektori `main`, impor fungsi-fungsi yang telah dibuat 
```
from main.views import register, login_user, logout_user
```
5. Menambahkan _path url_ fungsi-fungsi tersebut ke dalam `urlpatterns`
```
...
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
...
```
- [x] Membuat dua akun pengguna dengan masing-masing tiga _dummy data_ menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal. <br>
Agar kedua pengguna hanya dapat melihat item masing-masing, kita perlu merestriksi akses halaman `main`

* Buka `views.py` yang ada pada subdirektori `main` dan tambahkan import `login_required`
```
from django.contrib.auth.decorators import login_required
```
* Menambahkan kode `@login_required(login_url='/login')` di atas fungsi `render_main` agar halaman `main` hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).
```
...
@login_required(login_url='/login')
def render_main(request):
...
```

- [x] Menghubungkan model `Item` dengan `User`
1. Mengimpor _User_ pada berkas _models.py_ yang ada pada subdirektori _main_ 
```
...
from django.contrib.auth.models import User
...
```
2. Menambahkan atribut _User_ pada model `Item`
```
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
3. Memodifikasi beberapa fungsi pada berkas `views.py` di subdirektori `main`:
* fungsi `create_item`
Kita akan mengisi field `user` dengan objek User dari return value `request.user` yang sedang terotorisasi untuk menandakan bahwa objek tersebut dimiliki oleh pengguna yang sedang login.
```
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:render_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```
* fungsi `render_main`
```
def render_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    ...
...
```

4. Menyimpan semua perubahan, dan melakukan migrasi model dengan `python manage.py makemigrations`
5. Melakukan `python manage.py migrate` untuk mengaplikasikan migrasi yang dilakukan pada poin sebelumnya<br>

- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti _username_ dan menerapkan _cookies_ seperti _last login_ pada halaman utama aplikasi.
1. Mengimpor fungsi, class, dan module yang diperlukan pada berkas `views.py` di subdirektori `main`:
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

2. Memodifikasi fungsi `login_user` menjadi seperti berikut:
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:render_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
3. Menambahkan potongan kode `last_login': request.COOKIES['last_login']` ke dalam variabel `context` fungsi `render_main`
```
context = {
        'appname': 'CakeStock',
        'name': request.user.username,
        'class': 'local user',
        'items': items,
        'last_login': request.COOKIES['last_login']
    }
```
4. Memodifikasi fungsi `logout_user` menjadi seperti berikut:
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
5.  Menambahkan potongan kode berikut di antara tabel dan tombol _logout_ di berkas `main.html` untuk menampilkan data _last login_: 
```
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```
</details>

<details>
<summary>Tugas 5</summary>
## Jawaban Pertanyaan 
### Jelaskan manfaat dari setiap _element selector_ dan kapan waktu yang tepat untuk menggunakannya.
Pertanyaan ini rancu karena _element selector_ merujuk pada penggunaan nama tag HTML sebagai selektor. Manfaat setiap _element selector_ berarti
menjelaskan penggunaan selector pada setiap tag HTML(?). Maka diasumsikan maksud pertanyaan ialah _selector_ pada CSS secara umum.
1. Universal Selector (* {}) <br>
Universal selector digunakan untuk memberikan style yang sama pada semua elemen. Selector ini cocok digunakan untuk melakukan reset style atau ketika ingin memberikan style umum pada semua elemen di suatu halaman.
2. ID Selector (#value-id {}) <br>
ID selector digunakan untuk memilih elemen berdasarkan id yang ditentukan. Atribut id bersifat unik dalam satu halaman web. Oleh karena itu, selector ini cocok digunakan ketika ingin memberikan style spesifik pada suatu elemen.
3. Class Selector (.class-name {})<br>
Class selector akan memberikan style ke semua elemen HTML dengan nilai atribut class yang sama. Class selector cocok digunakan ketika kita ingin mengelompokkan beberapa tag agar memiliki style yang sama.
4. Element Selector (p {}) <br>
Element selector digunakan untuk memberikan style ke semua elemen yang memiliki tag HTML yang sama. Element selector cocok digunakan ketika kita ingin memberikan suatu style untuk semua elemen dengan tag yang sama.


###  Jelaskan HTML5 Tag yang kamu ketahui.
1. `<p>` untuk membuat paragraf
2. `<br>` untuk menambahkan baris baru
3. `<div>` untuk mengelompokkan beberapa elemen yang masih merupakan 1 bagian/section.
4. `<table>` untuk membuat tabel dan mengatur elemen-elemen dalam tabel. 
5. `<th>` untuk mendefinisikan table header
6. `<tr>` untuk mendefinisikan table row(baris)
6. `<td>` untuk mendefinisikan table data(dapat dipandang sebagai isi kolom).
7. `<h1> sampai <h6>` untuk membuat header, semakin besar angkanya semakin kecil tulisannya. 
8. `<button>` untuk menambahkan tombol.
9. `<title>` untuk memberi judul halaman web yang akan ditampilkan pada tab browser, dsb.


### Jelaskan perbedaan antara margin dan padding.
* Margin adalah ruang di luar batas elemen. 
Margin dapat dianggap sebagai ruang “eksternal” yang memisahkan suatu elemen dari elemen lain di sekitarnya. Misalnya jika kita memiliki dua kotak yang diletakkan bersebelahan, margin adalah ruang/jarak antara dua kotak tersebut.
* Padding adalah ruang di dalam batas elemen, antara batas elemen dan kontennya. 
Padding dapat dianggap sebagai ruang “internal” yang memberi jarak antara konten elemen (seperti teks) dengan batas elemen itu sendiri. Misalnya jika kita memiliki kotak dengan teks di dalamnya, padding adalah ruang/jarak antara teks dan batas kotak(border).
<br>

### Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
* Tailwind
1. Tailwind CSS membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya.
2. Tailwind CSS memiliki file CSS yang lebih kecil dibandingkan Bootstrap dan hanya akan memuat kelas-kelas utilitas yang ada.
3. Tailwind CSS memiliki memberikan fleksibilitas dan adaptabilitas tinggi terhadap proyek.
4. Tailwind CSS kurang _beginner friendly_ karena memerlukan pemahaman terhadap kelas-kelas utilitas yang tersedia dan bagaimana menggabungkannya untuk mencapai tampilan yang diinginkan.


* Bootstrap
1. Bootstrap menggunakan gaya dan komponen yang telah didefinisikan, sehingga tampilannya sudah jadi dan dapat digunakan secara langsung.
2. Bootstrap memerlukan ukuran file CSS yang lebih besar dibandingkan dengan Tailwind CSS karena banyak komponen yang telah didefinisikan.
3. Bootstrap sering kali menghasilkan tampilan yang lebih konsisten(serupa) di seluruh proyek karena menggunakan komponen yang telah didefinisikan.
4. Bootstrap lebih _beginner friendly_ karena pemula dapat mulai belajar menggunakan komponen yang telah didefinisikan.

Berdasarkan penjelasan di atas, Bootstrap cocok digunakan bagi pemula yang belum berpengalaman dalam desain tampilan atau CSS karena banyak komponen yang bisa langsung digunakan. Sedangkan Tailwind cocok digunakan jika ingin membuat desain web yang tidak monoton, memiliki kontrol penuh atas komponen, dan lebih ringan(ukuran file secara umum lebih kecil).  

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Menambahkan Bootstrap dan Javascript di templates/base.html
```
<head>
    {% block meta %}
        ...
    {% endblock meta %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
```
```
<head>
    ...
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
</head>
```
2. Melakukan kustomisasi desain menggunakan inline style dan internal style sheets. 
</details>

# Tugas 6
## Jawaban Pertanyaan 
### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming. <br>
Pada asynchronous programming, satu tugas tidak harus menunggu tugas lain selesai sebelum bisa mulai dikerjakan. Dengan kata lain, tugas-tugas dapat dieksekusi secara paralel, tidak bergantung pada tugas lain. Dampaknya ketika terdapat suatu operasi yang memerlukan waktu lama, operasi tersebut tidak menghentikan eksekusi program utama sehingga membuat program lebih responsif dan efisien. Asynchronous programming biasanya menggunakan mekanisme seperti _callback function_ dan _promises_ untuk menangani hasil operasi yang perlu waktu lama. 
Penggunaan asynchronous programming bisa lebih kompleks karena adanya mekanisme tersebut. 
Sedangkan pada synchronous programming, tugas dieksekusi satu per satu sesuai urutannya. Proses eksekusi jadi terhenti saat menunggu(mengerjakan) operasi I/O. Pengerjaan tugas juga menunggu pengerjaan tugas lain selesai terlebih dahulu sehingga kurang efisien saat terdapat operasi yang memerlukan waktu lama. Meski demikian, kode synchronous programming akan lebih mudah dipahami karena urutan eksekusinya sudah jelas. 

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini. <br>
Event-driven programming adalah suatu paradigma pemrograman di mana alur eksekusi suatu program dipengaruhi(ditentukan) oleh event-event yang muncul. Artinya suatu program akan menunggu event tertentu untuk muncul sebelum melanjutkan eksekusi. Paradigma ini akan menghasilkan program yang lebih responsif karena program akan menunggu "sesuatu" terjadi, kemudian memberi respon terhadap event tersebut. Event yang dimaksud bisa berupa _mouse click_, _keyboard events_, _mouse hover_, _form events_, _network events_, _window events_, dan masih banyak lagi. <br>
Pada penerapan event-driven programming, kita menentukan kode atau fungsi yang akan dijalankan ketika suatu event terjadi(melakukan event handling). Misalnya kita memiliki tombol di situs web kita yang akan men-trigger AJAX request ketika diklik. Daripada menunggu request tersebut selesai dijalankan, kita bisa membuat suatu event listener yang akan men-trigger `callback function` ketika request tersebut sudah selesai dijalankan. `Callback function` ini yang akan menangani respon dari AJAX request tersebut. Dengan demikian, event-driven programming dapat mendukung eksekusi kode secara asynchronous. <br>
Salah satu contoh penerapan event-driven programming pada tugas ini:<br>
`document.getElementById("button_add").onclick = addItem` <br>
Maksud dari kode tersebut adalah saat element dengan id "button_add" diklik, maka fungsi addItem akan dijalankan.

### Jelaskan penerapan asynchronous programming pada AJAX.
 AJAX bukanlah merupakan sebuah bahasa pemrograman, melainkan sebuah teknologi yang memadukan peramban web (untuk meminta data dari web server) dengan JavaScript dan HTML DOM (untuk menampilkan data). AJAX memungkinkan pengiriman HTTP Request (GET, POST, dll.) ke server secara asinkronus. Penerapan asynchronous programming pada AJAX memungkinkan komunikasi antara browser dan server tanpa perlu me-refresh seluruh halaman web.  Artinya AJAX memungkinkan aplikasi web untuk berkomunikasi dengan server tanpa harus menunggu respon untuk melanjutkan eksekusi perintah berikutnya. <br>
 AJAX dapat menggunakan objek seperti XMLHttpRequest, library jQuery, atau fetch API untuk mengirim dan menerima data secara asinkronus dari server, sambil menjalankan bagian kode lainnya. Dengan demikian, pengguna dapat memiliki pengalaman yang lebih mulus saat menggunakan aplikasi web.

### Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
<br>

1. Fetch API
* Hanya memerlukan JavaScript standar sehingga lebih ringan
* Perlu menulis kode tambahan untuk tugas yang kompleks seperti manipulasi DOM atau animasi
* Menggunakan Promise, lebih modern dan lebih sesuai dengan paradigma asynchronous programming
* Tidak dapat digunakan pada browser lama
* Cocok digunakan untuk aplikasi web modern
2. jQuery
* Memerlukan library eksternal 
* Memiliki berbagai fitur yang dapat mempermudah manipulasi DOM, animasi, event handling, dan sebagainya
* Masih menggunakan `callback pattern`, kurang modern dibandingkan Promise
* Dapat digunakan untuk browser versi lama karena dirancang untuk mendukung berbagai browser
* Cocok digunakan apabila ingin membuat aplikasi web yang dapat dijalankan di berbagai browser(memerlukan kompabilitas yang luas).
<br>
Pada dasarnya, pemilihan antara Fetch API dan jQuery sangat tergantung pada kebutuhan proyek dan preferensi dari developer aplikasi web itu sendiri. Secara umum, kita bisa mengatakan Fetch API adalah pilihan yang lebih baik. Fetch API cocok digunakan untuk mengembangkan aplikasi web modern yang ringan dan memanfaatkan fitur terbaru JavaScript. Selain itu, Fetch API adalah pilihan yang lebih modern dan sesuai dengan perkembangan teknologi web saat ini. Sedangkan jQuery bisa menjadi pilihan yang lebih baik untuk mengembangkan aplikasi web dengan kompabilitas yang luas.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
1. Membuat fungsi `get_item_json` di file `views.py`.
2. Menambahkan path url `get_item_json` ke dalam urlpatterns pada urls.py yang ada pada direktori main.
3. Membuat fungsi `getItems` dan `refreshItems` bagian `<script></script>` pada main.html untuk menampilkan seluruh item secara asinkronus.
4. Membuat fungsi `add_item_ajax` di file `views.py`.
5. Menambahkan path url fungsi tersebut sebagai `create-ajax/` ke dalam urlpatterns pada urls.py yang ada pada direktori main.
6. Menghapus bagian kode tabel yang sudah dibuat sebelumnya, diganti dengan div yang nantinya akan diisi dengan cards saat `refreshItems` dijalankan. 
7. Menambahkan kode untuk mengimplementasikan modal beserta tombol untuk menampilkan modal.
8. Menambahkan fungsi `addItem` untuk membuat form data baru dan mengirimnya ke server.
9. Menambahkan fungsi `onclick` pada button "Add Cake" pada modal sebagai event handler untuk menjalankan fungsi `addItem()` apabila tombol diklik.  
10. Menjalankan command `python manage.py collectstatic` untuk mengumpulkan semua file static ke satu tempat.
11. Melakukan deployment ke PaaS PBP Fasilkom UI.
