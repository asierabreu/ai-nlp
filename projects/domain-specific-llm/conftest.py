"""Configure pytest path for this project."""
import sys
from pathlib import Path

# Add the project root to sys.path so src/ imports work
sys.path.insert(0, str(Path(__file__).parent))
