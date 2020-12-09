from flask import Blueprint, render_template, request, redirect
from .models import Contact
from .forms import ContactForm
from app.init import db

bp = Blueprint(
    "contact",
    __name__,
    template_folder="templates",
)


@bp.route("/index", )
def say_hello():
    contacts = Contact.query.all()
    return render_template("phone_book/index.html", contacts=contacts)
    

@bp.route("/add-user", methods=["POST", "GET"])
def add_user():
    form = ContactForm()
    if form.validate_on_submit():
        c = Contact(name=form.name.data, family=form.family.data, phone_number=form.phone_number.data)
        db.session.add(c)
        db.session.commit()
        return redirect("/index")
    return render_template("phone_book/add_user.html", form=form)


@bp.route("/edit-user/<id>",methods=["POST","GET"])
def edit_user(id):
    contact=Contact.query.get(id)
    form = ContactForm()
    if form.validate_on_submit():
        contact.name = form.name.data
        contact.family = form.family.data
        contact.phone_number = form.phone_number.data
        db.session.commit()
        return redirect("/index")
    form.name.data = contact.name
    form.family.data = contact.family
    form.phone_number.data = contact.phone_number
    return render_template("phone_book/add_user.html", form=form)

@bp.route("/delete-user/<id>",methods=["POST","GET"])
def delete_user(id):
    contact=Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect("/index")
   