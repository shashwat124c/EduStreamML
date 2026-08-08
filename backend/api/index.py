import sys
import os

# Add the parent directory (backend/) to sys.path so app.py can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
