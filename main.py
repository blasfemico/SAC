from fastapi import FastAPI
from app.routes.ip import router as ip_router
from app.routes.browser import router as browser_router
import uvicorn

app = FastAPI(
    title="IP Rotation System",
    description="Sistema para gestionar la rotación de IP utilizando la interfaz de un router.",
    version="1.0.0"
)


app.include_router(ip_router)
app.include_router(browser_router)

@app.get("/")
def root():
    """
    Endpoint raíz para verificar el estado del sistema.
    """
    return {"message": "ping :D"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True)
