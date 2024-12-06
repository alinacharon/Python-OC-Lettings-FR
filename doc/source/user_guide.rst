User Guide
============================================

## Overview
The application is a Django-based web platform for managing property lettings and user profiles. This guide provides detailed information on using the application's features.

## Key Features

### 1. Lettings Management
- Browse all property listings
- View detailed information about specific properties

### 2. User Profiles
- View list of all user profiles
- Access individual profile details
- See user-specific information

## Application Structure

### Models

#### 1. Address
Represents a physical address with the following attributes:
- Street number
- Street name
- City
- State (2-letter code)
- ZIP code
- Country ISO code

#### 2. Letting
Represents a property listing with:
- Title
- Associated address

#### 3. User Profile
- Linked to Django's built-in User model
- Optional favorite city field

## Use Cases

### Scenario 1: Browsing Lettings
1. Navigate to `/lettings/`
2. View a list of all available property listings
3. See basic information for each letting

### Scenario 2: Viewing Specific Letting
1. From the listings page, click on a specific property
2. Navigate to `/lettings/{letting_id}/`
3. View detailed information about the selected property

### Scenario 3: Exploring User Profiles
1. Navigate to `/profiles/`
2. View a list of all user profiles
3. Click on a specific username to see detailed profile information

### Scenario 4: Viewing Individual Profile
1. From the profiles list, select a specific user
2. Navigate to `/profiles/{username}/`
3. View detailed information about the selected user profile

## Profiles Functionality Details

### Profiles Index View
- Endpoint: `/profiles/`
- Displays a comprehensive list of all user profiles
- Retrieves all Profile objects from the database
- Renders the list on the 'profiles/index.html' template

### Individual Profile View
- Endpoint: `/profiles/{username}/`
- Retrieves profile by username
- Handles scenarios:
  - Successful profile retrieval
  - Non-existent profile (404 error)
- Integrates with Sentry for error tracking

## Technical Specifications

### URL Patterns
Lettings:
- `/lettings/` - Listings index
- `/lettings/{id}/` - Individual letting details

Profiles:
- `/profiles/` - Profiles index
- `/profiles/{username}/` - Individual profile details

### Error Handling
- 404 error for non-existent lettings or profiles
- Sentry integration for error tracking and logging
