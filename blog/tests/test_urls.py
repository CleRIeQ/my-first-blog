from unittest import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import main_menu, profile, hello_page, post_detail, post_new, post_edit, register
from blog.views import category_view, login_user, post_list


class UrlResolveTestCase(SimpleTestCase):
    def test_main_menu_url(self):
        url = reverse('main_menu')
        self.assertEquals(resolve(url).func, main_menu)

    def test_profile_url(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_hello_page_url(self):
        url = reverse('hello_page')
        self.assertEquals(resolve(url).func, hello_page)

    def test_post_new(self):
        url = reverse('post_new')
        self.assertEquals(resolve(url).func, post_new)

    def test_post_detail_url(self):
        url = reverse('post_detail', args=[1])
        self.assertEquals(resolve(url).func, post_detail)

    def test_post_edit_url(self):
        url = reverse('post_edit', args=[1])
        self.assertEquals(resolve(url).func, post_edit)

    def test_register_url(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_like_view_url(self):
        url = reverse('post_detail', args=[1])
        self.assertEquals(resolve(url).func, post_detail)

    def test_category_url(self):
        url = reverse('category', args=['WoT'])
        self.assertEquals(resolve(url).func, category_view)

    def test_post_list_url(self):
        url = reverse('post_list')
        self.assertEquals(resolve(url).func, post_list)

    # def test_login_page_url(self):
        # url = reverse('login')
        # self.assertEquals(resolve(url).func, login_user)

# set DJANGO_SETTINGS_MODULE=mysite.settings
