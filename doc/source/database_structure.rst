Database Structure and Data Models
===================================

The OC-Lettings application uses a SQLite database with the following key models:

### Address Model

The `Address` model represents the address of a property and includes the following fields:
- **number**: A positive integer representing the street number (max value: 9999).
- **street**: A string representing the street name (max length: 64 characters).
- **city**: A string representing the city name (max length: 64 characters).
- **state**: A string representing the state (2 characters, validated for length).
- **zip_code**: A positive integer representing the postal code (max value: 99999).
- **country_iso_code**: A string representing the ISO code of the country (3 characters, validated for length).

### Letting Model

The `Letting` model represents a property listing and includes the following fields:
- **title**: A string representing the title of the property (max length: 256 characters).
- **address**: A one-to-one relationship with the `Address` model, linking each property to its address.

### Profile Model

The `Profile` model stores additional information about users and includes the following fields:
- **user**: A one-to-one relationship with the Django `User` model, linking each profile to a specific user.
- **favorite_city**: A string representing the user's favorite city (max length: 64 characters, can be blank).

### Database Schema

The database schema includes the following tables:
- **addresses**: Stores address information for properties.
- **lettings**: Stores property details, including titles and associated addresses.
- **profiles**: Stores user profiles, including favorite cities.

This structure allows for efficient data management and retrieval, ensuring a smooth user experience.