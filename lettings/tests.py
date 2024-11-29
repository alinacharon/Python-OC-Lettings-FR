import pytest
from django.test import Client
from django.urls import reverse

from lettings.models import Address, Letting


@pytest.mark.django_db
class TestAddressModel:
    def test_address_creation(self):
        address = Address.objects.create(
            number=123,
            street='Main St',
            city='New York',
            state='NY',
            zip_code=12345,
            country_iso_code='USA'
        )

        assert str(address) == '123 Main St'
        assert Address.objects.count() == 1


@pytest.mark.django_db
class TestLettingModel:
    def test_letting_creation(self):
        address = Address.objects.create(
            number=456,
            street='Oak Rd',
            city='San Francisco',
            state='CA',
            zip_code=94122,
            country_iso_code='USA'
        )

        letting = Letting.objects.create(
            title='Beautiful Apartment',
            address=address
        )

        assert str(letting) == 'Beautiful Apartment'
        assert Letting.objects.count() == 1
        assert letting.address == address


@pytest.mark.django_db
class TestLettingsViews:
    def setup_method(self):
        self.client = Client()

        # Create addresses
        self.address1 = Address.objects.create(
            number=123,
            street='Main St',
            city='New York',
            state='NY',
            zip_code=12345,
            country_iso_code='USA'
        )
        self.address2 = Address.objects.create(
            number=456,
            street='Oak Rd',
            city='San Francisco',
            state='CA',
            zip_code=94122,
            country_iso_code='USA'
        )

        # Create lettings
        self.letting1 = Letting.objects.create(
            title='Beautiful Apartment',
            address=self.address1
        )
        self.letting2 = Letting.objects.create(
            title='Cozy Loft',
            address=self.address2
        )

    def test_lettings_index_view(self):
        response = self.client.get(reverse('lettings_index'))

        assert response.status_code == 200
        assert 'lettings_list' in response.context
        assert len(response.context['lettings_list']) == 2

    def test_letting_detail_view(self):
        response = self.client.get(reverse('letting', kwargs={'letting_id': self.letting1.id}))

        assert response.status_code == 200
        assert 'title' in response.context
        assert response.context['title'] == 'Beautiful Apartment'
        assert response.context['address'] == self.address1

    def test_letting_view_with_nonexistent_letting(self):
        with pytest.raises(Exception):
            self.client.get(reverse('letting', kwargs={'letting_id': 9999}))


@pytest.mark.django_db
class TestLettingsURLs:
    def test_lettings_index_url(self):
        path = reverse('lettings_index')
        assert path == '/lettings/'

    def test_letting_detail_url(self):
        letting = Letting.objects.create(
            title='Test Letting',
            address=Address.objects.create(
                number=123,
                street='Test St',
                city='Test City',
                state='TS',
                zip_code=12345,
                country_iso_code='TST'
            )
        )
        path = reverse('letting', kwargs={'letting_id': letting.id})
        assert path == f'/lettings/lettings/{letting.id}/'
