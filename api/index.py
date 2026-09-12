import sys
import os

# Add backend directory to sys.path so app modules can be resolved
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

from app.main import app  # noqa: E402
