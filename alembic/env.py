import sys
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Ensure Alembic can import your application modules (e.g., app.models)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import your SQLAlchemy Base
from app.models.base import Base

# Alembic Config object, giving access to values within alembic.ini
config = context.config

# Configure Python logging using alembic.ini if available
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata used for autogeneration of migrations
target_metadata = Base.metadata


def run_migrations_offline():
    """
    Run migrations in 'offline' mode.

    In offline mode, Alembic does not create a database engine.
    Instead, it generates SQL statements using the database URL.
    """
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,            # Embed values directly into SQL
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """
    Run migrations in 'online' mode.

    In online mode, Alembic creates a real SQLAlchemy engine and
    applies migrations directly to the database.
    """

    # Retrieve the Alembic configuration section from alembic.ini.
    # Pyright warns this may return None, so we assert for type safety.
    section = config.get_section(config.config_ini_section)
    assert section is not None  # Safe: Alembic always provides this when running migrations.

    # Create a SQLAlchemy engine using the Alembic configuration.
    connectable = engine_from_config(
        section,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    # Connect to the database and configure the migration context.
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,            # Detect column type changes
            compare_server_default=True,  # Detect default value changes
        )

        # Apply migrations inside a transaction.
        with context.begin_transaction():
            context.run_migrations()


# Determine whether Alembic is running in offline or online mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()