from datetime import datetime, timezone
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

class PokemonCardTradingPlatformException(Exception):
    """Base exception for platform errors"""
    
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)
        
class ConflictError(PokemonCardTradingPlatformException):
    """Exception raised for resource conflicts."""
    
    def __init__(self, message: str = 'Resource conflict'):
        super().__init__(message, status_code=409)
        
class NotFoundError(PokemonCardTradingPlatformException):
    """Exception raised when a resource is not found."""
    
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, status_code=404)