import sys
import os

# Ensure backend directory is in the Python search path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app import app
