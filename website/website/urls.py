"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.test import TestCase

from django.test import Client

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]


class ExamplelGetTest(TestCase):

    @classmethod
    def setUpClass(self):
        # creating instance of a client.
        self.client = Client()

    def test_getLogin(self):
        # Issue a GET request.
        response = self.client.get('/application/login/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_addAccount(self):
            response = self.client.post('/', {'username': 'name', 'password': 'pass',
            'email':''})

            self.assertEqual(response.status_code, 302)
