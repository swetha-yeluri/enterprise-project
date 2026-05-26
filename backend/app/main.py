from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import settings
from app.routes.employee_routes import router as employee_router


def create_app() -> FastAPI:
    """
    Application factory — creates and configures the FastAPI instance.
    """
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description=settings.APP_DESCRIPTION,
        docs_url="/docs",
        redoc_url="/redoc",
        
    )

    # ------------------------------------------------------------------ #
    #  CORS Middleware                                                      #
    # ------------------------------------------------------------------ #
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ------------------------------------------------------------------ #
    #  Routers                                                             #
    # ------------------------------------------------------------------ #
    app.include_router(employee_router, prefix=settings.API_PREFIX)

    # ------------------------------------------------------------------ #
    #  Health-check endpoint                                               #
    # ------------------------------------------------------------------ #
    @app.get("/", tags=["Health"])
    def health_check():
        return {
            "app": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "status": "running",
        }

    return app


app = create_app()
