from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from .database import SessionLocal
from . import crud, schemas

from fastapi import FastAPI
from .database import engine
from .models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten")
def shorten_url(data: schemas.URLCreate, db: Session = Depends(get_db)):
    link = crud.create_short_url(db, data.url)
    return {"short_id": link.short_id}

@app.get("/{short_id}")
def redirect_url(short_id: str, db: Session = Depends(get_db)):
    link = crud.get_link(db, short_id)

    if not link:
        raise HTTPException(status_code=404)

    link.clicks += 1
    db.commit()

    return RedirectResponse(link.original_url)

@app.get("/stats/{short_id}")
def get_stats(short_id: str, db: Session = Depends(get_db)):
    link = crud.get_link(db, short_id)

    if not link:
        raise HTTPException(status_code=404)

    return {"clicks": link.clicks}