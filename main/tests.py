from django.test import TestCase, Client
from main.models import Item


class mainTest(TestCase):
    def setUp(self):
        Item.objects.create(name = "eggtart", amount = 10, description = "small circular tarts of flaky pastry, filled with a smooth, lightly sweetened egg custard.", price = 7000)
        Item.objects.create(name = "blackforest", amount = 2, description = "rich chocolate cake layers combined with fresh cherries, cherry liqueur, and a simple whipped cream frosting.", price = 200000)

    #tes apakah benar ada 2 buah objek Item yang telah dibuat
    def test_total_object(self):
        hitungjumlah = Item.objects.all().count()
        self.assertEqual(hitungjumlah,2)

    #tes apakah objek Item dengan nama eggtart dan blackforest berhasil dimasukkan ke database
    def test_item_created(self):
        self.assertTrue(Item.objects.filter(name="eggtart").exists())
        self.assertTrue(Item.objects.filter(name="blackforest").exists())

    #tes untuk mengecek apakah path URL /main/ dapat diakses.
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    #tes untuk mengecek apakah halaman /main/ di-render menggunakan template main.html.
    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    