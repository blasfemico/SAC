from fastapi import APIRouter, HTTPException
from app.services.ip_services import change_ip_and_validate

router = APIRouter(
    prefix="/ip",
    tags=["IP Rotation"]
)

@router.post("/rotate")
def rotate_ip():
    """
    Endpoint para reiniciar la IP y validarla.
    """
    try:
        new_ip = change_ip_and_validate()
        return {"status": "success", "new_ip": new_ip}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
