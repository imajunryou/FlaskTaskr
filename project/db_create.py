# project/db_create.py

from datetime import date

from views import db
from models import Task

# Create the DB and the DB tables
db.create_all()

# Insert data
db.session.add(Task("Finish this tutorial", date(2017, 12, 25), 10, 1))
db.session.add(Task("Eat some jellybeans", date(2017, 10, 6), 6, 1))

# Commit changes
db.session.commit()
