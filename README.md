# Django Recipe Website

A feature-rich recipe management web application built with Django. This platform allows users to create, share, and discover cooking recipes with a clean, responsive interface.

![Django Recipe Website](https://recipes.keepsolve.ru/static/img/logo.png)

## Features

- **User Authentication**: Register, login, and profile management
- **Recipe Management**: Create, edit, and delete your own recipes
- **Recipe Browsing**: Discover recipes by categories, search, or browse the homepage
- **Image Upload**: Add images to recipes to showcase your culinary creations
- **Responsive Design**: Works on desktops, tablets, and mobile devices
- **Multi-language Support**: Properly handles Cyrillic and other non-ASCII characters

## Technologies Used

- **Backend**: Django 5.2
- **Database**: PostgreSQL
- **Frontend**: Bootstrap 4, JavaScript
- **Deployment**: Nginx, Gunicorn, Supervisor
- **Security**: SSL/TLS with Let's Encrypt

## Installation

### Local Development

1. Clone the repository:

`bash git clone https://github.com/yourusername/recipe-website.git cd recipe-website`

2. Create and activate a virtual environment:

`bash python -m venv venv source venv/bin/activate # On Windows: venv\Scripts\activate`

3. Install dependencies:
`bash pip install -r requirements.txt`

4. Run migrations:

`bash python manage.py migrate`

5. Create a superuser:

`bash python manage.py createsuperuser`

6. Run the development server:

`bash python manage.py runserver`

7. Access the site at http://127.0.0.1:8000

### Production Deployment

For production deployment on Ubuntu, follow these steps:

1. Set up a server with Ubuntu 24.04
2. Install required packages:

`bash apt update && apt upgrade -y apt install -y python3 python3-pip python3-dev python3-venv apt install -y postgresql postgresql-contrib apt install -y nginx supervisor`

3. Set up PostgreSQL database:

`bash sudo -u postgres psql CREATE DATABASE recipe_db; CREATE USER recipe_user WITH PASSWORD 'your_secure_password'; GRANT ALL PRIVILEGES ON DATABASE recipe_db TO recipe_user; \c recipe_db GRANT ALL ON SCHEMA public TO recipe_user; \q`

4. Clone and configure the project (follow detailed steps in deployment guide)

5. Set up Gunicorn with Supervisor and configure Nginx

6. Set up SSL with Let's Encrypt:

`bash apt install -y certbot python3-certbot-nginx certbot --nginx -d yourdomain.com`

## Project Structure

recipe_website/ ├── manage.py ├── recipe_project/ │ ├── init.py │ ├── settings.py │ ├── urls.py │ └── wsgi.py ├── recipes/ │ ├── admin.py │ ├── forms.py │ ├── models.py │ ├── urls.py │ └── views.py ├── users/ │ ├── admin.py │ ├── forms.py │ ├── models.py │ ├── signals.py │ └── views.py ├── static/ │ ├── css/ │ └── js/ ├── media/ │ └── recipe_images/ ├── templates/ │ ├── base.html │ ├── recipes/ │ └── users/ └── requirements.txt

## Usage

### Creating a Recipe

1. Log in to your account
2. Click on "New Recipe" in the navigation bar
3. Fill in the recipe details:
   - Title
   - Description
   - Ingredients
   - Instructions
   - Preparation time
   - Categories
   - Image (optional)
4. Click "Submit" to publish your recipe

### Managing Your Recipes

From your profile page, you can:
- View all your recipes
- Edit recipes
- Delete recipes

## Common Issues and Solutions

### Unicode/Cyrillic Character Support (solved)
The application uses a custom slugify function to properly handle Cyrillic and other non-ASCII characters in recipe titles.

### Image Upload Issues (solved)
If images aren't displaying, check:
- Media directory permissions: `chmod 755 media/`
- Nginx configuration for media files
- Django settings for MEDIA_URL and MEDIA_ROOT

### 500 Server Errors (solved)
Common causes:
- Database connection issues
- Permission problems with media uploads
- Incorrect path settings

## Security Features

The site implements several security best practices:
- HTTPS with modern TLS configuration
- Secure HTTP headers
- CSRF protection
- XSS protection
- Proper permission model
- Password hashing with PBKDF2

## License

This project is licensed under the AGPL License

## Contributing

Contributions are welcome, but I'm tired please kill me (its a joke)

## Acknowledgments

- Django framework and community
- Bootstrap for the responsive design

---

by Alexander Lemport with love