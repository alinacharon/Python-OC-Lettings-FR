import pytest
from django.contrib.auth.models import User
from django.template import loader
from django.test import Client
from django.urls import reverse

from profiles.models import Profile


@pytest.mark.django_db
class TestProfileModel:
    def test_profile_creation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        profile = Profile.objects.create(user=user, favorite_city='Paris')

        assert Profile.objects.count() == 1
        assert str(profile) == 'testuser'
        assert profile.favorite_city == 'Paris'

    def test_profile_deletion_cascades(self):
        user = User.objects.create_user(username='testuser', password='12345')
        Profile.objects.create(user=user, favorite_city='London')

        user.delete()
        assert Profile.objects.count() == 0


@pytest.mark.django_db
class TestProfileViews:
    def setup_method(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='john', password='12345')
        self.user2 = User.objects.create_user(username='jane', password='54321')

        Profile.objects.create(user=self.user1, favorite_city='New York')
        Profile.objects.create(user=self.user2, favorite_city='San Francisco')

    def test_profiles_index_view(self):
        response = self.client.get(reverse('profiles_index'))

        assert response.status_code == 200
        assert 'profiles_list' in response.context
        assert len(response.context['profiles_list']) == 2

        template = loader.get_template('profiles/index.html')
        assert template.template.name.endswith('profiles/index.html')

    def test_profile_detail_view(self):
        response = self.client.get(reverse('profile', kwargs={'username': 'john'}))

        assert response.status_code == 200
        assert 'profile' in response.context
        assert response.context['profile'].user.username == 'john'

        template = loader.get_template('profiles/profile.html')
        assert template.template.name.endswith('profiles/profile.html')

    def test_profile_view_with_nonexistent_user(self):
        response = self.client.get(reverse('profile', kwargs={'username': 'nonexistent'}))
        assert response.status_code == 404
