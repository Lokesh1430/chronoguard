"""Runtime settings for local development and Render deployment."""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BACKEND_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env",
        env_prefix="CHRONOGUARD_",
        extra="ignore",
    )

    # ------------------------------------------------------------------
    # Database
    # ------------------------------------------------------------------
    # Local default:
    #   backend/chronoguard.db
    #
    # Render:
    #   Override with CHRONOGUARD_DATABASE_URL
    #
    # Example:
    #   sqlite:////var/data/chronoguard.db
    database_url: str = f"sqlite:///{BACKEND_DIR / 'chronoguard.db'}"

    # ------------------------------------------------------------------
    # File storage
    # ------------------------------------------------------------------
    # Local default:
    #   backend/storage/uploads
    #
    # Render:
    #   Override with CHRONOGUARD_UPLOAD_DIR
    #
    # Example:
    #   /var/data/uploads
    upload_dir: Path = BACKEND_DIR / "storage" / "uploads"

    # ------------------------------------------------------------------
    # Bundled sample datasets
    # ------------------------------------------------------------------
    # Keep this pointing to the project data directory.
    samples_dir: Path = BACKEND_DIR / "data" / "samples"

    # ------------------------------------------------------------------
    # Upload limits
    # ------------------------------------------------------------------
    max_upload_mb: int = 20

    # ------------------------------------------------------------------
    # CORS
    # ------------------------------------------------------------------
    # Local development works without any .env file.
    #
    # Render:
    #   Override with CHRONOGUARD_CORS_ORIGINS
    #
    # Example:
    #   ["https://chronoguard-frontend.onrender.com"]
    cors_origins: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]

    # ------------------------------------------------------------------
    # Sample data seeding
    # ------------------------------------------------------------------
    seed_samples_on_startup: bool = True

    # ------------------------------------------------------------------
    # Optional Azure OpenAI
    # ------------------------------------------------------------------
    # If these values are not configured, ChronoGuard uses its
    # local embedding/explanation fallback.
    azure_openai_endpoint: str | None = None
    azure_openai_api_key: str | None = None
    azure_openai_api_version: str = "2024-10-21"
    azure_openai_embedding_deployment: str | None = None
    azure_openai_chat_deployment: str | None = None

    # ------------------------------------------------------------------
    # Optional Hindsight
    # ------------------------------------------------------------------
    # If these values are not configured, Hindsight remains disabled.
    hindsight_base_url: str | None = None
    hindsight_api_key: str | None = None
    hindsight_bank_id: str = "chronoguard"


@lru_cache
def get_settings() -> Settings:
    """Return the cached application settings."""
    return Settings()
