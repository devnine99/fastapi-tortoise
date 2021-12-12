import os

from main import create_app

os.environ.setdefault('SETTINGS_MODULE', 'config.settings.local')

app = create_app()
