from database import session

# Dependency
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()