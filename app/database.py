from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)

# Database connection URL for async SQLAlchemy + asyncpg
DATABASE_URL = "postgresql+asyncpg://myuser:mypassword@localhost:5432/mydb"

# Create the async engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # Log SQL queries during development
)

# Create a session factory for async sessions
SessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

async def get_db():
    """Dependency that provides a database session per request."""
    async with SessionLocal() as session:
        yield session