from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from blog.models import Post,Category
from django.contrib.auth.models import User


class PostTests(APITestCase):

    def test_view_posts(self):

        url = reverse('blog_Api:listcreate')
        response=self.client.get(url,format='json')
        self.assertEqual(response.stauts_code,status.HTTP_200_OK)



# Create your tests here.
