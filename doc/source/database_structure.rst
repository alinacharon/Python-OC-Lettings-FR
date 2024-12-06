Database Structure and Data Models
===================================

The OC-Lettings application uses a SQLite database with the following key models:


### 1. Address Model
**Model Name:** `Address`
**Database Table:** `adresses`

#### Fields
| Field Name | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| `number` | Positive Integer | Max Value: 9999 | Street number |
| `street` | Character | Max Length: 64 | Street name |
| `city` | Character | Max Length: 64 | City name |
| `state` | Character | Length: 2 | State abbreviation |
| `zip_code` | Positive Integer | Max Value: 99999 | Postal code |
| `country_iso_code` | Character | Length: 3 | Country ISO code |

#### Validation Rules
- Street number must be a positive integer ≤ 9999
- State must be exactly 2 characters long
- Country code must be exactly 3 characters long

#### String Representation
Returns: `"{number} {street}"`

### 2. Letting Model
**Model Name:** `Letting`

#### Fields
| Field Name | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| `title` | Character | Max Length: 256 | Title of the letting |
| `address` | One-to-One Relationship | Cascading Delete | Unique address associated with the letting |

#### Relationships
- **Address Relationship:** One-to-One with `Address` model
- When the associated `Address` is deleted, the `Letting` is also deleted (CASCADE)

#### String Representation
Returns: `"{title}"`

### 3. Profile Model
**Model Name:** `Profile`

#### Fields
| Field Name | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| `user` | One-to-One Relationship | Cascading Delete | Associated Django User |
| `favorite_city` | Character | Optional, Max Length: 64 | User's favorite city |

#### Relationships
- **User Relationship:** One-to-One with Django's built-in `User` model
- When the associated `User` is deleted, the `Profile` is also deleted (CASCADE)

#### String Representation
Returns: `"{username}"`

## Model Relationships Diagram

```
User (Django Auth) ---(1:1)--- Profile
             |
             |
             v
           Address ---(1:1)--- Letting
```

## Key Design Considerations
1. Use of One-to-One relationships for User and Letting models
2. Strict validation on address fields
3. Cascading delete to maintain referential integrity

## Recommended Database Practices
- Ensure unique constraints are properly implemented
- Validate data at both model and form levels
- Use database migrations for schema changes