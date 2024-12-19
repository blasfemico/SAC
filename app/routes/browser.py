from fastapi import APIRouter, HTTPException
from app.services.browser_services import create_browser_profile, open_browser_with_profile

router = APIRouter(
    prefix="/browser",
    tags=["Browser Management"]
)

@router.post("/create/{profile_name}")
def create_profile(profile_name: str):
    """
    Endpoint para crear perfiles únicos.
    """
    try:
        path = create_browser_profile(profile_name)
        return {"status": "success", "message": f"Perfil '{profile_name}' creado.", "path": path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/open-browser/{profile_name}")
def open_browser(profile_name: str):
    """
    Abre un navegador local con un perfil único y User-Agent aleatorio.
    """
    try:
        open_browser_with_profile(profile_name)
        return {
            "status": "success",
            "message": f"Navegador con perfil '{profile_name}' abierto localmente."
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
