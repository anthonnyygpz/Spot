from fastapi import FastAPI

# from fastapi.middleware.cors import CORSMiddleware

from .routers import artists, albums,tracks
# from app.routers import

# from docs.documentation import configure_docs

app = FastAPI(title="Spot", version="1.0.0")
app.include_router(artists.router)
app.include_router(albums.router)
app.include_router(tracks.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=10000)
