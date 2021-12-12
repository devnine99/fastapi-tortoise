import os

os.environ.setdefault('SETTINGS_MODULE', 'config.settings.local')

from app.main import create_app
app = create_app()
