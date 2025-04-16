#!/usr/bin/env python
"""
This script helps fix the 'no such table: vehicles_foundvehicle' error
by ensuring the database tables are properly created.
"""
import os
import sys
import subprocess

def main():
    print("Starting database fix process...")
    
    # Check if Django is installed
    try:
        import django
        print(f"Django version {django.get_version()} is installed.")
    except ImportError:
        print("Django is not installed. Please run: pip install -r requirements.txt")
        return
    
    # Make migrations
    print("\nCreating migrations...")
    try:
        subprocess.run([sys.executable, "manage.py", "makemigrations", "vehicles"], check=True)
    except subprocess.CalledProcessError:
        print("Error creating migrations. Please check your models.")
        return
    
    # Apply migrations
    print("\nApplying migrations...")
    try:
        subprocess.run([sys.executable, "manage.py", "migrate"], check=True)
    except subprocess.CalledProcessError:
        print("Error applying migrations.")
        return
    
    # Check if database exists
    if os.path.exists("db.sqlite3"):
        print("\nDatabase file exists.")
    else:
        print("\nWarning: Database file (db.sqlite3) not found.")
    
    print("\nDatabase fix process completed.")
    print("\nIf you're still seeing the error, try these steps:")
    print("1. Delete the db.sqlite3 file (if it exists)")
    print("2. Delete all files in vehicles/migrations/ except __init__.py")
    print("3. Run this script again")
    print("\nThen restart your Django server with: python manage.py runserver")

if __name__ == "__main__":
    main()
