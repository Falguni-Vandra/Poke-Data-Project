import sys
import os

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

print("sys.path:", sys.path)

try:
    from storage import store_data_to_sqlite
    print("Import successful")
except ImportError as e:
    print(f"Import failed: {e}")
