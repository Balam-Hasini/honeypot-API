import subprocess
import sys

# start FastAPI
subprocess.Popen([
    sys.executable, "-m", "uvicorn",
    "app.main:app", "--reload"
])

# start Streamlit
subprocess.Popen([
    sys.executable, "-m", "streamlit",
    "run", "dashboard.py"
])
