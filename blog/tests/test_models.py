from django.contrib.auth.models import User
from django.test import TestCase, Client
from blog.models import Post


class TestAddedModelsFunc(TestCase):
    def setUp(self):
        self.user = self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

        self.post1 = Post.objects.create(
            pk=1,
            author=self.user,
            category='WoT'
        )

    def test_like_count(self):
        likes = self.post1.likes.add(self.user)
        total_likes = self.post1.total_likes()

        self.assertEquals(total_likes, 1)
