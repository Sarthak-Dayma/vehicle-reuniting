#!/usr/bin/env python
"""
Script to apply the new migration for additional vehicle fields
"""
import os
import sys
import subprocess

def main():
    print("Applying migration for new vehicle fields...")
    
    try:
        # Make migrations for the new fields
        print("Creating migrations...")
        subprocess.run([sys.executable, "manage.py", "makemigrations", "vehicles"], check=True)
        
        # Apply migrations
        print("Applying migrations...")
        subprocess.run([sys.executable, "manage.py", "migrate"], check=True)
        
        print("Migration completed successfully!")
        print("\nNew fields added to Lost Vehicle form:")
        print("- Year")
        print("- VIN/Chassis Number")
        print("- Engine Number")
        print("\nYou can now restart your Django server.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error during migration: {e}")
        print("Please check your models and try again.")

if __name__ == "__main__":
    main()
