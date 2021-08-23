import sys, os
sys.path.append('./src')
from src.app import App

with App() as app:
    app.randomize()