"""
ASGI config for vehicle_monitoring project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vehicle_monitoring.settings')

application = get_asgi_application()
