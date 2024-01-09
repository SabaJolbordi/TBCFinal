from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_remembered
from os import path
from werkzeug.security import check_password_hash

from forms import RegisterForm, LoginForm, AddProductForm, EditProductForm
from models import User, Product

import os
import uuid
from ext import app, db


products = [
    {"img": "img.jpg", "maintitle": "Drawing competition", "card_title": "cardtexxxxxxtiiiii", "time": "Dec 20, 14.30",
     "id": 0},
    {"img": "img.jpg", "maintitle": "satauri", "card_title": "cardtexxxxxxtiiiii", "time": "Dec 20, 14.30", "id": 1},

]


@app.route("/activities")
def activities():
    products = Product.query.all()
    return render_template("activities.html", products=products)


def path_join(root_path, param, filename):
    pass















# @app.route("/add_product", methods=["POST", "GET"])
# def add_product():
#     # products = None
#     # products = []
#     form = AddProductForm()
#     if form.validate_on_submit():
#         # print(form.title.data)
#         new_product = {
#             "maintitle": form.maintitle.data,
#             "img": form.img.data.filename,
#             "card_title": form.card_title.data,
#             "time": form.time.data,
#             "id": len(products)
#         }
#
#         file_dir = path.join(app.root_path, "static", form.img.data.filename)
#         form.img.data.save(file_dir)
#         products.append(new_product)
#     print(form.errors)
#     return redirect("/activities")
#     return render_template("add_product.html", form=form)



@app.route("/edit_product/<int:index>", methods=["GET", "POST"])
def edit_product(index):
    product = Product.query.get(index)

    if product is None:
        flash('Product not found', 'error')
        return redirect("/activities")

    form = EditProductForm(obj=product)

    if form.validate_on_submit():
        try:
            # Update the product data with the edited form data
            product.maintitle = form.maintitle.data
            product.img = form.img.data.filename
            product.card_title = form.card_title.data
            product.time = form.time.data

            # Save the changes to the database
            db.session.commit()

            flash('Product updated successfully', 'success')

            # Redirect to the activities page or wherever you want after editing
            return redirect("/activities")

        except Exception as e:
            # Handle exceptions, possibly roll back changes
            db.session.rollback()
            flash('An error occurred while updating the product', 'error')

    return render_template("edit_product.html", form=form, product=product)


# @app.route("/edit_product/<int:index>", methods=["GET", "POST"])
# def edit_product(index):
#     product = Product.query.get(index)
#     form = EditProductForm(obj=product)
#
#     if form.validate_on_submit():
#         # Update the product attributes with the form data
#         product.maintitle = form.maintitle.data
#         product.card_title = form.card_title.data
#         product.time = form.time.data
#
#         # Check if a new image is provided in the form
#         if form.img.data:
#             # Save the new image
#             file_dir = path.join(app.root_path, "static", form.img.data.filename)
#             form.img.data.save(file_dir)
#             product.img = form.img.data.filename
#
#         db.session.commit()
#         flash('Product updated successfully!', 'success')
#         return redirect("/activities")
#
#     return render_template("edit_product.html", form=form, product=product)


#
# @app.route("/delete_product/<int:index>")
# def delete_product(index):
#     product = Product.query.get(index)        ####   hoda ras giyvebodi amashi
#     db.sesion.delete(product)
#     db.session.commit()
#     return redirect("/activities")


@app.route("/delete_product/<int:index>")
def delete_product(index):
    product = Product.query.get(index)

    if product:
        db.session.delete(product)
        db.session.commit()

    return redirect("/activities")


