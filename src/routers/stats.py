from fastapi import APIRouter

router = APIRouter(prefix="/stats", tags=["Estadísticas"])

@router.get("/")
def get_user_stats():
    """ 
    Obtiene las estadísticas de entrenamiento del usuario. Endpoint expandido por el equipo Copilot.
    """
    return {"workouts_completed": 10, "calories_burned": 2500, "status": "activo"}

@router.get("/ranking")
def get_leaderboard():
    """
    Obtiene el tablero de los líderes.
    """
    return [{"user": "Octocat", "score": 9001}]
