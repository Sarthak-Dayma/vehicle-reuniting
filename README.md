# VehicleReunite - Anonymous Vehicle Monitoring System

VehicleReunite is a web application that helps reunite lost vehicles with their owners. The system allows people to report found vehicles and register lost vehicles, with automatic matching based on license plate numbers and email notifications when matches are found.

## Features

- Report found vehicles with details and photos
- Register lost vehicles with owner contact information
- Automatic matching of vehicles based on license plate numbers
- Email notifications when matches are found
- Dashboard to view and search all reported vehicles
- Responsive design that works on mobile and desktop

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Backend**: Django 4.2
- **Database**: SQLite (default), can be configured for PostgreSQL or MySQL
- **Email**: Configurable for SMTP or console output

## Installation

1. Clone the repository:
   \`\`\`
   git clone https://github.com/yourusername/vehicle-reunite.git
   cd vehicle-reunite
   \`\`\`

2. Create a virtual environment and activate it:
   \`\`\`
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   \`\`\`

3. Install dependencies:
   \`\`\`
   pip install -r requirements.txt
   \`\`\`

4. Run migrations:
   \`\`\`
   python manage.py migrate
   \`\`\`

5. Create a superuser (admin):
   \`\`\`
   python manage.py createsuperuser
   \`\`\`

6. Run the development server:
   \`\`\`
   python manage.py runserver
   \`\`\`

7. Visit http://127.0.0.1:8000/ in your browser

## Fixing Database Errors

If you encounter the error "no such table: vehicles_foundvehicle" or similar database errors, follow these steps:

1. Run the database fix script:
   \`\`\`
   python fix_database.py
   \`\`\`

2. If the error persists, try these manual steps:
   \`\`\`
   # Remove the database file
   rm db.sqlite3
   
   # Remove migration files (keep __init__.py)
   rm vehicles/migrations/0*.py
   
   # Create new migrations
   python manage.py makemigrations vehicles
   
   # Apply migrations
   python manage.py migrate
   
   # Create a superuser
   python manage.py createsuperuser
   \`\`\`

3. Restart the development server:
   \`\`\`
   python manage.py runserver
   \`\`\`

## Configuration

### Email Settings

By default, the application uses the console email backend for development. To configure SMTP for production, update the settings in `vehicle_monitoring/settings.py`:

\`\`\`python
# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'daymasarthak2@gmail.com'
EMAIL_HOST_PASSWORD = 'Sarthak2112003$@#'
DEFAULT_FROM_EMAIL = 'noreply@vehiclereunite.com'
