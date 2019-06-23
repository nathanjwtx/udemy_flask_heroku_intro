# split into separate file so it is detected and run by uswgi

from app import app

from db import db
db.init_app(app)

# table definitions are imported from the __tablename__ definitions in the
# models
@app.before_first_request
def create_tables():
    db.create_all()
