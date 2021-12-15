from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from blog.models import Post, Category, Comment


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.post_list_url = reverse('post_list')
        self.post_detail_url = reverse('post_detail', args=[1])
        self.main_menu_url = reverse('main_menu')
        self.register_url = reverse('register')
        self.category_url = reverse('category', args=['WoT'])
        self.hello_page_url = reverse('hello_page')
        self.post_new_url = reverse('post_new')
        self.login_page_url = reverse('login')
        self.user = self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        self.profile_url = reverse('profile')
        self.post1 = Post.objects.create(
            pk=1,
            author=self.user,
        )
        self.post_edit_url = reverse('post_edit', args=[1])

    def test_post_list_GET(self):
        response = self.client.get(self.post_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_detail_GET(self):
        response = self.client.get(self.post_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_profile_GET(self):
        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_files/profile.html')

    def test_main_menu_GET(self):
        response = self.client.get(self.main_menu_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/main_menu.html')

    def test_category_GET(self):
        response = self.client.get(self.category_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/categories.html')

    def test_hello_page_GET(self):
        response = self.client.get(self.hello_page_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/hello.html')

    def test_register_GET(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_post_edit_GET(self):
        response = self.client.get(self.post_edit_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_edit.html')

    def test_post_new_GET(self):
        response = self.client.get(self.post_new_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_edit.html')

    def test_login_page_GET(self):
        response = self.client.get(self.login_page_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
