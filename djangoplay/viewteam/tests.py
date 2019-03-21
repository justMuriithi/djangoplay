from django.test import TestCase
from .models import ViewTeam
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ModelTestCase(TestCase):
    """This class defines the test suite for the ViewTeam model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.ViewTeam_name = "Write world class code"
        self.ViewTeam = ViewTeam(name=self.ViewTeam_name)

    def test_model_can_create_a_ViewTeam(self):
        """Test the ViewTeam model can create ViewTeam."""
        old_count = ViewTeam.objects.count()
        self.ViewTeam.save()
        new_count = ViewTeam.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.viewteam_data = {
            'name': 'Name',
            'github': 'http://www.someurl.com',
            'funfact': 'funfact1'}
        self.res = self.client.post(
            reverse('viewteam-list'),
            self.viewteam_data,
            format="json")

    def test_api_can_create_a_teamlist(self):
        """Test the api has team member creation capability."""
        self.assertEqual(self.res.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_teamlist(self):
        """Test the api can get a teamlist."""
        res = self.client.get(
            '/viewteam/1/', format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_update_teamlist(self):
        """Test the api can update a given team member."""
        change_viewteam = {'name': 'Something new',
                           'github': 'http://www.someurl.com',
                           'funfact': 'funfact2'}
        res = self.client.put(
            '/viewteam/1/', change_viewteam, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_viewteam(self):
        """Test the api can delete a team member."""
        res = self.client.delete(
            '/viewteam/1/', format="json")
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)