@app.route("/add_product", methods=["POST", "GET"])
def add_product():
    form = AddProductForm()

    if form.validate_on_submit():
        # Generate a unique filename for the uploaded file
        unique_filename = str(uuid.uuid4()) + os.path.splitext(form.img.data.filename)[1]

        new_product = Product(
            maintitle=form.maintitle.data,
            img=unique_filename,  # Store the filename in the database
            card_title=form.card_title.data,
            time=form.time.data
        )

        db.session.add(new_product)
        db.session.commit()

        # Save the file to the server
        file_dir = path.join(app.root_path, "static", unique_filename)
        form.img.data.save(file_dir)

        return redirect("/activities")

    return render_template("add_product.html", form=form)
# @app.route("/add_product", methods=["POST", "GET"])
# def add_product():
#     # products = [...]
#
#     form = AddProductForm()
#
#     if form.validate_on_submit():
#         # new_product = {
#         #     "maintitle": form.maintitle.data,
#         #     "img": form.img.data.filename,
#         #     "card_title": form.card_title.data,
#         #     "time": form.time.data,
#         #     "id": len(products)
#         # }
#         new_product = Product(maintitle=form.maintitle.data, img=form.img.data, card_title=form.card_title.data, time=form.time.data)
#         db.session.add(new_product)
#         db.session.commit()
#         file_dir = path.join(app.root_path, "static", form.img.data.filename)
#         form.img.data.save(file_dir)
#         # products.append(new_product)
#         return redirect("/activities")
#     return render_template("add_product.html", form=form)




# products = []

# @app.route("/add_product", methods=["POST", "GET"])
# def add_product():
#     form = AddProductForm()
#     if form.validate_on_submit():
#         new_product = {
#             "title": form.title.data,
#             "img": form.img.data,
#             "cardtitle": form.cardtitle.data,
#             "time": form.time.data,
#             "id": len(products)
#         }
#         products.append(new_product)
#         flash('Product added successfully!', 'success')
#         return redirect(url_for('add_product'))  # Redirect to the same page after form submission
#     return render_template("add_product.html", form=form)

@app.route("/")
def home():
    # print(f"{app.root_path}\\static")    yuradgebaaaa
    return render_template("index.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

#    <3             eseseseseseseseseesseesesesseese
# @app.route("/edit_product/<int:index>")
# def edit_product(index):
#     product = Product.query.get(index)
#     from = AddProductForm()
#
#
#
#     return redirect("/edit_product")
#
# @app.route("/edit_product")
# def edit_product():
#     return render_template("edit_product.html")


@app.route("/activities")
def show_activities():
    return render_template("activities.html")


# @app.route("/results")
# def show_results():
#     return render_template("results.html")
#
# @app.route("/results", methods=['GET', 'POST'])
# def show_results():
#     message_form = MessageForm()
#
#     if message_form.validate_on_submit():
#         # Process the submitted message
#         message = message_form.message.data
#         flash(f'Message submitted: {message}', 'success')
#
#     return render_template("results.html", message_form=message_form)

@app.route('/results', methods=['GET', 'POST'])
def show_results():
    # message_form = MessageForm()
    #
    # if message_form.validate_on_submit():
    #     # Process the submitted message
    #     message = message_form.message.data
    #     flash(f'Message submitted: {message}', 'success')
    #
    # # Your existing logic for fetching and rendering results
    # # ...

    return render_template('results.html')




@app.route("/about_us")
def about_us():
    return render_template("aboutus.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        user.create()
        # print(form.username.data)
        # print(form.password.data)
        # print(form.confirmPassword.data)

        return redirect("/login")
        # YURADGEBS MIACIEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        # if user and user.check_password(form.password.data):
        # if user and user.password == form.password.data:
        if user and check_password_hash(user.password, form.password.data):
            # uyureee daakvirdiiiiiiiiiii gaitvaliswineeee uewvwliiiiiiiiiiiii
            login_user(user)
            return redirect("/")
    return render_template("login.html", form=form)

@app.route('/like/<int:product_id>')
def like_product(product_id):
    product = Product.query.get(product_id)
    if product:
        product.likes += 1
        db.session.commit()
    return redirect(url_for('activities'))

# if __name__ == "__main__":
#     app.run(debug=True)
