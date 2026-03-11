import sys
import os

# thêm root project vào python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# import FastAPI app
from backend.main import app
