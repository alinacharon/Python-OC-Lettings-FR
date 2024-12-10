Introduction
============

OC-Lettings is a comprehensive property management application designed to streamline operations and enhance efficiency for property owners and managers. 
This user-friendly platform offers tools to facilitate the listing and management of properties.

Core Data Models

OC-Lettings is built on a solid foundation of Django models, ensuring structured and efficient data management. Below are the key models used in the application:

1. Address

The Address model captures essential details of a postal address, including:
	•	Number: The house or building number.
	•	Street: The street name.
	•	City: The name of the city.
	•	State: A state abbreviation.
	•	Zip Code: A numerical zip code.
	•	Country ISO Code: An ISO code representing the country.

This model ensures accurate storage of address details, crucial for identifying property locations. 

2. Letting

The Letting model links properties to their respective addresses and includes:
	•	Title: A descriptive title for the property.
	•	Address: A one-to-one relationship with the Address model.


3. Profile

The Profile model extends the built-in Django User model, providing additional user-specific information:
	•	User: A one-to-one relationship with the Django User model, ensuring each profile is uniquely tied to a user.
	•	Favorite City: A user’s preferred city, stored as an optional field.


Key Features

	•	Scalability: Modular design with structured models allows easy expansion of functionalities.
	•	Efficiency: Centralized management of properties, addresses, and user profiles optimizes operations.
	•	Customizability: The models can be easily extended or modified to meet specific business requirements.

This robust architecture ensures OC-Lettings is not only a tool for managing properties but also a flexible platform adaptable to diverse use cases in the real estate industry.
