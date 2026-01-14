# Pokemon Card Trading Platform API

A full-stack backend application built with FastAPI to practice and demonstrate modern backend architecture patterns. This project implements a RESTful API for managing Pokemon cards and trading them.

## 🎯 Purpose

This repository serves as a hands-on practice project for learning and implementing:
- FastAPI framework fundamentals
- Clean architecture and layered design patterns
- PostgreSQL database integration with SQLAlchemy ORM
- RESTful API design principles
- Repository pattern for data access
- Service layer for business logic
- Pydantic schemas for data validation
- Database relationships and associations

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy 2.0
- **Validation**: Pydantic v2
- **Database Driver**: psycopg2-binary
- **Server**: Uvicorn

## 📁 Project Structure

```
Pokemon_Card_Trading_Platform/
├── main.py                     # Application entry point
├── src/
│   ├── api/                    # API layer
│   │   └── v1/                 # API version 1
│   │       ├── router.py       # Route aggregation
│   │       └── type.py         # Type endpoints
│   ├── core/                   # Core utilities
│   │   └── exceptions.py       # Custom exceptions
│   ├── database/               # Database layer
│   │   ├── base.py            # SQLAlchemy base
│   │   ├── core.py            # Database connection
│   │   └── repositories/      # Data access layer
│   │       ├── base.py        # Base repository
│   │       └── type_repository.py
│   ├── models/                 # SQLAlchemy models
│   │   ├── associations.py    # Many-to-many relationships
│   │   ├── type.py            # Type model
│   │   ├── character.py       # Character model
│   │   └── attack.py          # Attack model
│   ├── schemas/                # Pydantic schemas
│   │   └── type.py            # Type schemas
│   ├── service/                # Business logic layer
│   │   └── type_service.py    # Type service
│   └── config.py              # Application configuration
└── .env                        # Environment variables
```

## 🏗️ Architecture

The project follows a **layered architecture** pattern:

1. **API Layer** (`src/api/`): Handles HTTP requests and responses
2. **Service Layer** (`src/service/`): Contains business logic
3. **Repository Layer** (`src/database/repositories/`): Manages data access
4. **Model Layer** (`src/models/`): Defines database entities
5. **Schema Layer** (`src/schemas/`): Validates input/output data

## 🚀 Getting Started

### Prerequisites

- Python 3.14+
- PostgreSQL 18+
- pip or pipenv

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Pokemon_Card_Trading_Platform.git
cd Pokemon_Card_Trading_Platform
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic pydantic-settings
```

4. Set up your PostgreSQL database:
```bash
psql -U your_username -d postgres -c "CREATE DATABASE pokemon_card_trading_platform;"
```

5. Configure environment variables in `.env`:
```env
DATABASE_URL=postgresql://your_username@localhost:5432/pokemon_card_trading_platform
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

6. Run the application:
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## 📚 API Documentation

Once running, visit:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 🎮 Features

### Implemented
- ✅ Type CRUD operations
- ✅ Many-to-many relationships (Types ↔ Characters, Types ↔ Attacks)
- ✅ Database migrations with SQLAlchemy
- ✅ Pydantic validation
- ✅ Repository pattern
- ✅ Service layer pattern
- ✅ CORS middleware

### Database Schema

- **Types**: Pokemon card types (Fire, Water, Grass, etc.)
- **Characters**: Pokemon characters
- **Attacks**: Pokemon attacks
- **Association Tables**: 
  - `character_type`: Links characters to types
  - `attack_type`: Links attacks to types
  - `character_attack`: Links characters to attacks

## 🧪 API Endpoints

### Types
- `POST /api/v1/types/` - Create a new type
- `GET /api/v1/types/` - List all types (with pagination)
- `GET /api/v1/types/{id}` - Get type by ID
- `PUT /api/v1/types/{id}` - Update type
- `DELETE /api/v1/types/{id}` - Delete type

## 📝 Learning Objectives

Through this project, I practiced:
- [x] Setting up FastAPI project structure
- [x] Implementing clean architecture principles
- [x] Working with SQLAlchemy 2.0 ORM
- [x] Creating many-to-many relationships
- [x] Using Pydantic for data validation
- [x] Implementing repository pattern
- [x] Separating business logic into services
- [x] Database connection management
- [x] Error handling and custom exceptions
- [x] Environment-based configuration
- [x] API versioning

## 🔧 Configuration

Key settings in `src/config.py`:
- Database connection
- CORS settings
- Security parameters
- Pagination defaults
- Rate limiting

## 🤝 Contributing

This is a personal learning project, but suggestions and feedback are welcome!

## 📄 License

This project is open source and available for educational purposes.

## 👤 Author

Built by Musab as a practice project for mastering FastAPI and backend development.

---

⭐ Star this repo if you find it helpful for learning FastAPI architecture!
