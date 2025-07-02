# E-Commerce Website Repository

Welcome to the Johnnys Store / E-Commerce Website Repository! This repository contains the source code and documentation for an e-commerce website, including the main project files, cart application, store application, media files, and project documentation.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository hosts the codebase for an e-commerce website, providing a platform for users to browse products, add items to their cart, and make purchases. It includes the main project files, cart application, store application, media files for product images, and project documentation.

## Project Structure

The project structure is organized as follows:

- **Main File:**
  - Contains the main project code and files.
  
- **Cart File:**
  - Contains the source code for the cart application of the website.

- **E-Commerce Store:**
  - Backend of the website responsible for managing products, orders, and user authentication.

- **/media/images:**
  - Static directory holding all product images.

- **Store Application:**
  - Application responsible for serving the front-end store interface to users.

- **Documentation:**
  - Contains project documentation and diagrams:
    - Project Write-Up (project_writeup.pdf)
    - README (README.md)
    - State Machine Diagram (state_machine_diagram.pdf)
    - UML Shopping Cart Diagram (uml_shopping_cart_diagram.pdf)
    - License (LICENSE)

## Usage

Feel free to use the code and resources in this repository for reference, learning, or building upon for your own e-commerce projects. You can explore the project structure, examine the source code, and utilize the documentation to understand the functionality and implementation details.
To run the Django Python project:

1. **Clone the Repository:** First, clone the repository containing your Django project onto your local machine.

   ```bash
   git clone https://github.com/JUNE8UG/Johnnys-Store.git
   ```
Navigate to the Project Directory: Move into the directory where your Django project is located.

  ```bash
  cd Johnnys-Store
  ```
Install Requirements: Install the required dependencies specified in the requirements.txt file. It's recommended to set up a virtual environment for your project to manage dependencies.

  ```
  pip install -r requirements.txt
  ```
Run Migrations: Apply any database migrations to set up the database schema.

  ```
  python manage.py migrate
  ```
Create a Superuser (Optional): If your project includes user authentication or administration, create a superuser account to access the Django admin interface.
  ```
  python manage.py createsuperuser
  ```
Run the Development Server: Start the Django development server to run your project locally.
  ```
  python manage.py runserver
  ```
Access the Website: Open a web browser and navigate to the URL provided by the development server (usually http://127.0.0.1:8000/) to access your Django project.

Access the Django Admin Interface (Optional): If you created a superuser, you can access the Django admin interface by navigating to http://127.0.0.1:8000/admin/ and logging in with your superuser credentials. From there, you can manage users, content, and other aspects of your Django project.

Remember to consult the specific documentation or README file provided with your Django project for any additional setup instructions or project-specific details. Additionally, ensure that you have Python and Django installed on your system before running the project.

## Contributing

If you would like to contribute to this repository, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.

Your contributions are welcome and appreciated!

## License

This repository is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code and documentation for both personal and commercial purposes.

Happy e-commerce development!
