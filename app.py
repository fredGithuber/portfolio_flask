from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)


@app.route("/")
def index():
    return render_template(f"index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "did not save to database"
    else:
        return "something went wrong. Try again !"


def write_to_file(data):
    with open("database.txt", mode="a") as file:
        for k, v in data.items():
            file.write(f"{k} : {v}\n")


def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])