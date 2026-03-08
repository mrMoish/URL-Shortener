import random
import string
from sqlalchemy.orm import Session
from .models import Link

def generate_short_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_short_url(db: Session, original_url: str):
    short_id = generate_short_id()

    link = Link(
        original_url=original_url,
        short_id=short_id
    )

    db.add(link)
    db.commit()
    db.refresh(link)

    return link

def get_link(db: Session, short_id: str):
    return db.query(Link).filter(Link.short_id == short_id).first()