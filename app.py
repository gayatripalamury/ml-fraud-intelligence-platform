from flask import Flask, render_template, request, redirect
from database.db import init_db, get_all_transactions
from utils.analytics import get_system_stats
from utils.analytics import get_system_stats
from services.explanation_engine import get_fraud_explanation
from ml.predict import predict_transaction

app = Flask(__name__)

# initialize database
init_db()

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # allow login if user enters anything
        if username and password:
            return redirect("/dashboard")

        else:
            return "Please enter username and password"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    transactions = get_all_transactions()

    stats = get_system_stats()

    prediction, probability = predict_transaction(
        amount=12000,
        hour=2,
        device_change=1,
        location_change=1
    )

    example_transaction = {
        "amount":12000,
        "hour":2,
        "risk_score":probability
    }

    explanations = get_fraud_explanation(example_transaction)

    return render_template(
        "dashboard.html",
        transactions=transactions,
        stats=stats,
        probability=probability,
        prediction=prediction,
        explanations=explanations
    )


if __name__ == "__main__":
    app.run(debug=True)