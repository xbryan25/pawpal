
-- Create the shelters table
CREATE TABLE IF NOT EXISTS shelters(
shelter_id BINARY(16),
name VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL,
address VARCHAR(255) NOT NULL,
phone_number VARCHAR(11) NOT NULL,
created_at DATETIME NOT NULL,

UNIQUE KEY UC_phone_number (phone_number),

PRIMARY KEY (shelter_id)
);

-- Create the users table
CREATE TABLE IF NOT EXISTS users(
user_id BINARY(16) NOT NULL,
name VARCHAR(255) NOT NULL,
gender ENUM('male','female','others', 'prefer not to say') NOT NULL,
address VARCHAR(255) NOT NULL,
phone_number VARCHAR(11) NOT NULL,
birth_date DATE NOT NULL,
email VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL,
role ENUM('adopter', 'shelter staff', 'admin') NOT NULL,
profile_url VARCHAR(255) NOT NULL,
shelter_id BINARY(16),

PRIMARY KEY (user_id),
UNIQUE KEY UC_phone_number (phone_number),
UNIQUE KEY UC_email (email),

CONSTRAINT fk_users_shelter_id FOREIGN KEY (shelter_id) REFERENCES shelters(shelter_id)
);

-- Create the species table
CREATE TABLE IF NOT EXISTS species(
species_id BINARY(16) NOT NULL,
species_name VARCHAR(30) NOT NULL,

PRIMARY KEY (species_id),
UNIQUE KEY UC_species_name (species_name)
);

-- Create the breed table
CREATE TABLE IF NOT EXISTS breeds(
breed_id BINARY(16) NOT NULL,
breed_name VARCHAR(30) NOT NULL,
species_id BINARY(16) NOT NULL,

PRIMARY KEY (breed_id),
UNIQUE KEY UC_breed_name (breed_name),

CONSTRAINT fk_species_id FOREIGN KEY (species_id) REFERENCES species(species_id)
);

-- Create the pets table

CREATE TABLE IF NOT EXISTS pets(
pet_id BINARY(16) NOT NULL,
name VARCHAR(255) NOT NULL,
birth_date DATE NOT NULL,
sex ENUM('male','female') NOT NULL,
status ENUM('available','pending', 'adopted', 'unavailable') NOT NULL,
description VARCHAR(255) NOT NULL,
shelter_id BINARY(16) NOT NULL,
breed_id BINARY(16) NOT NULL,

PRIMARY KEY (pet_id),

CONSTRAINT fk_pets_shelter_id FOREIGN KEY (shelter_id) REFERENCES shelters(shelter_id),
CONSTRAINT fk_breed_id FOREIGN KEY (breed_id) REFERENCES breeds(breed_id)
);

-- Create the adoption_applications table

CREATE TABLE IF NOT EXISTS adoption_applications(
aa_id BINARY(16) NOT NULL,
status ENUM('approved', 'rejected', 'pending') NOT NULL,
application_date DATETIME NOT NULL,
decision_date DATETIME NULL,
user_id BINARY(16) NOT NULL,
pet_id BINARY(16) NOT NULL,

PRIMARY KEY (aa_id),

CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(user_id),
CONSTRAINT fk_adoption_applications_pet_id FOREIGN KEY (pet_id) REFERENCES pets(pet_id)
);

-- Create the pet_images table

CREATE TABLE IF NOT EXISTS pet_images(
pet_image_id BINARY(16) NOT NULL,
image_url VARCHAR(255) NOT NULL,
uploaded_at DATETIME NOT NULL,
sort_order INT NOT NULL,
pet_id BINARY(16) NOT NULL,

PRIMARY KEY (pet_image_id),

CONSTRAINT fk_pet_images_pet_id FOREIGN KEY (pet_id) REFERENCES pets(pet_id)
);

-- Create the shelter_images_table

CREATE TABLE IF NOT EXISTS shelter_images(
shelter_image_id BINARY(16) NOT NULL,
image_url VARCHAR(255) NOT NULL,
uploaded_at DATETIME NOT NULL,
sort_order INT NOT NULL,
shelter_id BINARY(16) NOT NULL,

PRIMARY KEY (shelter_image_id),

CONSTRAINT fk_shelter_images_shelter_id FOREIGN KEY (shelter_id) REFERENCES shelters(shelter_id)
);



