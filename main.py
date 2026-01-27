from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.config import get_settings
from src.api.v1.router import api_router
from src.models import Type, Character, Attack  # Import models to register them
from src.core.exceptions import PokemonCardTradingPlatformException

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

# Exception handler for custom exceptions
@app.exception_handler(PokemonCardTradingPlatformException)
async def pokemon_exception_handler(request: Request, exc: PokemonCardTradingPlatformException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix='/api/v1')
