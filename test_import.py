import sys
import os

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(
                os.path.dirname(__file__),
                'src')))

print("sys.path:", sys.path)

try:
    print("Import successful")
except ImportError as e:
    print(f"Import failed: {e}")
