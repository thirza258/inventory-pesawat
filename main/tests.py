from django.test import TestCase, Client

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)
    
    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_context_nama_is_right(self):
        response = Client().get('/main/')
        self.assertEqual(response.context['Nama'], 'Thirza Ahmad Tsaqif')

    def test_context_class_is_right(self):
        response = Client().get('/main/')
        self.assertEqual(response.context['Class'], 'PBP E')
    
    def test_context_nama_aplikasi_is_right(self):
        response = Client().get('/main/')
        self.assertEqual(response.context['Nama_Aplikasi'], 'Inventory RPG')