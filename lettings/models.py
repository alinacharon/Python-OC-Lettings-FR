from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a postal address with fields for number, street, city, state, zip code,
    and country ISO code.
    Used to store address details for lettings or other entities.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Returns a string representation of the address in the format:
        'number street'.
        """
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name = "address"
        verbose_name_plural = "addresses"


class Letting(models.Model):
    """
    Represents a letting, which includes a title and a reference to an address.
    Each letting is associated with a unique address.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the letting, which is its title.
        """
        return self.title
