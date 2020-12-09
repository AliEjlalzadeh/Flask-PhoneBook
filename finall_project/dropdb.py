from app.init import db
from app import create_app
from app.packages.phone_book.models import Contact

app = create_app()

with app.app_context():
    db.reflect()
    db.drop_all()
    db.create_all()

    pd = Contact(name="pedram", family="shahsafi", phone_number="09226255415")
    db.session.add(pd)

    kimiya = Contact(name="kimiya", family="abdolahi", phone_number="ffff")
    db.session.add(kimiya)

    db.session.commit()