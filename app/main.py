from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.routes import router
import webbrowser

app = FastAPI(
    title="Agentic Honeypot API",
    version="1.0.0"
)

app.include_router(router)

# root opens API dashboard
@app.get("/")
def home():
    return RedirectResponse(url="/docs")

# auto open browser when FastAPI starts
@app.on_event("startup")
def open_fastapi():
    webbrowser.open_new_tab("http://127.0.0.1:8000")
